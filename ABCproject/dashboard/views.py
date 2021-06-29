from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from .querry import select_tableName_sales, select_sum_sales_priority, select_sum_sales_priority_list, get_sale, get_sale_employee
# Create your views here.:
def Dashboard(request):
    return render(request, 'dashboard.html')

def GetSales(request):
    context = get_sale('ABC.sqlite3')
    context = pd.DataFrame(context, columns=['year', 'month', 'Sales']).to_json(orient='records')
    return HttpResponse(context)

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

def GetSumSales10Customers(request):
    context = select_sum_sales_priority('ABC.sqlite3', 'Customers', 'CustomerName', 'CustomerID')
    context = pd.DataFrame(context, columns=['CustomerName', 'Sales']).nlargest(10, 'Sales').to_json(orient='records')
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
    context = select_sum_sales_priority_list('ABC.sqlite3', 'Stores', 'Store, Latitude, Longitude',  'Store', 'StoreID')
    context = pd.DataFrame(context, columns=['Store', 'Latitude', 'Longitude', 'Sales']).to_json(orient='records')
    return HttpResponse(context)


def IndexAPIView(request):
    return render(request, 'apiview.html')

def getSaleRob(request):
    context = get_sale_employee('ABC.sqlite3', 'Rob Carsson')
    context = pd.DataFrame(context, columns=['Store', 'Latitude', 'Longitude', 'Sales']).to_json(orient='records')
    return HttpResponse(context)

def getSaleTom(request):
    context = get_sale_employee('ABC.sqlite3', 'Tom Lindwall')
    context = pd.DataFrame(context, columns=['Store', 'Latitude', 'Longitude', 'Sales']).to_json(orient='records')
    return HttpResponse(context)

def getSaleFrank(request):
    context = get_sale_employee('ABC.sqlite3', 'Frank Roll')
    context = pd.DataFrame(context, columns=['Store', 'Latitude', 'Longitude', 'Sales']).to_json(orient='records')
    return HttpResponse(context)
    
def getSaleHelen(request):
    context = get_sale_employee('ABC.sqlite3', 'Helen Brolin')
    context = pd.DataFrame(context, columns=['Store', 'Latitude', 'Longitude', 'Sales']).to_json(orient='records')
    return HttpResponse(context)

def getSaleLeif(request):
    context = get_sale_employee('ABC.sqlite3', 'Leif Shine')
    context = pd.DataFrame(context, columns=['Store', 'Latitude', 'Longitude', 'Sales']).to_json(orient='records')
    return HttpResponse(context)

def getSaleLennart(request):
    context = get_sale_employee('ABC.sqlite3', 'Lennart Skoglund')
    context = pd.DataFrame(context, columns=['Store', 'Latitude', 'Longitude', 'Sales']).to_json(orient='records')
    return HttpResponse(context)
    
def getSaleJoan(request):
    context = get_sale_employee('ABC.sqlite3', 'Joan Callins')
    context = pd.DataFrame(context, columns=['Store', 'Latitude', 'Longitude', 'Sales']).to_json(orient='records')
    return HttpResponse(context)

def getSaleIngrid(request):
    context = get_sale_employee('ABC.sqlite3', 'Ingrid Hendrix')
    context = pd.DataFrame(context, columns=['Store', 'Latitude', 'Longitude', 'Sales']).to_json(orient='records')
    return HttpResponse(context)


def getSaleErik(request):
    context = get_sale_employee('ABC.sqlite3', 'Erik Presley')
    context = pd.DataFrame(context, columns=['Store', 'Latitude', 'Longitude', 'Sales']).to_json(orient='records')
    return HttpResponse(context)

def singPath(request):
    return HttpResponse(open('.\static\data\singapore.geojson', "r"))

def worldPath(request):
    return HttpResponse(open('.\static\data\world.geojson', "r"))

def zoomable(request):
    return HttpResponse(open('.\static\data\zoomable.json', "r"))