from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .exceptions import UnhandledException
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):

    def create(self, request, **kwargs):
        try:
            user = get_user_model().objects.create_user(**request.data)
            return JsonResponse(
                status=200,
                data={
                    'status': 'success',
                    'data': {
                        'email': user.email,
                        'created_at': user.created_at
                    }
                }
            )
        except Exception as e:
            raise UnhandledException(str(e))

    def update(self, request, pk=None, **kwargs):
        print('POST')

    def retrieve(self, request, pk=None, **kwargs):
        print('GET')

    def list(self, request, **kwargs):
        print('LIST')

    def destroy(self, request, pk=None, **kwargs):
        print('DELETE')
