from django.views import generic
from django.shortcuts import render

class HomeView(generic.TemplateView):
    template_name = 'home/main.html'

def home(request):
    return render(request, 'home/main.html')
