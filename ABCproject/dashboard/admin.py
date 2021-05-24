from django.contrib import admin
from .models import Stores, Customers, Sales, Products, Employees
# Register your models here.

class StoresAdmin(admin.ModelAdmin):
    list_display = ['storeid', 'store']
class CustomersAdmin(admin.ModelAdmin):
    list_display = ['customerid', 'customername']
class SalesAdmin(admin.ModelAdmin):
    list_display = ['id', 'orderid']
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['productid', 'product']
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['salespersonid', 'salespersonname']

admin.site.register(Stores, StoresAdmin)
admin.site.register(Customers, CustomersAdmin)
admin.site.register(Sales, SalesAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Employees, EmployeesAdmin)