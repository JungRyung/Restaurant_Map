"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
import restaurant_map.views

## 첫 번째 인수는 일치시킬 경로, 두 번째 인수는 패턴이 일치할 때 호출되는 함수
urlpatterns = [
	path('polls/',include('polls.urls')),
	path('restaurant_map/',include('restaurant_map.urls')),
	path('', restaurant_map.views.index, name='index'),
    path('admin/', admin.site.urls),
    path('oauth/', restaurant_map.views.oauth, name='oauth'),
]