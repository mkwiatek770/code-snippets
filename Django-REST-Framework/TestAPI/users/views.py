from rest_framework import viewsets
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all().order_by('-date_joined')


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
