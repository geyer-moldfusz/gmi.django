from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^scooper/', include('gmi.django.scooper.urls', namespace='scooper')),
    url(r'^profile/', include('gmi.django.profile.urls', namespace='profile')),
    url(r'^admin/', include(admin.site.urls)),
]
