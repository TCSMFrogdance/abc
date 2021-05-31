from django.urls import path
from dashboard.views import Dashboard, GetSalesCustomers, GetSalesEmployees, GetSalesProducts, GetSalesStores, GetSumSalesCustomers, GetSumSalesEmployees, GetSumSalesProducts, GetSumSalesStores, GetSumSales, IndexAPIView

urlpatterns = [
    path('', Dashboard, name='dashboard'),
    path('api/', IndexAPIView, name='api'),
    path('customers/', GetSalesCustomers, name='customers'),
    path('employees/', GetSalesEmployees, name='employees'),
    path('products/', GetSalesProducts, name='products'),
    path('stores/', GetSalesStores, name='stores'),
    path('topcustomers/', GetSumSalesCustomers, name='topcustomers'),
    path('topemployees/', GetSumSalesEmployees, name='topemployees'),
    path('topproducts/', GetSumSalesProducts, name='topproducts'),
    path('topstores/', GetSumSalesStores, name='topstores'),
    path('overview/', GetSumSales, name='overview'),
]