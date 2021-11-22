from django.shortcuts import HttpResponse

def index_view(request):
    return HttpResponse("hello world!")