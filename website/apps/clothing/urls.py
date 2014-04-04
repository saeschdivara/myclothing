from django.conf.urls import url
from django.conf.urls import patterns
from django.core.urlresolvers import reverse_lazy



urlpatterns = patterns('',

       # sent event
       url(r'^/',
           'clothing.views.show',
           name='show',
           ),

   )