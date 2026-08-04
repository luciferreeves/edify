// Interactive playground: a CodeMirror editor over the edify chain, with
// as-you-type autocomplete from window.EDIFY_API, a live emitted-regex pane, and
// a test area that runs each line against the compiled pattern via Pyodide.

import { EditorView, basicSetup } from "https://esm.sh/codemirror@6.0.1";
import { python } from "https://esm.sh/@codemirror/lang-python@6.1.6";
import { autocompletion } from "https://esm.sh/@codemirror/autocomplete@6.18.1";
import { HighlightStyle, syntaxHighlighting } from "https://esm.sh/@codemirror/language@6.10.2";
import { tags as t } from "https://esm.sh/@lezer/highlight@1.2.0";
import { runEdify, testLine } from "./pyodide-runtime.js";

const API = window.EDIFY_API || [];
const KIND = { method: "method", constant: "constant", function: "function" };

// Structural colors reference the theme's CSS custom properties, so the editor
// follows the site's light/dark toggle without a second theme definition.
const editorTheme = EditorView.theme({
  "&": { backgroundColor: "transparent", color: "var(--fg)", fontSize: "0.82rem" },
  ".cm-content": { fontFamily: "var(--mono)", padding: "12px 0", caretColor: "var(--fg)" },
  ".cm-cursor, .cm-dropCursor": { borderLeftColor: "var(--fg)" },
  ".cm-gutters": { backgroundColor: "transparent", color: "var(--faint)", border: "none" },
  ".cm-activeLine": { backgroundColor: "var(--accent-weak)" },
  ".cm-activeLineGutter": { backgroundColor: "transparent", color: "var(--fg)" },
  ".cm-lineNumbers .cm-gutterElement": { padding: "0 10px 0 10px" },
  "&.cm-focused > .cm-scroller > .cm-selectionLayer .cm-selectionBackground, .cm-selectionBackground":
    { background: "var(--select)" },
  ".cm-line ::selection, .cm-line::selection, .cm-content ::selection": {
    backgroundColor: "var(--select)",
  },
  ".cm-selectionMatch": { backgroundColor: "var(--select)" },
  ".cm-matchingBracket, .cm-nonmatchingBracket": {
    backgroundColor: "var(--accent-weak)", outline: "none",
  },
});

// GitHub-style token colors, wired to theme-switching CSS custom properties.
const editorHighlight = HighlightStyle.define([
  { tag: t.keyword, color: "var(--syn-keyword)" },
  { tag: [t.function(t.variableName), t.function(t.propertyName), t.propertyName], color: "var(--syn-function)" },
  { tag: [t.string, t.special(t.string)], color: "var(--syn-string)" },
  { tag: [t.number, t.bool, t.null], color: "var(--syn-constant)" },
  { tag: t.comment, color: "var(--syn-comment)", fontStyle: "italic" },
  { tag: [t.operator, t.punctuation, t.separator, t.bracket], color: "var(--syn-punct)" },
  { tag: [t.variableName, t.className], color: "var(--fg)" },
]);

function edifyCompletions(context) {
  const token = context.matchBefore(/[\w.]*/);
  if (!token || (token.from === token.to && !context.explicit)) return null;
  const dot = token.text.lastIndexOf(".");
  const from = dot >= 0 ? token.from + dot + 1 : token.from;
  return {
    from,
    options: API.map((item) => ({
      label: item.label,
      detail: item.detail || undefined,
      info: item.doc || undefined,
      type: KIND[item.kind] || "variable",
    })),
  };
}

function el(tag, cls, text) {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text != null) node.textContent = text;
  return node;
}

function head(label, badgeCls, badgeText) {
  const node = el("div", "pg-pane-head", label);
  if (badgeCls) node.appendChild(el("span", badgeCls, badgeText || ""));
  return node;
}

function debounce(fn, ms) {
  let t;
  return (...args) => {
    clearTimeout(t);
    t = setTimeout(() => fn(...args), ms);
  };
}

function decodeAttr(root, name, fallback) {
  const raw = root.getAttribute(name);
  if (raw == null) return fallback;
  try {
    const decoded = atob(raw);
    if (btoa(decoded) === raw) return decoded;
  } catch (e) {
    // Not base64 — the attribute is plain text.
  }
  return raw;
}

