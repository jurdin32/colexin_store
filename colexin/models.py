from django.db import models

# Create your models here.

itemColexin=['nombre','logo_color','logo_blanco','logo_gris','logo_negro','favicon']
class Colexin(models.Model):
    nombre = models.CharField(max_length=100,null=True,blank=True)
    logo_color = models.ImageField(upload_to='colexin/',null=True, blank=True, help_text='100x100')
    logo_blanco = models.ImageField(upload_to='colexin/', null=True, blank=True, help_text='100x100')
    logo_gris = models.ImageField(upload_to='colexin/', null=True, blank=True, help_text='100x100')
    logo_negro = models.ImageField(upload_to='colexin/', null=True, blank=True, help_text='100x100')
    favicon = models.ImageField(upload_to='colexin/', null=True, blank=True, help_text='100x100')

    class Meta:
        verbose_name_plural = "1. Colexin"


itemContacto=['direccion','calle','mapa','representante','celular','telefono','correo']
class Contacto(models.Model):
    direccion=models.CharField(max_length=100,null=True,blank=True)
    calle=models.CharField(max_length=100,null=True,blank=True)
    mapa=models.TextField(max_length=500,null=True,blank=True)
    representante=models.CharField(max_length=100, null=True,blank=True)
    celular=models.CharField(max_length=11,null=True,blank=True)
    telefono=models.CharField(max_length=15,null=True,blank=True)
    correo=models.EmailField()

    class Meta:
        verbose_name_plural = "7. Contácto"

itemRedes=['facebook','instagram','twitter','youtube']
class Redes(models.Model):
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "8. Contácto Redes Sociales"