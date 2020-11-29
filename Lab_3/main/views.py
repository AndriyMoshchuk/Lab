
from django.shortcuts import render
from django.http import JsonResponse
import os
from datetime import datetime


def main(request):
    return render(request, 'main.html', {'parameter': "test"})


def health(request):
    response = {
        'datetime': datetime.now().isoformat(),
        'server_url': request.build_absolute_uri(),
        'server_iinfo': {
            'system': os.name,
            'server_Login': os.getlogin(),
        },
        'client_info': {
            'user agent': request.headers['User-Agent'],
            'remote addr': request.META['REMOTE_ADDR'],
        }
    }
    return JsonResponse(response)