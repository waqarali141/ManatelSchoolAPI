from rest_framework.viewsets import ModelViewSet

from .filters import SchoolFilter, StudentFilter
from .models import School, Student
from .serializer import SchoolSerializer, StudentSerializer


class SchoolViewSet(ModelViewSet):
    serializer_class = SchoolSerializer
    filterset_class = SchoolFilter
    queryset = School.objects.all()
    ordering_fields = ('id', 'name', 'max_num_of_students')


class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    filterset_class = StudentFilter
    queryset = Student.objects.all()
    ordering_fields = ('id', 'first_name',)
