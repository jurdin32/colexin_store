
from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic import DetailView

from products.models import Product


class StoreListView(ListView):
    template_name = 'store.html'
    queryset = Product.objects.all().order_by('-id')

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['menssage'] = 'Listado de productos'
        # context['products']=context['product_list']

        return context

class ProductDetailView(DetailView): #id -> pk
    model = Product
    template_name = 'store/template/store.html'