from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render

# Create your views here.
from django.views.generic import DeleteView, UpdateView, CreateView, DetailView, ListView, TemplateView
from pizza.models import Pizza, Topping
from pizza.forms import PizzaForm, ToppingForm, ToppingUsageForm, ToppingUsageFormSet


class PizzaList(ListView):
    model = Pizza
    context_object_name = 'pizza_list'

class PizzaDetail(DetailView):
    context_object_name = 'pizza'
    model = Pizza

class PizzaEdit(TemplateView):
    template_name = 'pizza/pizza_form.html'

    def get_instance(self, *args, **kwargs):
        """
        In case we are editing an existing pizza there should be a primary key provided.
        Try to get that pizza, raise an error if not available.
        """
        self.pizza = None
        pk = self.kwargs.get('pk', None)
        if pk:
            try:
                self.pizza = Pizza.objects.get(pk=pk)
            except ObjectDoesNotExist:
                raise Http404("No %(verbose_name)s found matching the query" %
                              {'verbose_name': Pizza._meta.verbose_name})

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates a blank version of the forms.
        Should display:
         - Pizzaform to create a new pizza
         - Set of Toppingusages to specify the usage parameters of a topping
         - Possibility to create new topping on-the-fly
        """

        self.get_instance(args, kwargs)
        self.pizza_form = PizzaForm(instance = self.pizza)
        self.topping_usage_formset = ToppingUsageFormSet(instance=self.pizza)
        return self.render_to_response(self.get_context_data())

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
        self.get_instance(args, kwargs)
        self.pizza_form = PizzaForm(data=self.request.POST, instance=self.pizza)
        self.topping_usage_formset = ToppingUsageFormSet(data=self.request.POST, instance=self.pizza)
        if self.pizza_form.is_valid() and self.topping_usage_formset.is_valid():
            # save pizza
            self.pizza = self.pizza_form.save()
            # Set pizza instance for toppingusageset before saving it
            # This is only necessary for creating new pizza, but should not harm anyway...
            self.topping_usage_formset.instance = self.pizza
            # Save toppingusageset
            self.topping_usage_formset.save()
            # return pizza url
            return HttpResponseRedirect(self.pizza.get_absolute_url())
        else:
            return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PizzaEdit, self).get_context_data(**kwargs)
        # Add extra data
        context['pizza'] = self.pizza
        context['pizza_form'] = self.pizza_form
        context['topping_usage_formset'] = self.topping_usage_formset
        context['toppings'] = Topping.objects.all()
        return context

class GenericPizzaCreate(CreateView):
    model = Pizza
    fields = ['name']

class GenericPizzaUpdate(UpdateView):
    model = Pizza
    fields = ['name']

class PizzaDelete(DeleteView):
    model = Pizza
    context_object_name = 'pizza'
    success_url = reverse_lazy('pizza_list')
