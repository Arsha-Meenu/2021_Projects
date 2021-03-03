from django.contrib.auth.models import User,Group
from rest_framework import serializers
from restapiapp.models import students

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = ['id','name','age','student_id']
        # fields = '__all__'
