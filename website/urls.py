from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.i18n import i18n_patterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
)

urlpatterns += i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
    
    # registration plugin
    # (r'^accounts/', include('registration.urls')),

    # clothing
    url(r'^clothing', include('clothing.urls', namespace='clothing')),

    # cms
    url(r'^', include('cms.urls')), # <--------- include the django cms urls via i18n_patterns
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)