# Generated by Django 3.1.1 on 2020-09-26 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_pedidos', '0002_auto_20200926_0330'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='entregado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fotografia',
            field=models.ImageField(blank=True, null=True, upload_to='gestion_pedidos'),
        ),
    ]