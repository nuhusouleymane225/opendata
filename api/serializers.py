from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import update_last_login, User
from .models import Pharma
from rest_framework_jwt.settings import api_settings




class PharmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharma
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'passeword': {'write_only': True}}

        def create(self, validated_data):
            user = User(
                email=validated_data['eamil'],
                name =validated_data['name']
            )
            user.set_password(validated_data['password'])
            user.save()
            Token.objects.create(user=user)
            return user
            

        