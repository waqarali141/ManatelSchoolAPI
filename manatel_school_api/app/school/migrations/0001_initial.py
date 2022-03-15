# Generated by Django 4.0.3 on 2022-03-15 10:03

import app.school.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='School name')),
                ('max_num_of_students', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'school',
                'verbose_name_plural': 'schools',
                'db_table': 'school',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(verbose_name='Student first name')),
                ('last_name', models.TextField(verbose_name='Student last name')),
                ('student_identification', models.CharField(default=app.school.models.get_student_identifier, editable=False, max_length=20, unique=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='school.school')),
            ],
            options={
                'verbose_name': 'student',
                'verbose_name_plural': 'students',
                'db_table': 'student',
                'ordering': ['id'],
            },
        ),
    ]
