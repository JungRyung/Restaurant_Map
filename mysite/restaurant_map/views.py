from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from restaurant_map.models import RestaurantList

class IndexView(TemplateView):
    template_name = 'restaurant_map/index.html'

class MapView(TemplateView):
    template_name = 'restaurant_map/map.html'
    res_list = RestaurantList.objects
    context = {'res_list':res_list}
    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = '공유'
        return context