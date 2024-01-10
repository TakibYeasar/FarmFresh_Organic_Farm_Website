from rest_framework import serializers
from .models import CustomUser, UserProfile


class RegisterSerializer(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'first_name', 'last_name', 'password', 'confirm_password']

    def validate(self, data):
        password = data['password']
        confirm_password = data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError(
                {'confirm_password': 'Password not matched!'})

        return data


class LoginSerializer(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'confirm_password']


class ForgetPasswordSerializer(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = ['email']


class ResetPasswordSerializer(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = ['password', 'confirm_password']

    def validate(self, data):
        password = data['password']
        confirm_password = data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError(
                {'confirm_password': 'Password not matched!'})

        return data


class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ['current_password', 'password', 'confirm_password']

    def validate(self, data):
        password = data['password']
        confirm_password = data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError(
                {'confirm_password': 'Password not matched!'})

        return data
