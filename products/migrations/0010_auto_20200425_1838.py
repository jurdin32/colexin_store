# Generated by Django 2.2 on 2020-04-25 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20200425_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pais',
            field=models.CharField(blank=True, max_length=90, null=True),
        ),
    ]
