import logging

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import DoreamonCafeUser
from .serializers import DoreamonCafeUserSerializers


class RegistrationView(GenericAPIView):
    serializer_class = DoreamonCafeUserSerializers

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({'code': 400, 'msg': 'already logined'})
        request = request.data
        mobile_number = request.get('mobile_number')
        password = request.get('password')
        user_misc = {
            'first_name': request.get('first_name'),
            'last_name': request.get('last_name'),
            'email_id': request.get('email_id'),
            'address': request.get('address'),
        }

        user = DoreamonCafeUser.objects.create_user(
            mobile_number=mobile_number,
            password=password
        )
        for k, v in user_misc.items():
            setattr(user, k, v)

        user.save()

        return Response({'code': 201, 'msg': 'success'})
