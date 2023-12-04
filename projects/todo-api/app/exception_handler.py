from django.http import JsonResponse
from rest_framework.views import exception_handler


def app_exception_handler(exc, context):

    response = exception_handler(exc, context)
    print('Response: ', response)

    return JsonResponse(
            status=response.status_code,
            data={
                'status': 'error',
                'data': response.data['detail']
            }
        )
