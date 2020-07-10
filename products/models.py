import uuid

from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

from django.utils.safestring import mark_safe

from Pais.models import *

itemTipo_Producto=['tipo_producto']
class Tipo_Producto(models.Model):
    tipo_producto=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return ' %s ' % ( self.tipo_producto)


itemProduct=['vista_previa','vista_previa2','stock','title','tipo_producto','tipo','pais','metal','offer','motivo','anio','descripcion','precio','PROOF','MS','UNC','XF','VF','F','VG','slug']
class Product(models.Model):
    offer = models.BooleanField(default=False)
    stock = models.BooleanField(default=True)
    tipo_producto = models.ForeignKey(Tipo_Producto, on_delete=models.CASCADE, null=True, blank=True)
    tipo=models.CharField(max_length=60 , choices=(('Moneda','Moneda'),('Billete','Billete'),('Medalla','Medalla')))
    title = models.CharField(max_length=50, null=True, blank=True)
    pais=models.ForeignKey(Pais,on_delete=models.CASCADE, null=True, blank=True)
    image_a = models.ImageField(upload_to='products/', null=True, blank=True, help_text='100x100')
    image_b = models.ImageField(upload_to='products/', null=True, blank=True, help_text='100x100')
    metal = models.ForeignKey(Aleacion, on_delete=models.CASCADE, null=True, blank=True)
    motivo = models.ForeignKey(Motivo, on_delete=models.CASCADE, null=True, blank=True)
    anio = models.ForeignKey(Anios, on_delete=models.CASCADE, null=True, blank=True)
    descripcion = models.TextField(max_length=500, null=True, blank=True)
    precio = models.IntegerField(null=True, blank=True)
    # precio_oferta = models.IntegerField(null=True, blank=True)

    PROOF = models.BooleanField(default=False, help_text='Prueba')
    MS = models.BooleanField(default=False, help_text='Flor De Cuño')
    UNC = models.BooleanField(default=False, help_text='Sin Circula')
    XF = models.BooleanField(default=False, help_text='Excelente Bien Conservada')
    VF = models.BooleanField(default=False, help_text='Muy Bien Conservada')
    F = models.BooleanField(default=False, help_text='Mas que Bien Conservada')
    VG = models.BooleanField(default=False, help_text='Bien Conservada')

    create_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=False, blank=True, unique=True)



    def __str__(self):
        return ' %s ' % ( self.title)


    def vista_previa(self):
        return mark_safe('<image width="100" height="100"  src="/media/%s">' % self.image_a)

    def vista_previa2(self):
        return mark_safe('<image width="100" height="100"  src="/media/%s">' % self.image_b)


def set_slug(sender, instance, *args, **kwargs): #callback
    if instance.title and not instance.slug:
        slug = slugify(instance.title)

        while Product.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.title, str(uuid.uuid4())[:8])
            )
        instance.slug = slug

pre_save.connect(set_slug, sender=Product)




itemMoneda=['vista_previa','vista_previa2','moneda_del_mes','create_at','titulo','denominacion','anio','ceca','motivo','metal','descripcion','PROOF','MS','UNC','XF','VF','F','VG']
class Moneda(models.Model):
    moneda_del_mes = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    image_a = models.ImageField(upload_to='products/', null=True, blank=True, help_text='100x100')
    image_b = models.ImageField(upload_to='products/', null=True, blank=True, help_text='100x100')
    titulo = models.CharField(max_length=50, null=True, blank=True)
    denominacion = models.ForeignKey(Denominacion, on_delete=models.CASCADE, null=True, blank=True)
    anio = models.ForeignKey(Anios, on_delete=models.CASCADE, null=True, blank=True)
    ceca = models.ForeignKey(Cecas, on_delete=models.CASCADE, null=True, blank=True)
    descripcion = models.TextField(max_length=500, null=True, blank=True)
    motivo = models.ForeignKey(Motivo, on_delete=models.CASCADE, null=True, blank=True)
    metal = models.ForeignKey(Aleacion, on_delete=models.CASCADE, null=True, blank=True)







    PROOF = models.IntegerField(null=True, blank=True, help_text='Prueba')
    MS = models.IntegerField(null=True, blank=True, help_text='Flor De Cuño')
    UNC = models.IntegerField(null=True, blank=True , help_text='Sin Circular   ')
    XF = models.IntegerField(null=True, blank=True, help_text='Excelente Bien Conservada')
    VF = models.IntegerField(null=True, blank=True, help_text='Muy Bien Conservada')
    F = models.IntegerField(null=True, blank=True , help_text='Mas que Bien Conservada')
    VG = models.IntegerField(null=True, blank=True, help_text='Bien Conservada')


    # slug = models.SlugField(null=False, blank=True, unique=True)

    # def set_slug(sender, instance, *args, **kwargs): #callback
    #     if instance.titulo and not instance.slug:
    #         slug = slugify(instance.titulo)
    #
    #         while Moneda.objects.titulo(slug=slug).exists():
    #             slug = slugify(
    #                 '{}-{}'.format(instance.titulo, str(uuid.uuid4())[:8])
    #             )
    #         instance.slug = slug
    #
    # pre_save.connect(set_slug, sender= Moneda)

    def __str__(self):
        return ' %s ' % ( self.titulo)


    def vista_previa(self):
        return mark_safe('<image width="100" height="100"  src="/media/%s">' % self.image_a)

    def vista_previa2(self):
        return mark_safe('<image width="100" height="100"  src="/media/%s">' % self.image_b)




itemBillete=['vista_previa','vista_previa2','offer','tipo_producto','denominacion','anio']
class Billete(models.Model):
    offer = models.BooleanField(default=False)
    tipo_producto= models.ForeignKey(Tipo_Producto, on_delete=models.CASCADE, null=True, blank=True)
    image_a = models.ImageField(upload_to='products/', null=True, blank=True, help_text='100x100')
    image_b = models.ImageField(upload_to='products/', null=True, blank=True, help_text='100x100')
    denominacion = models.ForeignKey(Denominacion, on_delete=models.CASCADE, null=True, blank=True)
    anio = models.ForeignKey(Anios, on_delete=models.CASCADE, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return ' %s ' % ( self.denominacion)


    def vista_previa(self):
        return mark_safe('<image width="125" height="50"  src="/media/%s">' % self.image_a)

    def vista_previa2(self):
        return mark_safe('<image width="125" height="50"  src="/media/%s">' % self.image_b)
