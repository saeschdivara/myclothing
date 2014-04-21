from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from django.utils.translation import ugettext as _

from rest_framework import viewsets, routers

from clothing.models import ClothingTime
from clothing.serializers import ClothingTimeSerializer, UserSerializer, GroupSerializer


""" Normal views """
def show(request):
    return render(request, 'clothing/layouts/index.html', {

    })

""" REST API Views """
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ClothingTimeViewSet(viewsets.ModelViewSet):
    queryset = ClothingTime.objects.all()
    serializer_class = ClothingTimeSerializer