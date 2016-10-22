from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from urlparse import urlparse

urlpatterns = [
    url(r'', include('apps.api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^avatar/', include('avatar.urls')),
    url(r'^admin/', admin.site.urls),
]


media_url = urlparse(settings.MEDIA_URL)
static_url = urlparse(settings.STATIC_URL)
urlpatterns += static(media_url.path, document_root=settings.MEDIA_ROOT)
urlpatterns += static(static_url.path, document_root=settings.STATIC_ROOT)
