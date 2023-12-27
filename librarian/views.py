from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

# Create your views here.
class LibrarianLoginView(APIView):
    def post(self,request):
        email = request.data.get('email')
        password = request.data.get('password')
        if email and password:
            user = authenticate(request, username=email, password=password)
            if user:
                user = User.objects.get(username=email)
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    "success": True,
                    "message": "login successful",
                    "data": {
                        "token": token.key,
                        "name": user.first_name,
                        "email": user.username,
                    }
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "success": False,
                    "message": "Invalid credentials"
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                "success": False,
                "message": "Email and Password is required"
            }, status=status.HTTP_400_BAD_REQUEST)