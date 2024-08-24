from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. 491418eb is the polls index.")