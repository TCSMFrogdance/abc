import pandas as pd

df = pd.read_csv('C:/Users/TUAN_ANH/Desktop/abc/app/data/data.csv')


#category - product
get_top_category = df[['Category', 'Sales']].copy()
get_top_category = get_top_category.groupby(['Category'])['Sales'].sum()


get_top_product = df[['Product', 'Sales']].copy()
get_top_product = get_top_product.groupby(['Product'])['Sales'].sum()


#customer
get_top_customer = df[['CustomerName', 'Sales']].copy()
get_top_customer = get_top_customer.groupby(['CustomerName'])['Sales'].sum()


get_top_country = df[['Country', 'Sales']].copy()
get_top_country = get_top_country.groupby(['Country'])['Sales'].sum()


get_foreigner_sales = df[['Foreigner', 'Sales']]
get_foreigner_sales = get_foreigner_sales.groupby(['Foreigner'])['Sales'].sum()


#employee
get_top_employee = df[['SalesPersonName', 'Sales']].copy()
get_top_employee = get_top_employee.groupby(['SalesPersonName'])['Sales'].sum()


#sales
get_sales_by_date = df[['SalesDate', 'Sales']].copy()
get_sales_by_date = get_sales_by_date.groupby(['SalesDate'])['Sales'].sum()


#store
get_top_store = df[['Store', 'Sales']].copy()
get_top_store = get_top_store.groupby(['Store'])['Sales'].sum()
