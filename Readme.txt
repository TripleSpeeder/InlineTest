Random notes:

InlineFormSet can modify all ToppingUsages belonging to a certain Pizza. But you can not edit the Pizza itself.
The Pizza needs to be provided with "instance=..." attribute.

Todo:
-> Dynamically add/remove toppingusages while creating a pizza (using javascript to modify formset management form)
-> Make it possible to directly create a new topping while creating a pizza (using typeahead or http://brianreavis.github.io/selectize.js/)
-> Use django-widget-tweaks to render the forms with boostrap instead of django-bootstrap3 as it does not work nice with formsets.