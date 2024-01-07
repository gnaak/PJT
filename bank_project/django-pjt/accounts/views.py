from dj_rest_auth.views import LoginView, UserDetailsView
from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer, CustomUserDetailsSerializer, CustomLoginSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import status
from .models import User
# from django.contrib.auth.hashers import check_password

class CustomLoginView(LoginView):
    serializer_class = CustomLoginSerializer

class CustomUserDetailsView(UserDetailsView):
    serializer_class = CustomUserDetailsSerializer

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer