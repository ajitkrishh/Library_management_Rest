from dataclasses import field
from rest_framework.authtoken.views import Token
from .models import Book, CustomUser
from rest_framework import serializers

from django.contrib.auth import get_user_model


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"



class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','email', 'password' , 'first_name' , 'UserType')

        extra_kwargs = {'password': {
            "write_only": True,
            "required": True
        },
            "email": {
            "required": True
        }
        }
    
    def create(self, validated_data):
        user = get_user_model().objects.create(**validated_data)
        print(validated_data)
        user.set_password(validated_data['password'])
        Token.objects.create(user = user)
        user.save()
        return user

    # def update(self, instance, validated_data):
    #     print(validated_data)
    #     user = get_user_model().objects.update(**validated_data)
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user

class ChangeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','first_name','email', 'password',"UserType")

