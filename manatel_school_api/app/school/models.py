import shortuuid
from django.db import models


class School(models.Model):
    class Meta:
        db_table = 'school'
        verbose_name = 'school'
        verbose_name_plural = 'schools'
        app_label = 'school'
        ordering = ['id', ]

    name = models.TextField(verbose_name="School name")
    max_num_of_students = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    @property
    def number_of_students(self) -> int:
        return self.students.count()


def get_student_identifier():
    return shortuuid.uuid()[:19]


class Student(models.Model):
    class Meta:
        db_table = 'student'
        verbose_name = 'student'
        verbose_name_plural = 'students'
        app_label = 'school'
        ordering = ['id', ]

    first_name = models.TextField(verbose_name="Student first name")
    last_name = models.TextField(verbose_name="Student last name")
    student_identification = models.CharField(max_length=20, unique=True, editable=False,
                                              default=get_student_identifier)

    school = models.ForeignKey(
        School,
        models.CASCADE,
        related_name='students'
    )

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
