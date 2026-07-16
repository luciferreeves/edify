import re

class RegexValidator:
    regex: re.Pattern[str]
    message: str
    code: str
    def __init__(
        self,
        regex: str | None = ...,
        message: str | None = ...,
        code: str | None = ...,
        inverse_match: bool | None = ...,
        flags: int | None = ...,
    ) -> None: ...
    def __call__(self, value: object) -> None: ...
