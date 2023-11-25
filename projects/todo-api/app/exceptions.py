from rest_framework import status
from rest_framework.exceptions import APIException


class CustomException(APIException):
    detail = None
    status_code = None

    def __init__(self, detail, status_code):
        super().__init__(detail, status_code)
        self.detail = detail
        self.status_code = status_code


class NotFoundException(CustomException):
    def __init__(self, detail):
        super().__init__(detail, status.HTTP_404_NOT_FOUND)


class AlreadyExistException(CustomException):
    def __init__(self, detail):
        super().__init__(detail, status.HTTP_409_CONFLICT)


class UnAuthorizedException(CustomException):
    def __init__(self, detail):
        super().__init__(detail, status.HTTP_401_UNAUTHORIZED)


class InvalidRequestException(CustomException):
    def __init__(self, detail):
        super().__init__(detail, status.HTTP_400_BAD_REQUEST)


class UnhandledException(CustomException):
    def __init__(self, detail):
        super().__init__(detail, status.HTTP_500_INTERNAL_SERVER_ERROR)
