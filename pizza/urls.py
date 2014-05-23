from django.conf.urls import patterns, url, include
from tastypie.api import Api
from pizza.views import PizzaEdit, PizzaDelete, PizzaDetail, PizzaList, PizzaAngular
from pizza.api import PizzaResource

v1_api = Api(api_name='v1')
v1_api.register(PizzaResource())


urlpatterns = patterns('',

    url(r'^list/$', PizzaList.as_view(), name='pizza_list'),
    url(r'^add/$', PizzaEdit.as_view(), name='pizza_add'),
    url(r'^(?P<pk>\d+)/update/$', PizzaEdit.as_view(), name='pizza_update'),
    url(r'^(?P<pk>\d+)/delete/$', PizzaDelete.as_view(), name='pizza_delete'),
    url(r'^(?P<pk>\d+)/$', PizzaDetail.as_view(), name='pizza_detail'),

    (r'^api/', include(v1_api.urls)),

    url(r'^angular/$', PizzaAngular.as_view(), name='pizza_angular'),
)
