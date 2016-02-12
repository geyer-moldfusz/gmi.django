from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('gmi.crewsite.urls', namespace='crewsite')),
    url(r'^scooper/', include('gmi.django.scooper.urls', namespace='scooper')),
    url(r'^profile/', include('gmi.django.profile.urls', namespace='profile')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^blog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),
]
