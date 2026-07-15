"""Exception raised when an integration module needs a framework the user has not installed."""

from __future__ import annotations

from edify.errors.formatting import compose_annotated_message
from edify.errors.syntax import EdifySyntaxError


class MissingIntegrationDependencyError(EdifySyntaxError):
    """Raised when an ``edify.integrations.<framework>`` helper runs without the framework.

    Args:
        framework: The framework name as it appears in the extras marker
            (``"pydantic"``, ``"fastapi"``, ``"django"``).
    """

    def __init__(self, framework: str) -> None:
        message = compose_annotated_message(
            summary=(
                f"the edify.integrations.{framework} module requires the {framework!r} "
                "package, which is not installed"
            ),
            trigger_hint=f"edify.integrations.{framework} helper called here",
            note=(
                f"the {framework!r} integration ships as an opt-in extra so pip install "
                "edify stays dependency-free."
            ),
            help_line=(f"help: install the extra with `pip install edify[{framework}]` and retry."),
        )
        super().__init__(message)
        self.framework = framework
