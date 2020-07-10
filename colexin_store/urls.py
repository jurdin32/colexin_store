from django.contrib import admin
from django.urls import path

from django.urls import include

from django.conf.urls.static import static
from django.conf import settings

from . import views

from products.views import ProductListView
from colexin.views import *
from .views import *

urlpatterns = [
    path('', index , name='index'),
    # path('', ProductListView.as_view(), name='index'),
    path('usuarios/login', views.login_view, name='login'),
    path('usuarios/logout', views.logout_view, name='logout'),
    path('usuarios/registro', views.register, name='register'),
    path('admin/', admin.site.urls),

    path('biblioteca/', biblioteca),
    path('biblioteca/<slug:pais>/', biblioteca_pais),
    path('biblioteca/<slug:pais>/<slug:periodo>',  biblioteca_pais_perido),

    path('usuario/', usuario),
    path('perfil/', perfil),
    path('moneda/<int:id>/', moneda_detalle),

    path('venta/', venta),



    path('blog/', blog),

    # path('blog/categoria/<int:n>/', blogfiltradocategoria),

    path('post/<int:n>/', post),
    path('periodo/',periodo),
    path('periodo/<int:id>/',periodo),
    path('periodo/<slug:slug>/',periodo),


    path('productos/', include('products.urls')),
    path('carrito/', include('carts.urls')),
    path('orden/', include('orders.urls')),
    path('direcciones/', include('shipping_addresses.urls')),
    path('codigos/',include('promo_codes.urls')),
    path('pagos/',include('billing_profiles.urls')),
    path('contacto/',contacto),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)