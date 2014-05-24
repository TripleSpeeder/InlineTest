# myapp/api.py
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from pizza.models import Pizza, Topping


class PizzaResource(ModelResource):
    class Meta:
        queryset = Pizza.objects.all()
        resource_name = 'pizza'
        authorization = Authorization()
        always_return_data = True         # required for angular?

