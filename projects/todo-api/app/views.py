from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from .models import User


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def create(self, request, **kwargs):
        get_user_model().objects.create_user(**request.data)
        return JsonResponse(status=200, data={'status': 'success', 'data': 'ok'})

    def update(self, request, pk=None, **kwargs):
        print('POST')

    def retrieve(self, request, pk=None, **kwargs):
        print('GET')

    def list(self, request, **kwargs):
        print('LIST')

    def destroy(self, request, pk=None, **kwargs):
        print('DELETE')
