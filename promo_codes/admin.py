from django.contrib import admin

# Register your models here.
from .models import PromoCode

class PromoCodeAdmin(admin.ModelAdmin):
    exclude = ['code']

admin.site.register(PromoCode,PromoCodeAdmin)