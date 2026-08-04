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


# Hosts that refuse automated clients outright while staying reachable in a browser.
# Ignoring them keeps the citation in the prose instead of trading a good reference
# for a weaker one. Sending a browser user agent is not the answer: w3.org rejects
# that in turn, so the set of reachable hosts only moves around.
linkcheck_ignore = [
    # Answer 403 to automated clients.
    r"https://www\.iso\.org/",
    r"https://www\.gs1\.org/",
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
