from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app.school.factories import SchoolFactory


class SchoolListTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('school-list')

    def test_students_list(self):
        SchoolFactory.create_batch(2)
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)


class SchoolDetailTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.school = SchoolFactory(name='bangkok school')

    def test_school_detail(self):
        url = reverse('school-detail', kwargs={'pk': self.school.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'bangkok school')

    def test_school_error_detail(self):
        url = reverse('school-detail', kwargs={'pk': -1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['detail'], 'Not found.')


class SchoolUpdateTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.school = SchoolFactory(name='test school')
        cls.url = reverse('school-detail', kwargs={'pk': cls.school.id})

    def test_school_update(self):
        response = self.client.put(self.url, format='json', data={'name': 'updated',
                                                                  'max_num_of_students': 10})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'updated')


class SchoolDeleteTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.school = SchoolFactory()

    def test_school_delete(self):
        url = reverse('school-detail', kwargs={'pk': self.school.id})
        response = self.client.delete(url, format='json', )
        self.assertEqual(response.status_code, 204)

    def test_student_error_delete(self):
        url = reverse('school-detail', kwargs={'pk': -1})
        response = self.client.delete(url, format='json', )
        self.assertEqual(response.status_code, 404)


class SchoolCreateTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('school-list')

    def test_student_create(self):
        response = self.client.post(self.url, data={
            'name': 'test school',
            'max_num_of_students': 10,
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'test school')
