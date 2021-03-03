from django.urls import path
from django.conf.urls import url

from restapi_crud_app import views

urlpatterns = [
    url(r'^sample$', views.sample.as_view(),name="sample"),
    url(r'^students$', views.studentsList.as_view(),name="students"),#for all objects of students table
    url('studentDetails/(?P<pk>\d+)/$', views.studentDetails.as_view(),name="studentDetails"), # specified (based on primary key ) object

    

]