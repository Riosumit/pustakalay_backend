from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ['user']

    def create(self, validated_data):
        user = self.context['user']
        student = Student.objects.create(user=user, **validated_data)
        return student