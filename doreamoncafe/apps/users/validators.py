import re

from django.core.exceptions import ValidationError
from django.core.validators import validate_email


def validate_indian_mobile_number(mobile_number):
    if re.findall('^[0-9]{10,10}$', str(mobile_number)):
        return mobile_number
    raise ValidationError(
        'invalid mobile number "{}"'.format(mobile_number), 301)


def validate_email_id(email):
    valid = validate_email(email)
    if valid and valid.get('code').lower == 'invalid':
        raise ValidationError('invalid email "{}"'.format(email), 301)
    return email
