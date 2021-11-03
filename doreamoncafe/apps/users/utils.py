from django.core.exceptions import ValidationError

from .validators import validate_email_id


def email_is_valid(email):
    try:
        validate_email_id(email)
    except ValidationError:
        return False
    return True
