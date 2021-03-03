from django.urls import path
from .views import (api_read,api_create,api_delete,api_update,api_all_delete)
from rest_framework.urlpatterns import format_suffix_patterns




urlpatterns = [
    path('student_create/',api_create, name='create') ,#post
    path('student_read/',api_read, name='read'),#get
    path('student_update/<int:pk>',api_update, name='update'), #put
    path('student_delete/<int:pk>',api_delete, name='delete'), #delete
    path('student_delete/',api_all_delete, name='all_delete'), #all delete


    
    

]

urlpatterns = format_suffix_patterns(urlpatterns)
