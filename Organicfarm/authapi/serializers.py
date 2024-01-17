from rest_framework import serializers
from .models import CustomUser
from rest_framework import exceptions
import attrs


class RegisterSerializer(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'first_name',
                  'last_name', 'password', 'confirm_password']
    
    def validate(self, attrs):
        username = attrs.get('username')

        if not username.isalnum():
            raise exceptions.ValidationError(
                'username must contains letters as well')

        return attrs
    
    def validate(self, data):
        password = data.get('password', '')
        confirm_password = data.get('confirm_password', '')

        if password != confirm_password:
            raise serializers.ValidationError(
                {'confirm_password': 'Password not matched!'})

        return data

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
 


class LoginSerializer(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        
    

# class ForgetPasswordSerializer(serializers.Serializer):
#     class Meta:
#         model = CustomUser
#         fields = ['email']


# class ResetPasswordSerializer(serializers.Serializer):
#     class Meta:
#         model = CustomUser
#         fields = ['password', 'confirm_password']

#     def validate(self, data):
#         password = data['password']
#         confirm_password = data['confirm_password']

#         if password != confirm_password:
#             raise serializers.ValidationError(
#                 {'confirm_password': 'Password not matched!'})

#         return data


# class ChangePasswordSerializer(serializers.Serializer):
#     current_password = serializers.CharField(max_length=100)

#     class Meta:
#         model = CustomUser
#         fields = ['current_password', 'password', 'confirm_password']

#     def validate(self, data):
#         password = data['password']
#         confirm_password = data['confirm_password']

#         if password != confirm_password:
#             raise serializers.ValidationError(
#                 {'confirm_password': 'Password not matched!'})

#         return data
