from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from django.utils.translation import ugettext as _

from clothing.models import ClothingTime



""" Normal views """
def show(request):
    return render(request, 'clothing/layouts/index.html', {

    })

""" REST API Views """
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    model = User

class GroupViewSet(viewsets.ModelViewSet):
    model = Group


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


""" AngularJS views """
from djangular.views.crud import NgCRUDView

class ClothingTimeCRUDView(NgCRUDView):
    model = ClothingTime