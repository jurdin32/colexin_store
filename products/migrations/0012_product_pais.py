# Generated by Django 2.2 on 2020-04-25 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_remove_product_pais'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pais',
            field=models.CharField(blank=True, max_length=90, null=True),
        ),
    ]
