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
    :param priority: string
    :param key: string
    """
    with connection.cursor() as cursor:
        cursor.execute("""SELECT {}, SUM(Sales) FROM Sales
                JOIN  {} ON Sales.{} = {}.{}
                GROUP BY {}""".format(priority, tableName, key, tableName, key, priority))
        rows = cursor.fetchall()
    return rows

