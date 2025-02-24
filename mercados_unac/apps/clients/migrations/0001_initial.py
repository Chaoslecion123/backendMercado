# Generated by Django 3.0.6 on 2020-05-29 04:01

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
                'permissions': (('manage_client', 'Puede gestionar clientes'), ('export_client', 'Puede exportar clientes')),
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
