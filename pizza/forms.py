from django.forms.models import inlineformset_factory

# Define forms
from pizza.models import Pizza, ToppingUsage

PizzaFormSet = inlineformset_factory(Pizza, ToppingUsage)
