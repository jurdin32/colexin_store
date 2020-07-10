from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe

itemAnios=['anio']
class Anios(models.Model):
    anio = models.IntegerField(null=True, blank=True, help_text='Año')

    def __str__(self):
        return '%s '%(self.anio)

    class Meta:
        verbose_name_plural = "1. Años"



itemContinente=['continente']
class Continente(models.Model):
    continente=models.CharField(max_length=90, null=True, blank=True)
    def __str__(self):
        return '%s '%(self.continente)



    class Meta:
        verbose_name_plural = "2. Continente"



itemPais=['continente','pais']
class Pais(models.Model):
    continente=models.ForeignKey(Continente,on_delete=models.CASCADE, null=True, blank=True)
    pais=models.CharField(max_length=90, null=True, blank=True)

    def __str__(self):
        return '%s | %s '%(self.continente,self.pais)


    class Meta:
        verbose_name_plural = "2. Pais"


itemMotivo=['motivo']
class Motivo(models.Model):
    motivo= models.CharField(max_length=90, null=True, blank=True)


    def __str__(self):
        return ' %s ' % ( self.motivo)

    class Meta:
        verbose_name_plural = "5. Motivo"


itemPeriodo=['pais','periodo','image_a','image_b','anio_inicio','anio_fin']
class Periodo(models.Model):
    pais=models.ForeignKey(Pais,on_delete=models.CASCADE, null=True, blank=True)
    periodo=models.CharField(max_length=90, null=True, blank=True)
    image_a = models.ImageField(upload_to='products/', null=True, blank=True, help_text='100x100')
    image_b = models.ImageField(upload_to='products/', null=True, blank=True, help_text='100x100')
    anio_inicio=models.CharField(max_length=90, null=True, blank=True)
    anio_fin=models.CharField(max_length=90, null=True, blank=True)

    def __str__(self):
        return '%s | %s | %s | %s '%(self.pais,self.periodo,self.anio_inicio,self.anio_fin)

    class Meta:
        verbose_name_plural = "3. Periodo"


itemCecas=['pais','ceca','marca_ceca']
class Cecas(models.Model):
    pais= models.ForeignKey(Pais,on_delete=models.CASCADE, null=True, blank=True)
    ceca = models.CharField(max_length=90, null=True, blank=True)
    marca_ceca= models.CharField(max_length=90, null=True, blank=True)

    def __str__(self):
        return '%s | %s | %s ' % (self.pais, self.ceca, self.marca_ceca,)

    class Meta:
        verbose_name_plural = "5. Ceca"


itemAleacion=['aleacion','detalle']
class Aleacion(models.Model):
    aleacion = models.CharField(max_length=20, null=True, blank=True)
    detalle = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return '%s | %s  ' % (self.aleacion, self.detalle)

    class Meta:
        verbose_name_plural = "6. Aleacion"




itemDeniminacion=['vista_previa','vista_previa2','periodo','km','orden','denominacion','motivo', 'metal','diametro', 'peso', 'grosor','canto', 'diseniador', 'anverso','inverso','nota']
class Denominacion(models.Model):
    orden = models.CharField(max_length=2, null=True, blank=True)
    periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE, null=True, blank=True)
    km = models.CharField(max_length=8, null=True, blank=True)
    denominacion = models.CharField(max_length=90, null=True, blank=True)
    image_a = models.ImageField(upload_to='products/', null=True, blank=True, help_text='100x100')
    image_b = models.ImageField(upload_to='products/', null=True, blank=True, help_text='100x100')

    motivo = models.ForeignKey(Motivo, on_delete=models.CASCADE, null=True, blank=True)
    metal = models.ForeignKey(Aleacion, on_delete=models.CASCADE, null=True, blank=True)
    diametro = models.CharField(max_length=90, blank=True, null=True)
    peso = models.CharField(max_length=10, null=True, blank=True)
    grosor = models.CharField(max_length=10, null=True, blank=True)
    canto = models.CharField(max_length=90, blank=True, null=True)
    diseniador = models.CharField(max_length=50, null=True, blank=True)
    anverso = models.CharField(max_length=90, blank=True, null=True)
    inverso = models.CharField(max_length=90, blank=True, null=True)
    nota = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return '%s | %s  ' % (self.periodo, self.denominacion)

    class Meta:
        verbose_name_plural = "6. Denominacion"

    def vista_previa(self):
        return mark_safe('<image width="100" height="100"  src="/media/%s">' % self.image_a)

    def vista_previa2(self):
        return mark_safe('<image width="100" height="100"  src="/media/%s">' % self.image_b)


