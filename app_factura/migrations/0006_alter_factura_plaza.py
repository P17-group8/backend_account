# Generated by Django 3.2.9 on 2021-12-02 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_factura', '0005_auto_20211201_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='plaza',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='app_factura.plaza'),
        ),
    ]
