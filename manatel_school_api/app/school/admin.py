from django.contrib import admin

from app.school.models import School, Student


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass
