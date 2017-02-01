from django.http import HttpResponse


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def test2(request, id):
    return HttpResponse('OK ' + id)
