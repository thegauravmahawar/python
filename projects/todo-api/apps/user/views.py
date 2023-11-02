from django.http import JsonResponse


def ok(request):
    return JsonResponse(
        {
            'status:': 'success',
            'data': 'ok'
        }
    )


def ping(request):
    return JsonResponse(
        {
            'status:': 'success',
            'data': 'pong!'
        }
    )
