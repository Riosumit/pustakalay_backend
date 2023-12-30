from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from student.serializers import StudentSerializer

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
        
class StudentResistrationView(APIView):
    authentication_classes = [TokenAuthentication]
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get("email")
        password = request.data.get('password')
        if name and email and password:
            user = User.objects.create_user(username=email, email=email, first_name=name, password=password)
            serializer = StudentSerializer(data=request.data, context={'user':user})
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "success": True,
                    "message": "Registered successfully",
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)
            else:
                user.delete()
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                "success": False,
                "message": "Name, Email and Password are required"
            }, status=status.HTTP_400_BAD_REQUEST)