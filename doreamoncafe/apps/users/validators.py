import re

from django.core.exceptions import ValidationError


def validate_indian_mobile_number(mobile_number):
    if re.findall('^[0-9]{10,10}$', str(mobile_number)):
        return mobile_number
    raise ValidationError('invalid mobile number')
