from django.http import HttpResponse


def miss(request):
    return HttpResponse('404')


def load(request):
    pass
    return HttpResponse('Hello, you\'re here')


def download(request, file_id):
    i = 0
    if not file_id.isdigit():
        print('In:', file_id)
        return miss(request)
    return HttpResponse('Your request is %d.' % i)
