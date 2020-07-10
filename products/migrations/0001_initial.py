# Generated by Django 2.2 on 2020-04-25 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Pais', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_producto', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.BooleanField(default=False)),
                ('image_a', models.ImageField(blank=True, help_text='100x100', null=True, upload_to='products/')),
                ('image_b', models.ImageField(blank=True, help_text='100x100', null=True, upload_to='products/')),
                ('descripcion', models.TextField(blank=True, max_length=500, null=True)),
                ('PROOF', models.BooleanField(default=False, help_text='Prueba')),
                ('MS', models.BooleanField(default=False, help_text='Flor De Cuño')),
                ('UNC', models.BooleanField(default=False, help_text='Sin Circula')),
                ('XF', models.BooleanField(default=False, help_text='Excelente Bien Conservada')),
                ('VF', models.BooleanField(default=False, help_text='Muy Bien Conservada')),
                ('F', models.BooleanField(default=False, help_text='Mas que Bien Conservada')),
                ('VG', models.BooleanField(default=False, help_text='Bien Conservada')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('anio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Pais.Anios')),
                ('ceca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Pais.Cecas')),
                ('motivo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Pais.Motivo')),
                ('tipo_producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Tipo_Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.BooleanField(default=False)),
                ('image_a', models.ImageField(blank=True, help_text='100x100', null=True, upload_to='products/')),
                ('image_b', models.ImageField(blank=True, help_text='100x100', null=True, upload_to='products/')),
                ('titulo', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.TextField(blank=True, max_length=500, null=True)),
                ('precio', models.IntegerField(blank=True, null=True)),
                ('precio_oferta', models.IntegerField(blank=True, null=True)),
                ('PROOF', models.BooleanField(default=False, help_text='Prueba')),
                ('MS', models.BooleanField(default=False, help_text='Flor De Cuño')),
                ('UNC', models.BooleanField(default=False, help_text='Sin Circula')),
                ('XF', models.BooleanField(default=False, help_text='Excelente Bien Conservada')),
                ('VF', models.BooleanField(default=False, help_text='Muy Bien Conservada')),
                ('F', models.BooleanField(default=False, help_text='Mas que Bien Conservada')),
                ('VG', models.BooleanField(default=False, help_text='Bien Conservada')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('anio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Pais.Anios')),
                ('ceca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Pais.Cecas')),
                ('denominacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Pais.Denominacion')),
                ('metal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Pais.Aleacion')),
                ('motivo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Pais.Motivo')),
            ],
        ),
        migrations.CreateModel(
            name='Billete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.BooleanField(default=False)),
                ('image_a', models.ImageField(blank=True, help_text='100x100', null=True, upload_to='products/')),
                ('image_b', models.ImageField(blank=True, help_text='100x100', null=True, upload_to='products/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('anio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Pais.Anios')),
                ('denominacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Pais.Denominacion')),
                ('tipo_producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Tipo_Producto')),
            ],
        ),
    ]
