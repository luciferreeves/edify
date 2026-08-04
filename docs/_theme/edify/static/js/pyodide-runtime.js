// Lazy, page-shared Pyodide runtime that installs the edify wheel and runs a
// small Python harness for compiling a chain and testing strings against it.

const PYODIDE_URL = "https://cdn.jsdelivr.net/pyodide/v0.28.2/full/pyodide.mjs";

let _runtimePromise = null;

// The harness below intentionally exec/eval's the user's snippet. That is the
// whole point of a playground: it runs the visitor's own edify code, inside the
// Pyodide WebAssembly sandbox in their own browser — no host filesystem or
// network access, nothing sent anywhere. This is not a server-side eval.
const HARNESS = String.raw`
import ast, json
import edify
import edify.library as _lib
from edify.errors.backend import MissingRegexBackendError

_ns_base = {k: getattr(edify, k) for k in edify.__all__}
_ns_base.update({k: getattr(_lib, k) for k in dir(_lib) if not k.startswith("_")})
_state = {"regex": None}

# The alternate engine is a compiled extension, so it cannot load in WebAssembly.
# Its own diagnostic says to pip install the extra, which a reader in a browser
# cannot act on, so the playground answers with what is true here instead.
_NO_ALTERNATE_ENGINE = (
    "engine='regex' is not available in this playground: it is a compiled extension "
    "and cannot load in the browser. Drop the argument to compile with the default "
    "engine, or install edify[regex] to use it locally."
)

def _regex_string(target, regex):
    if regex is None and _state["regex"] is None:
        try:
            _state["regex"] = target.to_regex()
        except Exception:
            pass
    return target.to_regex_string()

def edify_run(src):
    _state["regex"] = None
    ns = dict(_ns_base)
    try:
        tree = ast.parse(src, mode="exec")
    except SyntaxError as problem:
        return json.dumps({"error": "syntax error: " + (problem.msg or "invalid syntax"), "results": [], "regex": None})
    results = []
    regex = None
    for node in tree.body:
        try:
            if isinstance(node, ast.Expr):
                code = ast.get_source_segment(src, node) or ""
                value = eval(compile(ast.Expression(node.value), "<playground>", "eval"), ns)
                if isinstance(value, bool):
                    results.append({"code": code, "kind": "bool", "value": value})
                    if regex is None and isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name):
                        target = ns.get(node.value.func.id)
                        if hasattr(target, "to_regex_string"):
                            regex = _regex_string(target, regex)
                elif hasattr(value, "to_regex_string"):
                    if regex is None:
                        regex = _regex_string(value, regex)
                elif value is not None:
                    results.append({"code": code, "kind": "value", "value": repr(value)})
            else:
                module = ast.Module(body=[node], type_ignores=[])
                ast.fix_missing_locations(module)
                exec(compile(module, "<playground>", "exec"), ns)
        except MissingRegexBackendError:
            return json.dumps({"error": _NO_ALTERNATE_ENGINE, "results": results, "regex": regex})
        except edify.EdifyError as problem:
            return json.dumps({"error": str(problem), "results": results, "regex": regex})
        except Exception as problem:
            return json.dumps({"error": type(problem).__name__ + ": " + str(problem), "results": results, "regex": regex})
    return json.dumps({"regex": regex, "results": results})

def edify_test(line):
    rx = _state.get("regex")
    if rx is None:
        return False
    try:
        return bool(rx.search(line))
    except Exception:
        return False
`;

export function getRuntime(onStatus) {
  if (!_runtimePromise) {
    _runtimePromise = _load(onStatus);
  }
  return _runtimePromise;
}

async function _load(onStatus) {
  if (onStatus) onStatus("loading");
  const { loadPyodide } = await import(PYODIDE_URL);
  const pyodide = await loadPyodide();
  await pyodide.loadPackage("micropip");
  const micropip = pyodide.pyimport("micropip");
  const wheelUrl = new URL(window.EDIFY_WHEEL_URL, document.baseURI).href;
  await micropip.install(wheelUrl);
  pyodide.runPython(HARNESS);
  if (onStatus) onStatus("ready");
  return pyodide;
}

export async function runEdify(source, onStatus) {
  const pyodide = await getRuntime(onStatus);
  const raw = pyodide.runPython(`edify_run(${JSON.stringify(source)})`);
  return JSON.parse(raw);
}

export async function testLine(line) {
  const pyodide = await getRuntime();
  return pyodide.runPython(`edify_test(${JSON.stringify(line)})`);
}
