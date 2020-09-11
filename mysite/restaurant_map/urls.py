from django.urls import path

from . import views

app_name = 'restaurant_map'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('map/', views.MapView.as_view(), name='map'),
    path('comment/name<str:name>/', views.CommentList.as_view(), name='comment'),
]