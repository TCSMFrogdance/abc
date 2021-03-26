import db
import json

def convert(data):
    x = data.to_frame()
    x.reset_index(inplace=True)
    x = x.to_json(orient="records")
    x = json.loads(x)
    return json.dumps(x)

with open("C:/Users/TUAN_ANH/Desktop/abc/app/data/top_country.json", "w") as outfile:
    outfile.write(convert(db.get_top_country))

with open("C:/Users/TUAN_ANH/Desktop/abc/app/data/sales_by_date.json", "w") as outfile:
    outfile.write(convert(db.get_sales_by_date))

with open("C:/Users/TUAN_ANH/Desktop/abc/app/data/top_category.json", "w") as outfile:
    outfile.write(convert(db.get_top_category))

with open("C:/Users/TUAN_ANH/Desktop/abc/app/data/top_customer.json", "w") as outfile:
    outfile.write(convert(db.get_top_customer))

with open("C:/Users/TUAN_ANH/Desktop/abc/app/data/top_employee.json", "w") as outfile:
    outfile.write(convert(db.get_top_employee))

with open("C:/Users/TUAN_ANH/Desktop/abc/app/data/top_product.json", "w") as outfile:
    outfile.write(convert(db.get_top_product))

with open("C:/Users/TUAN_ANH/Desktop/abc/app/data/top_store.json", "w") as outfile:
    outfile.write(convert(db.get_top_store))