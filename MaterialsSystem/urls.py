"""System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add emergency_management URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add emergency_management URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add emergency_management URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.static import serve
from django.urls import path, include, re_path
from MaterialsSystem.settings import MEDIA_ROOT

urlpatterns = [
    path('local_library/', include("local_library.urls", namespace="local_library")),
    path('home/', include("home.urls", namespace="home")),
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    path('', admin.site.urls),

]
