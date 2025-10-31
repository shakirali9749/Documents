from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'password',
            'role'
        ]

    def create(self,validated_data):
        role = validated_data.get('role', 'customer')
        user = User.objects.create_user(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            phone_number = validated_data['phone_number'],
            role = role,
            password = validated_data['password']

        )
        return user

class SigninSerializers(serializers.ModelSerializer):
    email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'access',
            'refresh'
        ]

    def validate(self, data):
        eamil = data.get('email'),
        password = data.get('password')
        user = authenticate(email=email,password=password)
        if not user:
            raise serializers.ValidationError('oops!: Invalid Email or Password')

        refresh = RefreshToken.for_user(user)
        data['access'] = str(refresh.access_token)
        data['refresh'] = str(refresh)
        return data


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'phone_number',
            'profile_image',
            'email',
            'role',
        ]
        read_only_fields = ['id','role','email']