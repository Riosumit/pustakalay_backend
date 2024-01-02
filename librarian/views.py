from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from student.serializers import Student, StudentSerializer
from .serializeres import Book, BookSerializer

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
        
class StudentView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            student = Student.objects.filter(pk=pk).first()
            if student:
                serializer = StudentSerializer(instance=student)
                return Response({
                    "success": True,
                    "message": "Student details",
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "success": False,
                    "message": "Student not found",
                    "data": None,
                }, status=status.HTTP_404_NOT_FOUND)
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(instance=students, many=True)
            return Response({
                "success": True,
                "message": "Student List",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

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

    def delete(self, request, pk=None):
        if pk:
            student = Student.objects.filter(pk=pk).first()
            if student:
                student.user.delete()
                return Response({
                    "success": True,
                    "message": "Student deleted successfully",
                    "data": None
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "success": False,
                    "message": "Student not found",
                    "data": None
                }, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({
                "success": False,
                "message": "PK is required",
                "data": None
            }, status=status.HTTP_400_BAD_REQUEST)
        
class BookView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            book = Book.objects.filter(pk=pk).first()
            if book:
                serializer = BookSerializer(instance=book)
                return Response({
                    "success": True,
                    "message": "Book details",
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "success": False,
                    "message": "Book not found",
                    "data": None,
                }, status=status.HTTP_404_NOT_FOUND)
        else:
            books = Book.objects.all()
            serializer = BookSerializer(instance=books, many=True)
            return Response({
                "success": True,
                "message": "Book List",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "message": "Book added successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        if pk:
            book = Book.objects.filter(pk=pk).first()
            if book:
                book.delete()
                return Response({
                    "success": True,
                    "message": "Book deleted successfully",
                    "data": None
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "success": False,
                    "message": "Book not found",
                    "data": None
                }, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({
                "success": False,
                "message": "PK is required",
                "data": None
            }, status=status.HTTP_400_BAD_REQUEST)