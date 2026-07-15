"""Exception classes raised by the canonical :class:`Pattern` (de)serializer."""

from __future__ import annotations

from edify.errors.formatting import compose_annotated_message
from edify.errors.syntax import EdifySyntaxError
from edify.serialize.types import JSONValue


class MissingSchemaKeyError(EdifySyntaxError):
    """Raised when a canonical dict is missing a required top-level key.

    Args:
        missing_key: The name of the key that was not present.
    """

    def __init__(self, missing_key: str) -> None:
        message = compose_annotated_message(
            summary=f"canonical dict is missing the required {missing_key!r} key",
            trigger_hint="Pattern.from_dict / Pattern.from_json called here",
            note=(
                f"every canonical serialization must carry a top-level {missing_key!r} "
                "key; a document without it cannot be loaded."
            ),
            help_line=(
                f"help: add {missing_key!r} to the document, or regenerate the payload "
                "via ``pattern.to_dict()`` / ``pattern.to_json()``."
            ),
        )
        super().__init__(message)


class IncompatibleSchemaVersionError(EdifySyntaxError):
    """Raised when a canonical dict declares a schema version this build does not understand.

    Args:
        seen_version: The value found under the ``"edify"`` key.
        supported_version: The version this build emits and accepts.
    """

    def __init__(self, seen_version: JSONValue, supported_version: int) -> None:
        message = compose_annotated_message(
            summary=(
                f"canonical dict declares schema version {seen_version!r}, but this build "
                f"only understands {supported_version}"
            ),
            trigger_hint="Pattern.from_dict / Pattern.from_json called here",
            note=(
                "schema version 0 is experimental; regenerate the payload from the "
                "producing edify version, or upgrade this side to the version that emitted "
                "the payload."
            ),
            help_line=("help: check the ``edify`` key in the input matches the emitting build."),
        )
        super().__init__(message)


class UnknownElementKindError(EdifySyntaxError):
    """Raised when a nested dict declares a ``kind`` string not in the registry.

    Args:
        seen_kind: The ``"kind"`` value that could not be resolved.
    """

    def __init__(self, seen_kind: str) -> None:
        message = compose_annotated_message(
            summary=f"unknown element kind {seen_kind!r} in canonical dict",
            trigger_hint="Pattern.from_dict / Pattern.from_json called here",
            note=(
                f"the kind {seen_kind!r} is not registered; the payload likely "
                "originated from a newer edify build than the one loading it."
            ),
            help_line=(
                "help: upgrade edify on the loading side, or regenerate the payload from "
                "a build the loader recognises."
            ),
        )
        super().__init__(message)
