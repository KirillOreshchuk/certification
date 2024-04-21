from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Contacts(models.Model):
    """Модель контактов"""

    contact_email = models.EmailField(verbose_name='Contact_email')
    country = models.CharField(max_length=50, **NULLABLE, verbose_name='Страна')
    city = models.CharField(max_length=50, **NULLABLE, verbose_name='Город')
    street = models.CharField(max_length=50, **NULLABLE, verbose_name='Улица')
    house_number = models.CharField(max_length=50, **NULLABLE, verbose_name='Улица')

    def __str__(self):
        return (f'Email: {self.contact_email}, country: {self.country}, city: {self.city},'
                f' street: {self.street}, house number: {self.house_number}')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Product(models.Model):
    """Модель продукта"""

    product_name = models.CharField(max_length=100, verbose_name='Название продукта')
    product_model = models.CharField(max_length=100, verbose_name='Модель продукта')
    release_date = models.DateField(verbose_name='Дата выхода товара на рынок')

    def __str__(self):
        return f'Продукт: {self.product_name} модель: {self.product_model} дата выхода: {self.release_date}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class SalesNetworkObject(models.Model):
    """Модель объета сети продаж"""

    LEVEL_CHOICES = (
        ('0', 'Завод'),
        ('1', 'Розничная сеть'),
        ('2', 'Индивидуальный предприниматель'),
    )

    object_name = models.CharField(max_length=100, verbose_name='Объект сети')
    object_level = models.CharField(max_length=30, choices=LEVEL_CHOICES, verbose_name='Уровень объекта сети')
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE, verbose_name='Контакты')
    products = models.ManyToManyField('Product', blank=True, verbose_name='Продукты')
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Поставщик')
    debt = models.DecimalField(max_digits=50, decimal_places=2, **NULLABLE, verbose_name='Задолженность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='Владелец')

    def __str__(self):
        return f'{self.object_name}'

    class Meta:
        verbose_name = 'Объект сети продаж'
        verbose_name_plural = 'Объекты сети продаж'
