from rest_framework.serializers import ModelSerializer

from app.exceptions import ValidationError
from .models import School, Student


class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = ("id", "name", "max_num_of_students", "number_of_students")
        read_only_fields = ("id", "number_of_students")


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ("id", "first_name", "last_name", "student_identification", "school")
        read_only_fields = ("id", "student_identification")

    def create(self, validated_data):

        # Validate if school has reached maximum number of students
        if validated_data['school'].number_of_students < validated_data['school'].max_num_of_students:
            return super().create(validated_data)
        raise ValidationError()
