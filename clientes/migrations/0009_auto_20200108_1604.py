# Generated by Django 2.1 on 2020-01-08 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0008_auto_20200108_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itensdopedido',
            name='produto',
        ),
        migrations.RemoveField(
            model_name='itensdopedido',
            name='venda',
        ),
        migrations.RemoveField(
            model_name='venda',
            name='pessoa',
        ),
        migrations.DeleteModel(
            name='ItensDoPedido',
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
        migrations.DeleteModel(
            name='Venda',
        ),
    ]
