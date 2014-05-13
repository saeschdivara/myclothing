from django.contrib.auth.models import User, Group
from rest_framework import serializers

from clothing.models import ClothingTime, Clothing


class ClothingTimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClothingTime
        fields = ('name', 'clothes', 'slug', 'image', )


class ClothingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clothing
        fields = ('name', 'slug', 'image', )
        
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name',)