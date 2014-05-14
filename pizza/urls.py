from django.conf.urls import patterns, url

from pizza import views
from pizza.views import PizzaEdit, PizzaUpdate, PizzaDelete, PizzaDetail, PizzaList

urlpatterns = patterns('',

    url(r'^list/$', PizzaList.as_view(), name='pizza_list'),
    url(r'^add/$', PizzaEdit.as_view(), name='pizza_add'),
    url(r'^(?P<pk>\d+)/update/$', PizzaEdit.as_view(), name='pizza_update'),
    url(r'^(?P<pk>\d+)/delete/$', PizzaDelete.as_view(), name='pizza_delete'),
    url(r'^(?P<pk>\d+)/$', PizzaDetail.as_view(), name='pizza_detail'),
)
