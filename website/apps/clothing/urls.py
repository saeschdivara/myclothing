from django.conf.urls import url
from django.conf.urls import patterns
from django.core.urlresolvers import reverse_lazy

from clothing.views import ClothingTimeCRUDView



urlpatterns = patterns('',

       # sent event
       url(r'^/',
           'clothing.views.show',
           name='show',
           ),

       url(r'^crud/clothing-time/?$', ClothingTimeCRUDView.as_view(), name='my_crud_view'),

   )