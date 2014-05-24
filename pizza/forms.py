from django.forms.models import modelform_factory, inlineformset_factory, ModelForm

# Define forms
from pizza.models import Pizza, Topping, ToppingUsage

# PizzaForm = modelform_factory(Pizza, fields=("name",))
ToppingForm = modelform_factory(Topping, fields=("name",))
ToppingUsageForm = modelform_factory(ToppingUsage, fields=("topping", "amount",))

ToppingUsageFormSet = inlineformset_factory(Pizza,ToppingUsage, extra=1)

class PizzaForm(ModelForm):
    class Meta:
        model = Pizza
        fields = ('name',)
