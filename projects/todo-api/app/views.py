from django.http import JsonResponse, HttpResponse
from rest_framework.viewsets import ViewSet, ModelViewSet


class UserViewSet(ModelViewSet):

    def create(self, request, **kwargs):
        print('POST')
        return JsonResponse(status=200, data={'status': 'success', 'data': 'ok'})

    def update(self, request, pk=None, **kwargs):
        print('POST')

    def retrieve(self, request, pk=None, **kwargs):
        print('GET')

    def list(self, request, **kwargs):
        print('LIST')

    def destroy(self, request, pk=None, **kwargs):
        print('DELETE')
