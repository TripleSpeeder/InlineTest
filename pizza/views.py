from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import DeleteView, UpdateView, CreateView, DetailView, ListView, TemplateView
from pizza.models import Pizza
from pizza.forms import PizzaFormSet


class PizzaList(ListView):
    model = Pizza
    context_object_name = 'pizza_list'

class PizzaDetail(DetailView):
    context_object_name = 'pizza'
    model = Pizza

class PizzaCreate(TemplateView):
    template_name = 'pizza/pizza_form.html'
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates a blank version of the forms.
        """
        form = PizzaFormSet(instance = None)
        # Problem: This will just render 3 toppingUsages, but I can't create a new Pizza :-(
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = PizzaFormSet(data=self.request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class GenericPizzaCreate(CreateView):
    model = Pizza
    fields = ['name']

class PizzaUpdate(UpdateView):
    model = Pizza
    fields = ['name']

class PizzaDelete(DeleteView):
    model = Pizza
    context_object_name = 'pizza'
    success_url = reverse_lazy('pizza_list')
