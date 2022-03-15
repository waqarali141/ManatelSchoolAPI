import django_filters
from .models import School, Student


class StudentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='first_name', lookup_expr='icontains')

    class Meta:
        model = Student
        fields = {"school__name": ['icontains']}


class SchoolFilter(django_filters.FilterSet):

    class Meta:
        model = School
        fields = {"name": ['icontains']}
