from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index. 99932f26. Cheers!")
