from django.contrib import admin
from django.utils.html import format_html

from sales_network.models import Product, Contacts, SalesNetworkObject


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name')


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact_email', 'country', 'city', 'street', 'house_number')
    ordering = ('id',)


@admin.register(SalesNetworkObject)
class SalesNetworkObjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'object_name', 'object_level', 'get_supplier',]
    list_filter = ['contacts__city']
    actions = ('clear_debt',)

    @admin.action(description='Очистить задолжность')
    def clear_debt(self, _, queryset):
        queryset.update(debt=0.00)

    @admin.display(description="Поставщик")
    def get_supplier(self, obj):
        if obj.supplier is not None:
            return format_html("<a href='{url}'>{name}</a>", url=obj.supplier.id,
                               name=obj.supplier.object_name)
        return "-"
