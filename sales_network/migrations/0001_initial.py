# Generated by Django 5.0.4 on 2024-04-20 12:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_email', models.EmailField(max_length=254, verbose_name='Contact_email')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Страна')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='Город')),
                ('street', models.CharField(blank=True, max_length=50, null=True, verbose_name='Улица')),
                ('house_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Улица')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='Название продукта')),
                ('product_model', models.CharField(max_length=100, verbose_name='Модель продукта')),
                ('release_date', models.DateField(verbose_name='Дата выхода товара на рынок')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='SalesNetworkObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_name', models.CharField(max_length=100, verbose_name='Объект сети')),
                ('object_level', models.CharField(choices=[('0', 'Завод'), ('1', 'Розничная сеть'), ('2', 'Индивидуальный предприниматель')], max_length=30, verbose_name='Уровень объекта сети')),
                ('debt', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='Задолженность')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('contacts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales_network.contacts', verbose_name='Контакты')),
            ],
            options={
                'verbose_name': 'Объект сети продаж',
                'verbose_name_plural': 'Объекты сети продаж',
            },
        ),
    ]
