from django.urls import path
from rest_framework import routers

from sales_network.views import (SalesNetworkObjectListView, SalesNetworkObjectDetailView,
                                 SalesNetworkObjectCreateView, SalesNetworkObjectUpdateView,
                                 SalesNetworkObjectDeleteView, ProductViewSet, ContactsViewSet)

urlpatterns = [
    path('sales_object/', SalesNetworkObjectListView.as_view(), name='sales_object_list'),
    path('sales_object/create/', SalesNetworkObjectCreateView.as_view(), name='ssales_object_create'),
    path('sales_object/<int:pk>/', SalesNetworkObjectDetailView.as_view(), name='sales_object_detail'),
    path('sales_object/update/<int:pk>/', SalesNetworkObjectUpdateView.as_view(), name='sales_object_update'),
    path('sales_object/delete/<int:pk>/', SalesNetworkObjectDeleteView.as_view(), name='sales_object_delete'),
]

router = routers.SimpleRouter()
router.register('product', ProductViewSet)
router.register('contacts', ContactsViewSet)

urlpatterns += router.urls
