# coding:utf-8
from itertools import product

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

from django.http import HttpResponseRedirect

# from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView

from Pais.models import Pais, Periodo
from products.models import Product, Billete, Moneda
from users.models import User, Profile

from .forms import RegisterForm
from colexin.models import Contacto, Colexin, Redes
from Pais.models import *
from Blogs.models import *
from Blogs.templatetags import contador


def blog_paginado(request):
    list = Blogs.objects.all().order_by("-fecha_publicacion")
    paginator = Paginator(list,10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        blogss = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogss = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blogss = paginator.page(paginator.num_pages)
    return blogss


def index(request):
    contexto={
        'colexin': Colexin.objects.all().first(),
        'pais': Pais.objects.all(),
        'periodo': Periodo.objects.all(),
        'contacto':Contacto.objects.all().first(),
        'products':Product.objects.all(),
        'billetes': Billete.objects.all(),
        'monedas': Moneda.objects.all(),
        'blogs': Blogs.objects.all(),

    }
    return render_to_response('../templates/index.html', contexto)


def usuario(request):
    contexto={
        'colexin': Colexin.objects.all().first(),
        'pais': Pais.objects.all(),
        'periodo': Periodo.objects.all(),
        'contacto':Contacto.objects.all().first(),
        'product':Product.objects.all(),
        'billetes': Billete.objects.all(),
        'monedas': Moneda.objects.all(),


    }
    return render_to_response('../templates/about.html', contexto)


def perfil(request):
    contexto={
        'colexin': Colexin.objects.all().first(),
        'pais': Pais.objects.all(),
        'periodo': Periodo.objects.all(),
        'contacto':Contacto.objects.all().first(),
        'product':Product.objects.all(),
        'billetes': Billete.objects.all(),
        'monedas': Moneda.objects.all(),
        'perfiles':User.objects.all(),
    }
    return render_to_response('../templates/perfil.html', contexto)

def biblioteca(request):
    sistema = Sistema_monetario.objects.all()
    contexto={
        'contine': Continente.objects.all(),
        'pa': Pais.objects.all().order_by('continente'),
        'peri': Periodo.objects.all(),

        'colexin': Colexin.objects.all().first(),
        'contacto':Contacto.objects.all().first(),
        'product':Product.objects.all(),
        'sistema': sistema,

    }
    return render_to_response('../templates/biblioteca.html', contexto)


def biblioteca_pais(request,pais):
    contexto = {
        'contine': Continente.objects.all(),
        'pa': Pais.objects.all().order_by('continente'),
        'peri': Periodo.objects.all(),

        'periodo': Periodo.objects.filter(pais__pais=pais),
        'denominacion': Denominacion.objects.filter(periodo__periodo=periodo),
        'colexin': Colexin.objects.all().first(),
        'contacto': Contacto.objects.all().first(),
    }

    return render_to_response('../templates/biblioteca_pais.html', contexto)

def biblioteca_pais_perido(request,pais,periodo):
    contexto={
        'contine': Continente.objects.all(),
        'pa': Pais.objects.all().order_by('continente'),
        'peri': Periodo.objects.all(),

        'periodo' : Periodo.objects.get(periodo=periodo),
        'denominacion': Denominacion.objects.filter(periodo__periodo=periodo),
        'colexin': Colexin.objects.all().first(),
        'contacto':Contacto.objects.all().first(),
    }
    return render_to_response('../templates/biblioteca_periodo.html', contexto)


def venta(request):
    # sistema = Sistema_monetario.objects.all()
    contexto={
        'continente':Continente.objects.all(),
        'pais': Pais.objects.all().order_by('continente'),
        'periodo': Periodo.objects.all(),
        'colexin': Colexin.objects.all().first(),
        'contacto':Contacto.objects.all().first(),
        'monedas': Moneda.objects.all(),
        'products': Product.objects.all(),
        # 'sistema': sistema,


    }
    return render_to_response('../templates/venta.html', contexto)



# def moneda_detalle(request,id):
#     moneda=Moneda.objects.get(id=id)
#     # sistema=Sistema_monetario.objects.filter(periodo=moneda.periodo)
#     contexto={
#         'pais': Pais.objects.all().order_by('continente'),
#         'colexin': Colexin.objects.all().first(),
#         'contacto':Contacto.objects.all().first(),
#         'monedas':moneda,
#         # 'produ': Product.objects.all(),
#         # 'sistema':sistema,
#         'anioo':Anios.objects.all(),
#
#     }
#     return render_to_response('../templates/moneda_detalle.html', contexto)


def product(request):
    # sistema = Sistema_monetario.objects.all()
    contexto={
        'continente':Continente.objects.all(),
        'pais': Pais.objects.all().order_by('continente'),
        'periodo': Periodo.objects.all(),
        'colexin': Colexin.objects.all().first(),
        'contacto':Contacto.objects.all().first(),
        'producto': Product.objects.all(),
        # 'sistema': sistema,

    }
    return render_to_response('../templates/venta.html', contexto)

def pais(request,pais):
    periodo=Periodo.objects.get(id=id)
    sistema = Sistema_monetario.objects.filter(denomina__periodo=periodo)
    contexto = {
        'pais': Pais.objects.filter(pais=pais),
        'perio': Periodo.objects.filter(periodo=periodo),
        'denominacion':Denominacion.objects.filter(periodo=periodo),
        'sistema': sistema,
        # 'sistema': Sistema_monetario.objects.filter(periodo=)

    }
    return render_to_response('../templates/periodo.html',contexto)



def periodo(request,id):
    periodo=Periodo.objects.get(id=id)
    sistema = Sistema_monetario.objects.filter(denomina__periodo=periodo)
    contexto = {
        'pais': Pais.objects.all().order_by('continente'),
        'perio': Periodo.objects.filter(periodo=periodo),
        # 'colexin': Colexin.objects.all().first(),
        # 'contacto': Contacto.objects.all().first(),
        'denominacion':Denominacion.objects.filter(periodo=periodo),
        'sistema': sistema,
        # 'sistema': Sistema_monetario.objects.filter(periodo=)

    }
    return render_to_response('../templates/periodo.html',contexto)

# def produc_detalle(request,id):
#     moneda=Product.objects.get(id=id)
#     sistema=Sistema_monetario.objects.filter(periodo=moneda.periodo)
#     contexto={
#         'product':moneda,
#         'produ': Product.objects.all(),
#         'sistema':sistema,
#         'anioo':Anios.objects.all(),
#
#     }
#     return render_to_response('../templates/product_detail.html', contexto)





# def biblioteca_filtro(request,n):
#     # moneda = Product.objects.get(periodo__pais=n)
#     contexto={
#         'pais': Pais.objects.all().order_by('continente'),
#         'periodo': Periodo.objects.filter(pais=n),
#         'denominacion':Denominacion.objects.all(),
#         'colexin': Colexin.objects.all().first(),
#         'contacto':Contacto.objects.all().first(),
#         'product':Product.objects.all(),
#         'sistema':Sistema_monetario.objects.all(),
#         # 'prod': moneda,
#     }
#     return render_to_response('../templates/biblioteca_clasificacion.html', contexto)


def produc_detalle(request,id):
    moneda=Product.objects.get(id=id)
    sistema=Sistema_monetario.objects.filter(periodo=moneda.periodo)
    contexto={
        'pais': Pais.objects.all().order_by('continente'),
        'colexin': Colexin.objects.all().first(),
        'contacto':Contacto.objects.all().first(),
        'product':moneda,
        'produ': Product.objects.all(),
        'sistema':sistema,
        'anioo':Anios.objects.all(),

    }
    return render_to_response('../templates/product_detail.html', contexto)



def moneda_detalle(request,id):
    moneda=Moneda.objects.get(id=id)
    # sistema=Sistema_monetario.objects.filter(periodo=moneda.periodo)
    contexto={
        'pais': Pais.objects.all().order_by('continente'),
        'colexin': Colexin.objects.all().first(),
        'contacto':Contacto.objects.all().first(),
        'moneda':moneda,
        # 'sistema':sistema,
        'anioo':Anios.objects.all(),
    }
    return render_to_response('../templates/moneda_detalle.html', contexto)



class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['menssage'] = 'Listado de productos'
        context['products']=context['product_list']

        return context

class ProductDetailView(DetailView): #id -> pk
    model = Product
    template_name = 'products/product.html'


# def index(request):
#     contexto ={
#         'products':Product.objects.all().first(),
#         'colexin':Colexin.objects.all(),
#
#     }
#     return redirect('index.html', contexto)
#

# def index(request):
#     products = Product.objects.all().order_by('-id')
#
#     return render(request,'index.html',{
#         'message': 'Listado de Productos',
#         'title': 'Productos',
#         'products': products,
#     })


def blog(request):
    contexto = {
        'blog': blog_paginado(request),
        'visitas': Visitas_Blog.objects.all(),
        'blogs': Blogs.objects.all(),
        'categorias': Categoria.objects.all(),
        'paginas': "x" * blog_paginado(request).paginator.num_pages,
    }

    return render_to_response("../templates/blog-medium-image.html", contexto)


# def blogfiltradocategoria(request, n):
#     cat = Categoria.objects.get(id=n)
#     blogg = Blogs.objects.filter(categoria=cat)
#     categorias = Categoria.objects.all()
#
#     return render_to_response("../templates/blog-medium-image.html",
#                               {"blogs": blogg,
#                                "categorias": cat,
#                                "cats": categorias,
#
#                                })


def post(request, n):
    try:
        Visitas_Blog(blog_id=n).save()
    except:
        visita = Visitas_Blog.objects.get(blog_id=n)
        visita.save()
    contexto={
        'blogg':  Blogs.objects.get(id=n),
        'blog':  Blogs.objects.all(),

    }
    return render_to_response("../templates/blog-post.html", contexto)


def contacto(request):

    contexto={
        'colexin': Colexin.objects.all().first(),
        'contacto': Contacto.objects.all().first(),
        'redes': Redes.objects.all().first(),
    }
    return render_to_response('../templates/contacto.html', contexto)


# def buscar_blog(request):
#     if request.POST:
#         categorias = Categoria.objects.all()
#         context = {
#             "blogs": blog,
#             "categorias": categorias,
#             "cats": categorias,
#             'blogs': Blogs.objects.filter(titulo__icontains=request.POST['parametro']) or Blogs.objects.filter(
#                 articulo__icontains=request.POST['parametro']),
#             # "contacto_empresa": Contacto_empresa.objects.all().first(),
#             # "redes": Redes_sociales.objects.all().first(),
#         }
#         return render_to_response("../templates/blog-medium-image.html", context)
#     else:
#         return HttpResponseRedirect("/blog/?page=1")





def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username') #diccionario
        password = request.POST.get('password') #None

        user = authenticate(username=username, password=password)# None
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))

            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET['next'])

            return redirect('index')
        else:
            messages.error(request, 'Usuario o Contraseña no validas')

    return render(request, 'users/login.html', {

    })


def logout_view(request):
    # if request.user.is_authenticated:
    #     return redirect('index')
    logout(request)
    messages.success(request,'Sesión cerrada exitosamente')
    return redirect('login')


def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():

        user = form.save()
        if user:
            login(request, user)
            messages.success(request,'Usuario creado exitosamente')
            return redirect('index')


    if request.user.is_authenticated:
        return redirect('index')


    return render(request, 'users/register.html',{
        'form': form
    })

