from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import DeleteView, UpdateView, CreateView, DetailView, ListView
from pizza.models import Pizza

class PizzaList(ListView):
    model = Pizza
    context_object_name = 'pizza_list'

class PizzaDetail(DetailView):
    context_object_name = 'pizza'
    model = Pizza

class PizzaCreate(CreateView):
    model = Pizza
    fields = ['name']

class PizzaUpdate(UpdateView):
    model = Pizza
    fields = ['name']

class PizzaDelete(DeleteView):
    model = Pizza
    context_object_name = 'pizza'
    success_url = reverse_lazy('pizza_list')
