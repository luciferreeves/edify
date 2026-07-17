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
from edify.introspect import explain_elements

_ns_base = {k: getattr(edify, k) for k in edify.__all__}
_ns_base.update({k: getattr(_lib, k) for k in dir(_lib) if not k.startswith("_")})
_state = {"regex": None}

def _eval_source(src):
    ns = dict(_ns_base)
    block = ast.parse(src, mode="exec")
    result = None
    if block.body and isinstance(block.body[-1], ast.Expr):
        last = block.body.pop()
        exec(compile(block, "<playground>", "exec"), ns)
        result = eval(compile(ast.Expression(last.value), "<playground>", "eval"), ns)
    else:
        exec(compile(block, "<playground>", "exec"), ns)
    return result

def edify_run(src):
    _state["regex"] = None
    try:
        result = _eval_source(src)
    except edify.EdifyError as problem:
        return json.dumps({"error": str(problem)})
    except SyntaxError as problem:
        return json.dumps({"error": "syntax error: " + (problem.msg or "invalid syntax")})
    except Exception as problem:
        return json.dumps({"error": str(problem)})
    if hasattr(result, "to_regex_string"):
        try:
            compiled = result.to_regex()
        except Exception as problem:
            name = type(problem).__name__
            if "Regex" in name or "Backend" in name or "regex" in str(problem).lower():
                return json.dumps({"engineUnsupported": True, "regex": result.to_regex_string()})
            return json.dumps({"error": str(problem)})
        _state["regex"] = compiled
        return json.dumps({
            "regex": result.to_regex_string(),
            "explain": explain_elements(compiled.elements),
        })
    if isinstance(result, bool):
        return json.dumps({"value": "True" if result else "False"})
    return json.dumps({"value": repr(result)})

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
