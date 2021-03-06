# Generated by Django 2.2 on 2020-05-10 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20200510_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moneda',
            name='F',
            field=models.IntegerField(blank=True, help_text='Mas que Bien Conservada', null=True),
        ),
        migrations.AlterField(
            model_name='moneda',
            name='MS',
            field=models.IntegerField(blank=True, help_text='Flor De Cuño', null=True),
        ),
        migrations.AlterField(
            model_name='moneda',
            name='PROOF',
            field=models.IntegerField(blank=True, help_text='Prueba', null=True),
        ),
        migrations.AlterField(
            model_name='moneda',
            name='UNC',
            field=models.IntegerField(blank=True, help_text='Sin Circula', null=True),
        ),
        migrations.AlterField(
            model_name='moneda',
            name='VF',
            field=models.IntegerField(blank=True, help_text='Muy Bien Conservada', null=True),
        ),
        migrations.AlterField(
            model_name='moneda',
            name='VG',
            field=models.IntegerField(blank=True, help_text='Bien Conservada', null=True),
        ),
        migrations.AlterField(
            model_name='moneda',
            name='XF',
            field=models.IntegerField(blank=True, help_text='Excelente Bien Conservada', null=True),
        ),
    ]