itemDenimina_detalle = ['denominacion', 'motivo', 'metal','diametro', 'peso', 'grosor','canto', 'diseniador', 'anverso','inverso']
class Denimina_detalle(models.Model):
    denominacion = models.ForeignKey(Denominacion, on_delete=models.CASCADE, null=True, blank=True)
    motivo = models.ForeignKey(Motivo, on_delete=models.CASCADE, null=True, blank=True)
    metal = models.ForeignKey(Aleacion, on_delete=models.CASCADE, null=True, blank=True)
    diametro = models.CharField(max_length=90, blank=True, null=True)
    peso = models.CharField(max_length=10, null=True, blank=True)
    grosor = models.CharField(max_length=10, null=True, blank=True)
    canto = models.CharField(max_length=90, blank=True, null=True)
    diseniador = models.CharField(max_length=50, null=True, blank=True)
    anverso = models.CharField(max_length=90, blank=True, null=True)
    inverso = models.CharField(max_length=90, blank=True, null=True)

    def __str__(self):
        return '%s ' % (self.denominacion)

    class Meta:
        verbose_name_plural = "6. Denimina_detalle"


itemSistema_monetario=['periodo', 'denomina', 'anio','ceca','acunacion','PROOF','MS','UNC','XF','VF','F','VG','G','P']
class Sistema_monetario(models.Model):
    periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE, null=True, blank=True)
    denomina = models.ForeignKey(Denominacion,on_delete=models.CASCADE, null=True, blank=True)
    anio = models.ForeignKey(Anios, on_delete=models.CASCADE, null=True, blank=True)
    ceca = models.ForeignKey(Cecas, on_delete=models.CASCADE, null=True, blank=True)
    acunacion = models.IntegerField(null=True, blank=True)
    PROOF = models.IntegerField(null=True, blank=True, help_text='Prueba')
    MS = models.IntegerField(null=True, blank=True, help_text='Flor De Cuño')
    UNC = models.IntegerField(null=True, blank=True, help_text='Sin Circula')
    XF = models.IntegerField(null=True, blank=True, help_text='Excelente Bien Conservada')
    VF = models.IntegerField(null=True, blank=True, help_text='Muy Bien Conservada')
    F = models.IntegerField(null=True, blank=True, help_text='Mas que Bien Conservada')
    VG = models.IntegerField(null=True, blank=True, help_text='Bien Conservada')
    G = models.IntegerField(null=True, blank=True, help_text='Regular Conservación')
    P = models.IntegerField(null=True, blank=True, help_text='Mal Conservada')

    def __str__(self):
        return '%s | %s | %s '%(self.periodo,self.denomina,self.anio)

    class Meta:
        verbose_name_plural = "7. Sistema Monetario"



# itemTiraje=['periodo','anio','ceca','acunacion','PROOF','MS','UNC','XF','VF','F','VG','G','P']
# class Tiraje(models.Model):
#     periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE, null=True, blank=True)
#     anio = models.ForeignKey(Anios,on_delete=models.CASCADE, null=True, blank=True)
#     ceca = models.ForeignKey(Cecas,on_delete=models.CASCADE, null=True, blank=True)
#     acunacion= models.IntegerField(null=True, blank=True)
#     PROOF = models.IntegerField(null=True, blank=True, help_text='Prueba')
#     MS  = models.IntegerField(null=True, blank=True, help_text='Flor De Cuño')
#     UNC  = models.IntegerField(null=True, blank=True, help_text='Sin Circula')
#     XF  = models.IntegerField(null=True, blank=True, help_text='Excelente Bien Conservada')
#     VF  = models.IntegerField(null=True, blank=True, help_text='Muy Bien Conservada')
#     F  = models.IntegerField(null=True, blank=True, help_text='Mas que Bien Conservada')
#     VG  = models.IntegerField(null=True, blank=True, help_text='Bien Conservada')
#     G  = models.IntegerField(null=True, blank=True, help_text='Regular Conservación')
#     P = models.IntegerField(null=True, blank=True, help_text='Mal Conservada')
#
#     def __str__(self):
#         return '%s |%s '%(self.periodo, self.anio)
#
#     class Meta:
#         verbose_name_plural = "6. Tiraje"


