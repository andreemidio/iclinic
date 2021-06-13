"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import authentication
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='IClinic Challenge',
        default_version='v1',
        description='API IClinic Challenge',
        terms_of_service='No terms',
        contact=openapi.Contact(email='andre.emidio@iclinic.com.br'),
        license=openapi.License(name='No License'),
    ),

    public=True,
    # authentication_classes=(authentication.BasicAuthentication,),
    authentication_classes=(authentication.TokenAuthentication,),
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', lambda request: redirect('docs/', permanent=True)),

    url(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
    url(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/v1/users/', include('apps.users.urls', namespace='users')),
    path('api/v1/prescriptions/', include('apps.prescriptions.urls', namespace='prescriptions')),
]
