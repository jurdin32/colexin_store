# Generated by Django 2.2 on 2020-05-17 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pais', '0002_auto_20200426_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='denominacion',
            name='orden',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
