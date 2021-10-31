from rest_framework.serializers import ModelSerializer

from .models import DoreamonCafeUser


class DoreamonCafeUserSerializers(ModelSerializer):
    class Meta:
        model = DoreamonCafeUser()
        fields = ['first_name', 'last_name',
                  'mobile_number', 'email', 'password', 'address']
