from django.shortcuts import HttpResponse, HttpResponseRedirect, render

# Create your views here.


def index(request):
    return HttpResponse("Hello, World!; How are you?")
