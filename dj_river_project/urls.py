"""dj_river_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from dj_river_app import views

urlpatterns = [
    path('admin/', admin.site.urls), # path for django admin page
    path('sample/',views.Sample,name = " sample"), # trial function url
    path('approve_ticket/(?P<ticket_id>\d+)/(?P<next_state_id>\d+)/', views.approve_ticket, name='approve_ticket'), # django river
    path('', include("river_admin.urls")),
    # 
]

