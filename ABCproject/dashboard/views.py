from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from .querry import select_tableName_sales, select_sum_sales_priority
# Create your views here.:
def Dashboard(request):
    return render(request, 'dashboard.html')

def GetSalesCustomers(request):
    context = select_tableName_sales('ABC.sqlite3', 'DATE(SalesDate), CustomerName, Sales', 'Customers', 'CustomerID')
    context = pd.DataFrame(context, columns=['Date', 'CustomerName', 'Sales']).to_json(orient='records')
    return HttpResponse(context)

def GetSalesEmployees(request):
    context = select_tableName_sales('ABC.sqlite3', 'DATE(SalesDate), SalesPersonName, Sales', 'Employees', 'SalesPersonID')
    context = pd.DataFrame(context, columns=['Date', 'SalesPersonName', 'Sales']).to_json(orient='records')
    return HttpResponse(context)

def GetSalesProducts(request):
    context = select_tableName_sales('ABC.sqlite3', 'DATE(SalesDate), Product, Category, Sales', 'Products', 'ProductID')
    context = pd.DataFrame(context, columns=['Date', 'Product', 'Category', 'Sales']).to_json(orient='records')
    return HttpResponse(context)

def GetSalesStores(request):
    context = select_tableName_sales('ABC.sqlite3', 'DATE(SalesDate), Store, Sales', 'Stores', 'StoreID')
    context = pd.DataFrame(context, columns=['Date', 'Store', 'Sales']).to_json(orient='records')
    return HttpResponse(context)

def GetSumSalesCustomers(request):
    context = select_sum_sales_priority('ABC.sqlite3', 'Customers', 'CustomerName', 'CustomerID')
    context = pd.DataFrame(context, columns=['CustomerName', 'Sales']).to_json(orient='records')
    return HttpResponse(context)

def GetSumSalesEmployees(request):
    context = select_sum_sales_priority('ABC.sqlite3', 'Employees', 'SalesPersonName', 'SalesPersonID')
    context = pd.DataFrame(context, columns=['SalesPersonName', 'Sales']).to_json(orient='records')
    return HttpResponse(context)

def GetSumSalesProducts(request):
    context = select_sum_sales_priority('ABC.sqlite3', 'Products', 'Product', 'ProductID')
    context = pd.DataFrame(context, columns=['Product', 'Sales']).to_json(orient='records')
    return HttpResponse(context)


def GetSumSalesStores(request):
    context = select_sum_sales_priority('ABC.sqlite3', 'Stores', 'Store', 'StoreID')
    context = pd.DataFrame(context, columns=['Store', 'Sales']).to_json(orient='records')
    return HttpResponse(context)

def GetSumSales(request):
    context = select_sum_sales_priority('ABC.sqlite3', 'Stores', 'SalesDate', 'StoreID')
    context = pd.DataFrame(context, columns=['SalesDate', 'Sales']).to_json(orient='records')
    return HttpResponse(context)

def IndexAPIView(request):
    return render(request, 'apiview.html')