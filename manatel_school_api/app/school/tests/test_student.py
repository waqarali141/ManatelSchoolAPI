from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app.school.factories import StudentFactory, SchoolFactory


class StudentListTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('student-list')

    def test_students_list(self):
        StudentFactory.create_batch(2)
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)


class StudentDetailTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.student = StudentFactory(first_name='waqar', last_name="ali")

    def test_student_detail(self):
        url = reverse('student-detail', kwargs={'pk': self.student.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'waqar')

    def test_student_error_detail(self):
        url = reverse('student-detail', kwargs={'pk': -1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['detail'], 'Not found.')


class StudentUpdateTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.student = StudentFactory(first_name='waqar', last_name="ali")
        cls.url = reverse('student-detail', kwargs={'pk': cls.student.id})

    def test_student_update(self):
        response = self.client.put(self.url, format='json', data={'first_name': 'updated_name',
                                                                  'last_name': 'ali',
                                                                  'school': self.student.school.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'updated_name')


class StudentDeleteTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.student = StudentFactory()

    def test_student_delete(self):
        url = reverse('student-detail', kwargs={'pk': self.student.id})
        response = self.client.delete(url, format='json', )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_student_error_delete(self):
        url = reverse('student-detail', kwargs={'pk': -1})
        response = self.client.delete(url, format='json', )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class StudentCreateTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('student-list')
        cls.school = SchoolFactory(max_num_of_students=1)

    def test_student_create(self):
        response = self.client.post(self.url, data={
            'first_name': 'waqar',
            'last_name': 'ali',
            'school': self.school.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['first_name'], 'waqar')

    def test_student_error_create(self):
        response = self.client.post(self.url, data={
            'first_name': 'new student',
            'last_name': 'ali',
            'school': self.school.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['first_name'], 'new student')
        error_response = self.client.post(self.url, data={
            'first_name': 'over flow student',
            'last_name': 'ali',
            'school': self.school.id
        })
        self.assertEqual(error_response.status_code, status.HTTP_400_BAD_REQUEST)
