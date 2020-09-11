from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from restaurant_map.models import Restaurant, Comment

class IndexView(TemplateView):
    template_name = 'restaurant_map/index.html'

class MapView(ListView):
    model = Restaurant

class CommentList(ListView):
    model = Comment