#pip install geopandas
import geopandas as gpd

df = gpd.read_file("C:/Users/TUAN_ANH/Desktop/abc/app/data/singapore_shape_file_data/MP14_PLNG_AREA_NO_SEA_PL.shx")


df.to_file("output.json", driver="GeoJSON")