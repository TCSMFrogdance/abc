import db

def csv(data):

    return data

csv(db.get_top_country).to_csv('top_country.csv')

csv(db.get_top_employee).to_csv('top_employee.csv')