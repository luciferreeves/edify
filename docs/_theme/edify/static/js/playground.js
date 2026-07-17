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
  "&.cm-focused .cm-selectionBackground, .cm-selectionBackground, .cm-content ::selection": {
    backgroundColor: "var(--accent-weak)",
  },
  ".cm-matchingBracket, .cm-nonmatchingBracket": {
    backgroundColor: "var(--accent-weak)", outline: "none",
  },
});

const editorHighlight = HighlightStyle.define([
  { tag: t.keyword, color: "var(--accent-strong)" },
  { tag: [t.function(t.variableName), t.function(t.propertyName), t.propertyName], color: "var(--accent)" },
  { tag: [t.string, t.special(t.string)], color: "#7c93e8" },
  { tag: [t.number, t.bool, t.null], color: "#d98a3d" },
  { tag: t.comment, color: "var(--faint)", fontStyle: "italic" },
  { tag: [t.operator, t.punctuation, t.separator, t.bracket], color: "var(--muted)" },
  { tag: t.variableName, color: "var(--fg)" },
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

function decodeSource(root) {
  const raw = root.getAttribute("data-source") || "";
  try {
    const decoded = atob(raw);
    if (btoa(decoded) === raw) return decoded;
  } catch (e) {
    // Not base64 — the attribute is a plain-text chain.
  }
  return raw;
}

function mount(root) {
  const source = decodeSource(root);
  root.replaceChildren();
  root.classList.add("pg-live");

  const grid = el("div", "pg-grid");
  const left = el("div", "pg-left");
  const builderPane = el("div", "pg-pane pg-builder");
  builderPane.appendChild(head("Builder", "pg-status", "click to run ▸"));
  const editorHost = el("div", "pg-editor");
  builderPane.appendChild(editorHost);

  const regexPane = el("div", "pg-pane pg-regex");
  regexPane.appendChild(head("Emitted regex"));
  const regexOut = el("pre", "pg-code pg-regex-out", "");
  regexPane.appendChild(regexOut);
  left.appendChild(builderPane);
  left.appendChild(regexPane);

  const testPane = el("div", "pg-pane pg-test");
  testPane.appendChild(head("Test strings", "pg-count"));
  const testArea = el("textarea", "pg-test-input");
  testArea.spellcheck = false;
  testArea.value = "2024\n90210\nabcd\n12";
  const testResults = el("div", "pg-test-results");
  testPane.appendChild(testArea);
  testPane.appendChild(testResults);

  grid.appendChild(left);
  grid.appendChild(testPane);
  root.appendChild(grid);

  const status = builderPane.querySelector(".pg-status");
  const count = testPane.querySelector(".pg-count");

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

  async function refreshTests() {
    const lines = testArea.value.split("\n");
    testResults.replaceChildren();
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
      testResults.appendChild(row);
    }
    count.textContent = tested ? matches + " / " + tested + " match" : "";
  }

  async function run() {
    status.textContent = "loading Python…";
    let result;
    try {
      result = await runEdify(view.state.doc.toString(), (s) => {
        status.textContent = s === "ready" ? "running ●" : "installing edify…";
      });
    } catch (e) {
      status.textContent = "error";
      regexOut.textContent = String(e);
      return;
    }
    status.textContent = "running ●";
    if (result.error) {
      regexPane.classList.add("has-error");
      regexOut.textContent = result.error;
      testResults.replaceChildren();
      count.textContent = "";
      return;
    }
    regexPane.classList.remove("has-error");
    if (result.engineUnsupported) {
      regexOut.textContent =
        result.regex +
        "\n\n(the 'regex' engine isn't bundled in the browser — use the default engine to test here.)";
      return;
    }
    if (result.regex != null) {
      regexOut.textContent = result.regex;
      await refreshTests();
    } else {
      regexOut.textContent = result.value != null ? result.value : "";
      testResults.replaceChildren();
      count.textContent = "";
    }
  }

  const scheduleRun = debounce(run, 400);
  testArea.addEventListener("input", debounce(refreshTests, 300));

  // Lazy: only boot Pyodide when the visitor first interacts with this widget.
  let booted = false;
  function boot() {
    if (booted) return;
    booted = true;
    run();
  }
  editorHost.addEventListener("focusin", boot, { once: true });
  builderPane.querySelector(".pg-pane-head").addEventListener("click", boot);
}

document.addEventListener("DOMContentLoaded", () => {
  if (!document.querySelector(".edify-playground")) return;
  document.querySelectorAll(".edify-playground").forEach(mount);
});
