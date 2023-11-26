from django.contrib.auth import get_user_model
from rest_framework import serializers
from app.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password']
        extra_kwargs = {'password': {'writeOnly': True, 'min_length': 5}}


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'email'
