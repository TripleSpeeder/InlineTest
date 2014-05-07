from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import DeleteView, UpdateView, CreateView
from pizza.models import Pizza


def detail(request, pizza_id):
    return HttpResponse("You're looking at pizza %s." % pizza_id)

class PizzaCreate(CreateView):
    model = Pizza
    fields = ['name']

class PizzaUpdate(UpdateView):
    model = Pizza
    fields = ['name']

class PizzaDelete(DeleteView):
    model = Pizza
    success_url = reverse_lazy('author-list')