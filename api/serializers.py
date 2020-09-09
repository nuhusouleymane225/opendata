from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from .models import Pharma
from rest_framework_jwt.settings import api_settings




class PharmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharma
        fields = '__all__'


