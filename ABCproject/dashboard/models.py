from django.db import models

# Create your models here.
class Customers(models.Model):
    customerid = models.TextField(db_column='CustomerID', primary_key=True)  # Field name made lowercase. This field type is a guess.
    country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    customername = models.CharField(db_column='CustomerName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customers'

    def __str__(self):
        return self.customername

class Employees(models.Model):
    salespersonid = models.TextField(db_column='SalesPersonID', primary_key=True)  # Field name made lowercase. This field type is a guess.
    salespersonname = models.TextField(db_column='SalesPersonName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    title = models.CharField(db_column='Title', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employees'
    
    def __str__(self):
        return self.salespersonname


class Products(models.Model):
    productid = models.TextField(db_column='ProductID', primary_key=True)  # Field name made lowercase. This field type is a guess.
    category = models.TextField(db_column='Category', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    product = models.CharField(db_column='Product', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'products'
    def __str__(self):
        return self.product


class Stores(models.Model):
    storeid = models.TextField(db_column='StoreID', primary_key=True)  # Field name made lowercase. This field type is a guess.
    region = models.TextField(db_column='Region', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    store = models.CharField(db_column='Store', max_length=20, blank=True, null=True)  # Field name made lowercase.
    latitude = models.TextField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    longitude = models.TextField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'stores'
    
    def __str__(self):
        return self.store

class Sales(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    salesdate = models.DateTimeField(db_column='SalesDate', blank=True, null=True)  # Field name made lowercase.
    orderid = models.SmallIntegerField(db_column='OrderID')  # Field name made lowercase.
    customerid = models.ForeignKey(Customers, models.DO_NOTHING, db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    salespersonid = models.TextField(db_column='SalesPersonID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    productid = models.ForeignKey(Products, models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    quantity = models.TextField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sales = models.TextField(db_column='Sales', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    storeid = models.ForeignKey('Stores', models.DO_NOTHING, db_column='StoreID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sales'

    def __str__(self):
        return self.orderid
