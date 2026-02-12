from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello this is the response!")


def about(request):
    return HttpResponse("This is the about page")

