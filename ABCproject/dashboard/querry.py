from django.db import connection

def select_tableName_sales(self, querry, tableName, key):
    """
    Querry sales with key
    :param self: the db
    :param querry: string
    :param tableName: string
    :param key: string
    :return:
    """
    with connection.cursor() as cursor:
        cursor.execute("SELECT {} FROM Sales JOIN {} ON Sales.{} = {}.{}".format(querry, tableName, key, tableName, key))
        rows = cursor.fetchall()
    return rows

def select_sum_sales_priority(self, tableName, priority, key):
    """
    Qeurry sum sales with priority
    :param self: the db
    :param tableName: table name
    :param priority: string
    :param key: string
    """
    with connection.cursor() as cursor:
        cursor.execute("""SELECT {}, SUM(Sales) FROM Sales
                JOIN  {} ON Sales.{} = {}.{}
                GROUP BY {}""".format(priority, tableName, key, tableName, key, priority))
        rows = cursor.fetchall()
    return rows

def select_sum_sales_priority_list(self, tableName, query, priority, key):
    """
    Qeurry sum sales with priority
    :param self: the db
    :param tableName: table name
    :param query: list column
    :param priority: string
    :param key: string
    """
    with connection.cursor() as cursor:
        cursor.execute("""SELECT {}, SUM(Sales) FROM Sales
                JOIN  {} ON Sales.{} = {}.{}
                GROUP BY {}""".format(query, tableName, key, tableName, key, priority))
        rows = cursor.fetchall()
    return rows

def get_sale(self):
    with connection.cursor() as cursor:
        cursor.execute("""SELECT strftime('%Y', SalesDate) as year, strftime('%m', SalesDate) as month, SUM(Sales) FROM Sales
                GROUP BY strftime('%Y', SalesDate), strftime('%m', SalesDate)""")
        rows = cursor.fetchall()
    return rows

def get_sale_employee(self, name):
    with connection.cursor() as cursor:
        cursor.execute("""SELECT Store, Latitude, Longitude, SUM(Sales) FROM Sales
                    JOIN  Stores ON Sales.StoreID = Stores.StoreID JOIN Employees ON Sales.SalesPersonID = Employees.SalesPersonID
                    WHERE SalesPersonName = '{}'
                    GROUP BY Store""".format(name))
        rows = cursor.fetchall()
    return rows