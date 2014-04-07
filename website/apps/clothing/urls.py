from django.conf.urls import url, patterns, include



urlpatterns = patterns('',

       # sent event
       url(r'^',
           'clothing.views.show',
           name='show',
           ),

   )