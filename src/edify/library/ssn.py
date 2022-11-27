import re

ssn_validate_pattern = "^(?!666|000|9\\d{2})\\d{3}-(?!00)\\d{2}-(?!0{4})\\d{4}$"


def ssn(ssn: str) -> bool:
    """Validate a Social Security Number (SSN).

    Args:
        ssn (str): The SSN to validate.

    Returns:
        bool: True if the SSN is valid, False otherwise.
    """
    if not isinstance(ssn, str):
        return False
    return bool(re.match(ssn_validate_pattern, ssn))
