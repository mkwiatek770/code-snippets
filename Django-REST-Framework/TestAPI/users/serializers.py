from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'url', 'username', 'email', 'groups',)


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'url', 'name')