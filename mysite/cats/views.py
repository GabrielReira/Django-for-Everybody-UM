from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from cats.models import Cat, Breed


# Main Views

class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        mc = Breed.objects.all().count()
        al = Cat.objects.all()
        ctx = {'breed_count': mc, 'cat_list': al}

        return render(request, 'cats/cat_list.html', ctx)

class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        ml = Breed.objects.all()
        ctx = {'breed_list': ml}

        return render(request, 'cats/breed_list.html', ctx)


# Breed CRUD

class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')


# Cat CRUD

class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')
