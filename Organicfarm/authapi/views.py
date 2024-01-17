from rest_framework.views import APIView
from .models import CustomUser
from .serializers import *
from .utils import send_email
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from django.utils.crypto import get_random_string
from django.contrib.auth import logout


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = CustomUser.objects.get(email=serializer.data['email'])
        send_email("Activate your account...", user.email, {
                   "user": user}, "emails/activate_account.html")
        return Response({"message": "User created successfully"}, status=201)


class ActivateAccountView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, email_active_code):
        user = CustomUser.objects.filter(
            email_active_code=email_active_code).first()
        if user and not user.is_active:
            user.is_active = True
            user.email_active_code = get_random_string(length=72)
            user.save()
            return Response({"message": "Account activated successfully"}, status=200)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        request.user.auth_token.delete()
        return Response({"message": "Logged out successfully"}, status=200)


# class ForgetPasswordView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         serializer = ForgetPasswordSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         send_email("Enter your email...", user.email, {
#                    "user": user}, "emails/forget_password.html")
#         return Response({"message": "Email sent for password reset"}, status=200)


# class ResetPasswordView(APIView):
#     permission_classes = [IsAuthenticated]

#     def put(self, request, active_code):
#         user = CustomUser.objects.filter(email_active_code=active_code)
#         serializer = ResetPasswordSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user.set_password(serializer.validated_data['password'])
#         user.email_active_code = get_random_string(72)
#         user.is_active = True
#         user.save()
#         return Response({"message": "Password reset successfully"}, status=200)


# class ChangePasswordPage(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         serializer = ChangePasswordSerializer(request.data)
#         if serializer.is_valid():
#             current_user = request.user
#             current_password = serializer.cleaned_data.get("current_password")
#             is_correct_password = current_user.check_password(current_password)

#             if is_correct_password:
#                 new_password = serializer.cleaned_data.get("password")
#                 current_user.set_password(new_password)
#                 current_user.save()
#                 logout(request)
#                 return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)
#             else:
#                 return Response({"error": "Incorrect current password"}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
