from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from restaurant_map.models import Restaurant, Comment
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(TemplateView):
    template_name = 'restaurant_map/index.html'

class MapView(LoginRequiredMixin,ListView):
    model = Restaurant
    login_url = '/common/login/'

class RestaurantDetail(DetailView):
    model = Restaurant