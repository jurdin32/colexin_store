from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Product


class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')
    paginate_by = 2

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['menssage'] = 'Listado de productos'
        context['products']=context['product_list']

        return context

class ProductDetailView(DetailView): #id -> pk
    model = Product
    template_name = 'products/product.html'


    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)

        print(context)

        return context

class MonedaDetailView(DetailView): #id -> pk
    model = Product
    template_name = '../templates/moneda_detalle.html'


    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)

        print(context)

        return context


class ProductSearchListView(ListView):
    template_name = 'products/search.html'

    def get_queryset(self):
        #SELECT * FROM products Where title like %valor%
        return Product.objects.filter(title__icontains=self.query())

    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['count'] = context['product_list'].count()

        return context