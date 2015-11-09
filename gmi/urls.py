from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^scooper/', include('gmi.scooper.urls', namespace='gmi.scooper')),
    url(r'^admin/', include(admin.site.urls)),
]
