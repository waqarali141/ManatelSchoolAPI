import factory
from .models import School, Student


class SchoolFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = School

    max_num_of_students = 5


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student

    school = factory.SubFactory(SchoolFactory)
