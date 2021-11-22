from django.shortcuts import HttpResponse, render

def index_view(request):
    # return HttpResponse("hello world!")
    return render(request, 'templates/index.html')