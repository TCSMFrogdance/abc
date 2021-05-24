# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stores, Sales, Customers, Employees, Products
from .serializers import StoresSerializer, SalesSerializer, CustomersSerializer, EmployeesSerializer, ProductsSerializer
# Create your views here.


class GetAllStoresAPIView(APIView):
    def get(self, request):
        list_store = Stores.objects.all()
        mydata = StoresSerializer(list_store, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)

class GetAllSalesAPIView(APIView):
    def get(self, request):
        list_sale = Sales.objects.all()
        mydata = SalesSerializer(list_sale, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)

class GetAllCustomersAPIView(APIView):
    def get(self, request):
        list_customer = Customers.objects.all()
        mydata = CustomersSerializer(list_customer, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)

class GetAllEmployeesAPIView(APIView):
    def get(self, request):
        list_employee = Employees.objects.all()
        mydata = EmployeesSerializer(list_employee, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)

class GetAllProductsAPIView(APIView):
    def get(self, request):
        list_product = Products.objects.all()
        mydata = ProductsSerializer(list_product, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)