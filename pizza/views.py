from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import DeleteView, UpdateView, CreateView, DetailView, ListView, TemplateView
from pizza.models import Pizza
from pizza.forms import PizzaForm, ToppingForm, ToppingUsageForm, ToppingUsageFormSet


class PizzaList(ListView):
    model = Pizza
    context_object_name = 'pizza_list'

class PizzaDetail(DetailView):
    context_object_name = 'pizza'
    model = Pizza

class PizzaCreate(TemplateView):
    template_name = 'pizza/pizza_form.html'
    success_url = None

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates a blank version of the forms.
        Should display 3 parts:
         - Pizzaform to create a new pizza
         - [Toppingform to create a new Topping]
         - Set of Toppingusages to specify the usage parameters
        """
        pizza_form = PizzaForm(instance = None)
        topping_usage_formset = ToppingUsageFormSet(instance=None)
        return self.render_to_response(self.get_context_data(
            pizza_form=pizza_form,
            topping_usage_formset=topping_usage_formset
        ))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.

        Things to do:
        - Check if all forms are valid
        - Save the pizza
        [- Save the topping]
        - Set topping and pizza PK to ToppingUsage
        - Save toppingUsage
        """
        pizza_form = PizzaForm(data=self.request.POST)
        topping_usage_formset = ToppingUsageFormSet(data=self.request.POST)
        if pizza_form.is_valid() and topping_usage_formset.is_valid():
            # save pizza
            pizza = pizza_form.save()
            # Set pizza instance for toppingusageset before saving it
            topping_usage_formset.instance = pizza
            # Save toppingusageset
            topping_usage_formset.save()
            # return pizza url
            return HttpResponseRedirect(pizza.get_absolute_url())
        else:
            return self.render_to_response(self.get_context_data(
                pizza_form=pizza_form,
                topping_usage_formset=topping_usage_formset
            ))


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
