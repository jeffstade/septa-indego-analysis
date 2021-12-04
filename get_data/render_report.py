#####
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/jeffstern/Documents/UPenn/Courses/MUSA-509/keys/musa509-lab09-46a0d7200e51.json'
#####

import geopandas as gpd
import pandas as pd
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from pipeline_tools import upload_to_gcs

template_root = 'templates'
output_root = 'output'

def main():
    # Download the map data.
    mapdata_df = pd.read_gbq("SELECT * FROM finalproj.combined_stations_fewer_buses")
    mapdata_df.the_geom = gpd.GeoSeries.from_wkt(mapdata_df.the_geom)
    mapdata_gdf = gpd.GeoDataFrame(mapdata_df, geometry='the_geom')
    textdata_df = pd.read_gbq("SELECT * FROM finalproj.counts")
    bike_station_count = textdata_df[textdata_df['Modal']=='Bike']['count'].item()
    subway_station_count = textdata_df[textdata_df['Modal']=='Subway']['count'].item()
    bus_station_count = textdata_df[textdata_df['Modal']=='Bus']['count'].item()
    indego_df = pd.read_gbq("SELECT * FROM musa509-lab09.finalproj.indego_stations")
    # mapdata_gdf[mapdatagdf['Modal'] == ]
    # Render the data into the template.
    env = Environment(loader=FileSystemLoader(template_root))
    template = env.get_template('index.html')
    output = template.render(
        mapdata=mapdata_gdf.to_json(),
        bike_station_count = bike_station_count,
        bus_station_count = bus_station_count,
        subway_station_count = subway_station_count
    )
    # Save the rendered output to a file in the "output" folder.
    print(output_root)
    with open(output_root + '/index.html', mode='w') as outfile:
        outfile.write(output)
   # upload_to_gcs('output/index.html', 'jawnt_philadelphia', 'index.html')


    template_station = env.get_template('station.html')
    for index, row in indego_df.iterrows():
        output_station = template_station.render(station_name = row.name, station_address = row.address, lon = row.lon, lat=row.lat)
        pagename = row.station_id + '.html'
        with open(output_root + '/' + pagename, mode='w+') as outfile:
            outfile.write(output_station)
            #upload_to_gcs(output_root'/'+pagename, 'jawnt_philadelphia', pagename)

if __name__ == '__main__':
    main()
