from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Role


class RegisterSerializer(serializers.Serializer):
    phone_number = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=150, required=True)
    role = serializers.CharField(max_length=150, required=True)
    password = serializers.CharField(max_length=4)

    def create(self, validated_data):
        name = validated_data['name']
        split_name = name.split(' ')
        first_name = split_name[0]
        last_name = split_name[1:].join(' ') if len(split_name) > 1 else ""
        create_user = User.objects.create_user(username=validated_data['phone_number'], password=validated_data['password'],
                                               first_name=first_name, last_name=last_name)
        role = validated_data['role']
        add_role = Role(user=create_user, role_name=role.lower())
        add_role.save()
        return create_user