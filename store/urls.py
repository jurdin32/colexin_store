from django.urls import path
from . import views
app_name = 'carts'

urlpatterns = [
    path('', views.StoreListView, name='store'),
    path('store', views.StoreListView, name='store'),
]