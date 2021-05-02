from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from .serializers import RegisterSerializer, LoginSerializer, JwtSerializer
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from django.db import IntegrityError
from .models import Role
import datetime
import jwt


class RegisterView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request):
        generated_password = User.objects.make_random_password()[:4]
        request.data['password'] = generated_password
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                serializer.create(serializer.data)
                return JsonResponse({
                    "phone_number": serializer.data['phone_number'],
                    "password": serializer.data['password'],
                    "name": serializer.data['name'],
                    "role": serializer.data['role']
                }, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return JsonResponse({
                    "error": "Phone Number Already Taken"
                }, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.data['phone_number'],
                                password=serializer.data['password'])
            if user is not None and user.is_authenticated:
                key = "efish-test"
                phone_number = user.username
                name = user.first_name + user.last_name
                role = Role.objects.get(id=user.id)
                timestamp = datetime.datetime.utcnow()
                encoded = jwt.encode({"phone_number": phone_number,
                                      "name": name,
                                      "role": role.role_name,
                                      "exp": timestamp + datetime.timedelta(seconds=60)},
                                     key, algorithm="HS256")
                return JsonResponse({
                    "jwt": encoded
                }, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse({
                    "message": "Invalid Phone Number/Password"
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JwtView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = JwtSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            key = "efish-test"
            try:
                decode_jwt = jwt.decode(serializer.data['jwt'], key, algorithms="HS256")
                return JsonResponse(decode_jwt, status=status.HTTP_200_OK)
            except jwt.ExpiredSignatureError:
                return JsonResponse({
                    "message": "jwt expired"
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return JsonResponse(serializer.errors)
