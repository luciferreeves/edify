import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "_ext"))

project = "Edify"
author = "Bobby"
copyright = "2022-2026, Bobby"
release = version = "1.0.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "playground",
    "autolink",
    "signatures",
    "codelinks",
]

intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}
intersphinx_timeout = 30

extlinks = {
    "issue": ("https://github.com/luciferreeves/edify/issues/%s", "#%s"),
    "pr": ("https://github.com/luciferreeves/edify/pull/%s", "PR #%s"),
}

source_suffix = {".rst": "restructuredtext"}
root_doc = "index"

html_theme = "edify"
html_theme_path = ["_theme"]
html_static_path = ["_static"]
html_permalinks = False
html_title = "Edify"

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False

python_use_unqualified_type_names = True
autodoc_member_order = "bysource"


# Hosts linkcheck cannot reach even though the links are good, so the citations stay
# in the prose rather than being traded for weaker references.
linkcheck_ignore = [
    # Serve 403 to automated clients while remaining reachable in a browser.
    r"https://www\.iso\.org/",
    r"https://www\.icao\.int/",
    r"https://www\.ssa\.gov/",
    # Publishes an AAAA record; CI runners have no IPv6 route, so every request
    # fails with "network is unreachable" regardless of the URL being valid.
    r"https://www\.gnu\.org/",
]
linkcheck_retries = 2
linkcheck_timeout = 30
linkcheck_workers = 5


def _wheel_filename() -> str:
    wheels = sorted((Path(__file__).parent / "_static").glob("edify-*.whl"))
    return wheels[-1].name if wheels else ""


html_context = {"edify_wheel_filename": _wheel_filename()}
