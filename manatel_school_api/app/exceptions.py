"""
Custom API exception handler
"""

from rest_framework.exceptions import APIException


class ValidationError(APIException):
    status_code = 400
    default_detail = 'Students can not be enrolled in this school.'
    default_code = 'bad_request'
