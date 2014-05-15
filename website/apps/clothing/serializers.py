from django.contrib.auth.models import User, Group
from rest_framework import serializers

from clothing.models import ClothingTime, Clothing, BodyPart


class ClothingTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingTime
        fields = ('id', 'name', 'clothes', 'slug', 'image', )


class ClothingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothing
        fields = ('id', 'name', 'slug', 'image', )


class BodyPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyPart
        fields = ('id', 'name', )
        
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name',)