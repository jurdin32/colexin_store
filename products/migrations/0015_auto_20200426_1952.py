# Generated by Django 2.2 on 2020-04-27 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_product_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tipo',
            field=models.CharField(choices=[('Moneda', 'Moneda'), ('Billete', 'Billete'), ('Medalla', 'Medalla')], default='Moneda', max_length=60),
        ),
    ]
