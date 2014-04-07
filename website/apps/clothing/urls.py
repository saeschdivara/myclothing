from django.conf.urls import url
from django.conf.urls import patterns
from django.core.urlresolvers import reverse_lazy

from clothing.views import ClothingTimeCRUDView, router
# 
from django.conf.urls import url, patterns, include
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers



urlpatterns = patterns('',

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

       # sent event
       url(r'^/',
           'clothing.views.show',
           name='show',
           ),

       url(r'^crud/clothing-time/?$', ClothingTimeCRUDView.as_view(), name='my_crud_view'),

   )