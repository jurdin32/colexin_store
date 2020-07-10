from django.urls import path

from . import views

urlpatterns = [
    path('search', views.ProductSearchListView.as_view(), name='search'),
    # path('<pk>', views.ProductDetailView.as_view(), name='product'),  # id -> llave primaaria
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product'), #id -> llave primaaria

]