# Generated by Django 2.2 on 2020-05-10 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20200508_0800'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moneda',
            old_name='offer',
            new_name='moneda_del_mes',
        ),
    ]
