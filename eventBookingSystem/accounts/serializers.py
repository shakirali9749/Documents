from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .utils.image_utils import handle_base64_profile_image

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
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

class SigninSerializer(serializers.ModelSerializer):
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
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email,password=password)
        if not user:
            raise serializers.ValidationError('oops!: Invalid Email or Password')

        refresh = RefreshToken.for_user(user)
        data['access'] = str(refresh.access_token)
        data['refresh'] = str(refresh)
        print(f"Data: {data}")
        return data


class UserProfileSerializer(serializers.ModelSerializer):
    profile_image = serializers.CharField(write_only=True, required=False)
    profile_image_url = serializers.SerializerMethodField(read_only=True)

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
            'profile_image_url'
        ]
        read_only_fields = ['id','role','email']

    def get_profile_image_url(self, obj):
        request = self.context.get("request")
        if obj.profile_image:
            return request.build_absolute_uri(obj.profile_image.url)

        return None

    def update(self, instance, validated_data):
        base64_image = validated_data.pop("profile_image", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if base64_image:
            handle_base64_profile_image(instance, base64_image)

        instance.save()

        return instance



