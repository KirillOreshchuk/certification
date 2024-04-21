from rest_framework import serializers

from sales_network.models import SalesNetworkObject, Contacts, Product


class SalesNetworkObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesNetworkObject
        fields = '__all__'


class SalesNetworkObjectUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesNetworkObject
        fields = '__all__'
        read_only_fields = ('debt',)


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
