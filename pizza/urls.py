from django.conf.urls import patterns, url

from pizza import views
from pizza.views import PizzaCreate, PizzaUpdate, PizzaDelete

urlpatterns = patterns('',
    url(r'^(?P<pizza_id>\d+)/$', views.detail, name='detail'),

    url(r'pizza/add/$', PizzaCreate.as_view(), name='pizza_add'),
    url(r'pizza/(?P<pk>\d+)/$', PizzaUpdate.as_view(), name='pizza_update'),
    url(r'pizza/(?P<pk>\d+)/delete/$', PizzaDelete.as_view(), name='pizza_delete'),
)
