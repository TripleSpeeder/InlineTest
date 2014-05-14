Random notes:

InlineFormSet can modify all ToppingUsages belonging to a certain Pizza. But you can not edit the Pizza itself.
The Pizza needs to be provided with "instance=..." attribute.

Todo:
-> Edit existing pizzas
-> Dynamically add/remove toppingusages while creating a pizza (using javascript to modify formset management form)
-> Make it possible to directly create a new topping while creating a pizza (also requires javascript)
