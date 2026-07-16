"""Shared pytest fixtures + Hypothesis profile registration.

Registers three Hypothesis profiles chosen at collection time via the
``EDIFY_HYPOTHESIS_PROFILE`` environment variable:

* ``dev`` (default) — fast, 50 examples per property.
* ``ci`` — 300 examples, deterministic seed via HYPOTHESIS_DATABASE_FILE.
* ``nightly`` — 2000 examples with the shrinker granted extra time.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

from hypothesis import HealthCheck, Verbosity, settings

_REPO_ROOT = Path(__file__).parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

_PROFILE_ENVIRONMENT_VARIABLE = "EDIFY_HYPOTHESIS_PROFILE"


settings.register_profile(
    "dev",
    max_examples=50,
    deadline=None,
    verbosity=Verbosity.normal,
    suppress_health_check=[HealthCheck.too_slow],
)
settings.register_profile(
    "ci",
    max_examples=300,
    deadline=None,
    verbosity=Verbosity.normal,
    suppress_health_check=[HealthCheck.too_slow],
)
settings.register_profile(
    "nightly",
    max_examples=2000,
    deadline=None,
    verbosity=Verbosity.verbose,
    suppress_health_check=[HealthCheck.too_slow],
)

_chosen_profile = os.environ.get(_PROFILE_ENVIRONMENT_VARIABLE, "dev")
settings.load_profile(_chosen_profile)
