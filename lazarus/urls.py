from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

from lazarus import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'lazarus.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload/', 'website.views.manage_upload', name='post_upload'),
    url(r'^$', 'website.views.home', name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

