from rest_framework import serializers
from .models import StudentsClass

class StudentClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsClass
        fields = '__all__'
        # fields = ('name','dateofjoining')
