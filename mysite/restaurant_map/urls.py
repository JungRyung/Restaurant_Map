from django.urls import path

from . import views

app_name = 'restaurant_map'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('map/', views.MapView.as_view(), name='map'),
    path('restaurant_detail/<str:pk>/', views.RestaurantDetail.as_view(), name='restaurant_detail'),
]