function mount(root) {
  const source = decodeAttr(root, "data-source", "");
  const tests = decodeAttr(root, "data-tests", null);
  const buildMode = tests != null;
  root.replaceChildren();
  root.classList.add("pg-live");

  const grid = el("div", "pg-grid");
  const left = el("div", "pg-left");
  const builderPane = el("div", "pg-pane pg-builder");
  builderPane.appendChild(head("edify", "pg-status", ""));
  const editorHost = el("div", "pg-editor");
  builderPane.appendChild(editorHost);

  const regexPane = el("div", "pg-pane pg-regex");
  regexPane.appendChild(head("Emitted regex"));
  const regexOut = el("pre", "pg-code pg-regex-out", "");
  regexPane.appendChild(regexOut);
  left.appendChild(builderPane);
  left.appendChild(regexPane);

  const outPane = el("div", "pg-pane pg-test");
  outPane.appendChild(head(buildMode ? "Test strings" : "Result", "pg-count"));
  let testArea = null;
  if (buildMode) {
    testArea = el("textarea", "pg-test-input");
    testArea.spellcheck = false;
    testArea.value = tests;
    outPane.appendChild(testArea);
  }
  const outResults = el("div", "pg-test-results");
  outPane.appendChild(outResults);

  grid.appendChild(left);
  grid.appendChild(outPane);
  root.appendChild(grid);

  const status = builderPane.querySelector(".pg-status");
  const count = outPane.querySelector(".pg-count");

  const view = new EditorView({
    doc: source,
    extensions: [
      basicSetup,
      python(),
      editorTheme,
      syntaxHighlighting(editorHighlight),
      autocompletion({ override: [edifyCompletions], icons: true }),
      EditorView.updateListener.of((u) => {
        if (u.docChanged) scheduleRun();
      }),
    ],
    parent: editorHost,
  });

  // run mode (library pages): each call in the source, with its live True/False
  function renderResults(data) {
    outResults.replaceChildren();
    const results = data.results || [];
    let hits = 0;
    let bools = 0;
    for (const item of results) {
      const row = el("div", "pg-test-row");
      if (item.kind === "bool") {
        bools += 1;
        if (item.value) hits += 1;
        row.classList.add(item.value ? "pg-hit" : "pg-miss");
        row.appendChild(el("span", "pg-mark", item.value ? "✓" : "✗"));
        row.appendChild(el("code", "pg-str", item.code));
        row.appendChild(el("span", "pg-bool", item.value ? "True" : "False"));
      } else {
        row.classList.add("pg-val");
        row.appendChild(el("code", "pg-str", item.code));
        row.appendChild(el("span", "pg-outval", item.value));
      }
      outResults.appendChild(row);
    }
    if (data.error) {
      const errRow = el("div", "pg-test-row pg-miss pg-err");
      errRow.appendChild(el("span", "pg-mark", "!"));
      errRow.appendChild(el("span", "pg-str", data.error));
      outResults.appendChild(errRow);
    }
    count.textContent = bools ? hits + " / " + bools + " match" : "";
  }

  // build mode (playground + guide): editable strings tested against the pattern
  async function refreshTests() {
    const lines = testArea.value.split("\n");
    outResults.replaceChildren();
    let matches = 0;
    let tested = 0;
    for (const line of lines) {
      if (line === "") continue;
      tested += 1;
      let ok = false;
      try {
        ok = await testLine(line);
      } catch (e) {
        ok = false;
      }
      if (ok) matches += 1;
      const row = el("div", "pg-test-row " + (ok ? "pg-hit" : "pg-miss"));
      row.appendChild(el("span", "pg-mark", ok ? "✓" : "✗"));
      row.appendChild(el("span", "pg-str", line));
      outResults.appendChild(row);
    }
    count.textContent = tested ? matches + " / " + tested + " match" : "";
  }

  async function run() {
    status.textContent = "loading…";
    let data;
    try {
      data = await runEdify(view.state.doc.toString(), (s) => {
        status.textContent = s === "ready" ? "" : "installing edify…";
      });
    } catch (e) {
      status.textContent = "error";
      regexOut.textContent = "";
      outResults.replaceChildren();
      outResults.appendChild(el("div", "pg-test-row pg-miss pg-err", String(e)));
      return;
    }
    status.textContent = "";
    regexPane.classList.toggle("has-error", Boolean(data.error));
    regexOut.textContent = data.regex || (data.error ? "" : "—");
    if (!buildMode) {
      renderResults(data);
    } else if (data.error) {
      outResults.replaceChildren();
      outResults.appendChild(el("div", "pg-test-row pg-miss pg-err", data.error));
      count.textContent = "";
    } else {
      await refreshTests();
    }
  }

  const scheduleRun = debounce(run, 400);
  if (buildMode) testArea.addEventListener("input", debounce(refreshTests, 300));

  // Boot the shared runtime as soon as the widget scrolls into view, so every
  // playground runs on its own without a click. The runtime is memoised, so
  // multiple widgets on a page share a single Pyodide load.
  let booted = false;
  function boot() {
    if (booted) return;
    booted = true;
    run();
  }
  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver((entries) => {
      if (entries.some((entry) => entry.isIntersecting)) {
        observer.disconnect();
        boot();
      }
    }, { rootMargin: "200px" });
    observer.observe(root);
  } else {
    boot();
  }
}

document.addEventListener("DOMContentLoaded", () => {
  if (!document.querySelector(".edify-playground")) return;
  document.querySelectorAll(".edify-playground").forEach(mount);
});
