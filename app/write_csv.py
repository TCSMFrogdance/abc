import db

def csv(data):

    return data

csv(db.get_top_country).to_csv('top_country.csv')

csv(db.get_top_employee).to_csv('top_employee.csv')

#x = csv(db.get_top_store).to_frame()
#x['Region'] = db.df['Region', 'Store'].copy().groupby(['Store'])
#x['Latitude'] = db.df['Latitude', 'Store'].copy().groupby(['Store'])
#x['Longitude'] = db.df['Longitude', 'Store'].copy().groupby(['Store'])
#x.to_csv('top_store.csv')