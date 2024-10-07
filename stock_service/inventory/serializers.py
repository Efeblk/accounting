from rest_framework import serializers
from .models import Product, Warehouse, Stock

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  # Nested serializer to show product details
    warehouse = WarehouseSerializer()  # Nested serializer to show warehouse details

    class Meta:
        model = Stock
        fields = '__all__'
