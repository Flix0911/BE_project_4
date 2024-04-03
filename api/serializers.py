# get our auth User model
from django.contrib.auth.models import User
# serializers
from rest_framework import serializers
# import models for Plate and Cup
from .models import Plate, Cup

# create serializer to convert python object to json
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # This is built into django
        model = User
        # what we want to serialize ~ if valid go to create function
        fields = ["id", "username", "password"]
        # tells django to accept password, but don't return it
        # No one can read it
        extra_kwargs = {"password": {"write_only": True}}
        
        # create function
    def create(self, validated_data):
        print(validated_data)
        # implement method that will be called to created the new user
        user = User.objects.create_user(**validated_data)
        return user

# Plate serializer
class PlateSerializer(serializers.ModelSerializer):
    class Meta:
        # Plate model
        model = Plate
        fields = ["id", "title", "size", "owner"]
        # Can read who the author is, but can't write it
        extra_kwargs = {"owner": {"read_only": True}}
        
# Cup serializer
class CupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cup
        fields = ["id", "title", "size", "owner"]
        extra_kwargs = {"owner": {"read_only": True}}