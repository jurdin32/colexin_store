# Generated by Django 2.2 on 2020-04-28 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(default=1, max_length=100, unique=True),
        ),
    ]
