from rest_framework import serializers
from vueOne.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','course','email','phone','address','profession']