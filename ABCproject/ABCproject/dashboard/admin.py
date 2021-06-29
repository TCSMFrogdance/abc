from django.contrib import admin
from .models import Stores, Customers, Products, Employees,  Sales
# Register your models here.

class StoresAdmin(admin.ModelAdmin):
    list_display = ['storeid', 'store', 'region', 'latitude', 'longitude']
class CustomersAdmin(admin.ModelAdmin):
    list_display = ['customerid', 'customername', 'country', 'gender', 'phone', 'postalcode']
class SalesAdmin(admin.ModelAdmin):
    list_display = ['id', 'orderid', 'salesdate', 'customerid', 'salespersonid', 'productid', 'quantity', 'sales', 'storeid']
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['productid', 'product', 'category']
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['salespersonid', 'salespersonname', 'title']


admin.site.register(Stores, StoresAdmin)
admin.site.register(Customers, CustomersAdmin)
admin.site.register(Sales, SalesAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Employees, EmployeesAdmin)