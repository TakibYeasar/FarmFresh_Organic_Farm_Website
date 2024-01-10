from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('activate/<str:email_active_code>/',
         ActivateAccountView.as_view(), name='activate'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('forget-password/', ForgetPasswordView.as_view(), name='forget-password'),
    path('reset-password/<str:active_code>/',
         ResetPasswordView.as_view(), name='reset-password'),
    path('change-password/', ChangePasswordPage.as_view(), name='change-password'),
]
