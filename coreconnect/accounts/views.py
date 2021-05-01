from django.contrib.auth.models import User
from django.http import JsonResponse
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.db import IntegrityError


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
                })
            except IntegrityError:
                return JsonResponse({
                    "messagge": "Phone Number Already Taken"
                })
        else:
            return JsonResponse(serializer.errors)
