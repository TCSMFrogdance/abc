import db

def csv(data):
    x = data.to_frame()
    x.reset_index(inplace=True)
    x.to_frame(index=False)
    return x

csv(db.get_top_country).to_csv('top_country.csv')