from django.urls import path
from dashboard.views import Dashboard, GetSalesCustomers, GetSalesEmployees, GetSalesProducts, GetSalesStores, GetSumSalesCustomers, GetSumSales10Customers, GetSumSalesEmployees, GetSumSalesProducts, GetSumSalesStores, GetSales, IndexAPIView, getSaleErik, getSaleFrank, getSaleHelen, getSaleIngrid, getSaleJoan, getSaleLeif, getSaleLennart, getSaleRob, getSaleTom, singPath, worldPath, zoomable

urlpatterns = [
    path('', Dashboard, name='dashboard'),
    path('api/', IndexAPIView, name='api'),
    path('customers/', GetSalesCustomers, name='customers'),
    path('employees/', GetSalesEmployees, name='employees'),
    path('products/', GetSalesProducts, name='products'),
    path('stores/', GetSalesStores, name='stores'),
    path('topcustomers/', GetSumSalesCustomers, name='topcustomers'),
    path('top10customers/', GetSumSales10Customers, name='top10customers'),
    path('topemployees/', GetSumSalesEmployees, name='topemployees'),
    path('topproducts/', GetSumSalesProducts, name='topproducts'),
    path('topstores/', GetSumSalesStores, name='topstores'),
    path('overview/', GetSales, name='overview'),
    path('employees/getSaleErik', getSaleErik, name='Erik Presley'),
    path('employees/getSaleFrank', getSaleFrank, name='Frank Roll'),
    path('employees/getSaleHelen', getSaleHelen, name='Helen Brolin'),
    path('employees/getSaleIngrid', getSaleIngrid, name='Ingrid Hendrix'),
    path('employees/getSaleJoan', getSaleJoan, name='Joan Callins'),
    path('employees/getSaleLeif', getSaleLeif, name='Leif Shine'),
    path('employees/getSaleLennart', getSaleLennart, name='Lennart Skoglund'),
    path('employees/getSaleRob', getSaleRob, name='Rob Carsson'),
    path('employees/getSaleTom', getSaleTom, name='Tom Lindwall'),
    path('singpath', singPath, name='singPath'),
    path('worldpath', worldPath, name='worldPath'),
    path('zoomable', zoomable, name='zoomable'),
]
