from django.urls import include, path
from rest_framework_nested import routers

from .views import SchoolViewSet, StudentViewSet

router = routers.SimpleRouter()
router.register("schools", SchoolViewSet, basename='school')
router.register("students", StudentViewSet, basename='student')

schools_router = routers.NestedSimpleRouter(router, 'schools', lookup='schools')
schools_router.register('students', StudentViewSet, basename='schools-students')

urlpatterns = [
    path("", include(router.urls)),
    path("", include(schools_router.urls)),
]
