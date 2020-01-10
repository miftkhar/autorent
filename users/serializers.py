from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('first_name', 'last_name', 'username', 'street_address', 'address2',
        'country','city','state', 'zipcode')
        #fields = '__all__'
