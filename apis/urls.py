from django.conf.urls import url, include, handler404
from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from django.urls import path

from apis_core.apis_entities.api_views import GetEntityGeneric

urlpatterns = [
    url(r'^apis/', include('apis_core.urls', namespace="apis")),
    url(r'^bibsonomy/', include('apis_bibsonomy.urls', namespace="bibsonomy")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^bibsonomy/', include('apis_bibsonomy.urls', namespace="bibsonomy")),
    path(r"entity/<int:pk>/", GetEntityGeneric.as_view(), name="GetEntityGenericRoot"),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('webpage.urls', namespace='webpage')),
]


handler404 = 'webpage.views.handler404'
