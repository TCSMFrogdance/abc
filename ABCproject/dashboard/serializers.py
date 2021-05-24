from .models import Stores, Sales, Customers, Employees, Products
from rest_framework import serializers

class StoresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stores
        fields = ('storeid', 'region', 'store', 'latitude', 'longtitude',)

class SalesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sales
        fields = ('id', 'salesdate', 'orderid', 'customerid', 'salespersonid', 'productid', 'quantity', 'sales', 'storeid',)

class CustomersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customers
        fields = ('customerid', 'country', 'customername', 'gender', 'phone', 'postalcode',)

class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employees
        fields = ('salespersonid', 'salespersonname', 'title',)

class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ('productid', 'category', 'product',)