from django.conf.urls import url, patterns, include
from django.conf.urls.i18n import i18n_patterns

from rest_framework import viewsets, routers

from clothing.views import UserViewSet, GroupViewSet, ClothingTimeViewSet, ClothingViewSet, BodyPartsViewSet



# Routers provide an easy way of automatically determining the URL conf.
from website import settings

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'clothing-time', ClothingTimeViewSet)
router.register(r'clothing', ClothingViewSet)
router.register(r'body', BodyPartsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    url(r'^clothing/', include('clothing.urls', namespace='clothing')),
)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns += i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
)


###############################################################################################
###############################################################################################
# from django.conf import settings
# from django.conf.urls.defaults import patterns, include, url
# from django.conf.urls.i18n import i18n_patterns
#
# # Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
#
# urlpatterns = patterns('',
#     url(r'foo/', include('foo.urls', namespace='foo')),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
# )
#
# urlpatterns += i18n_patterns('',
#     url(r'^admin/', include(admin.site.urls)),
# )
#
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)