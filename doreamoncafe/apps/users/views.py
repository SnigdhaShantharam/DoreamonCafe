import logging

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import DoreamonCafeUser
from .serializers import DoreamonCafeUserSerializers
from .utils import email_is_valid
from .validators import validate_indian_mobile_number


class RegistrationView(GenericAPIView):
    serializer_class = DoreamonCafeUserSerializers

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({'code': 400, 'msg': 'already logined'})
        request = request.data

        password = request.get('password')
        try:
            mobile_number = validate_indian_mobile_number(
                request.get('mobile_number'))

            user = DoreamonCafeUser.objects.create_user(
                mobile_number=mobile_number,
                password=password
            )
        except IntegrityError as e:
            logging.info(e)
            return Response({'code': 301, 'msg': 'mobile number exists'})
        except ValidationError as e:
            return Response({'code': e.code, 'msg': e.message})
        first_name = request.get('first_name')
        if first_name:
            user.first_name = first_name
        user.last_name = request.get('last_name')
        email_id = request.get('email')
        if email_is_valid(email_id):
            user.email = email_id
        user.address = request.get('address')
        user.save()

        return Response({'code': 201, 'msg': 'success'})
