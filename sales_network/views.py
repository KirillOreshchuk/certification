from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from sales_network.models import SalesNetworkObject, Contacts, Product
from users.permissions import IsActive
from sales_network.serializers import SalesNetworkObjectSerializer, SalesNetworkObjectUpdateSerializer, \
    ContactsSerializer, ProductSerializer


class SalesNetworkObjectListView(ListAPIView):
    """Отображение списка объетов сети"""
    queryset = SalesNetworkObject.objects.all()
    serializer_class = SalesNetworkObjectSerializer
    permission_classes = [IsActive]
    filter_backends = [SearchFilter]
    search_fields = ['contacts__country',]
    filterset_fields = ['contacts__country',]


class SalesNetworkObjectCreateView(CreateAPIView):
    """Создание объекта сети"""
    queryset = SalesNetworkObject.objects.all()
    serializer_class = SalesNetworkObjectSerializer
    permission_classes = [IsActive]

    def perform_create(self, serializer):
        """Функция привязывает пользователя к созданному им объекту сети"""
        new_object = serializer.save()
        new_object.user = self.request.user
        new_object.save()


class SalesNetworkObjectDetailView(RetrieveAPIView):
    """Отображение одного объекта сети"""
    queryset = SalesNetworkObject.objects.all()
    serializer_class = SalesNetworkObjectSerializer
    permission_classes = [IsActive]


class SalesNetworkObjectUpdateView(UpdateAPIView):
    """Изменение объекта сети"""
    queryset = SalesNetworkObject.objects.all()
    serializer_class = SalesNetworkObjectUpdateSerializer
    permission_classes = [IsActive]


class SalesNetworkObjectDeleteView(DestroyAPIView):
    """Удаление объекта сети"""
    queryset = SalesNetworkObject.objects.all()
    serializer_class = SalesNetworkObjectSerializer
    permission_classes = [IsActive]


class ContactsViewSet(ModelViewSet):
    """ViewSet контактов"""
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [IsActive]


class ProductViewSet(ModelViewSet):
    """ViewSet продуктов"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActive]
