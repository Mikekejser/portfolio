from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('site/<sitename>', views.site, name='site')
]
