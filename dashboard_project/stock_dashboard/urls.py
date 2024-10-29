from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_stock_data/', views.get_stock_data_view, name='get_stock_data'),
]