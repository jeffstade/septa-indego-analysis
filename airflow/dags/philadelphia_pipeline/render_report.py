import geopandas as gpd
import pandas as pd
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from pipeline_tools import upload_to_gcs

template_root = 'templates'
output_root = 'output'

def render_index(template, mapdata_gdf, counts):
    output = template.render(
        mapdata=mapdata_gdf.to_json(),
        counts = counts
    )
    # Save the rendered output to a file in the "output" folder.
    with open(output_root + '/index.html', mode='w') as outfile:
        outfile.write(output)
    upload_to_gcs('output/index.html', 'jawnt_philadelphia', 'index.html')

def render_station_pages(template, station_data):
    for index, row in station_data.iterrows():
        output_station = template.render(
            station_name = row['name'],
            station_address = row['address'],
            lon = row['lon'],
            lat=row['lat'])
        pagename = row.station_id + '.html'
        with open(output_root + '/' + pagename, mode='w+') as outfile:
            outfile.write(output_station)
            upload_to_gcs(output_root+ '/' + pagename, 'jawnt_philadelphia', pagename)

def main():
    # Download the map data.
    mapdata_df = pd.read_gbq("SELECT * FROM finalproj.combined_stations_fewer_buses WHERE Modal='Bike'")
    mapdata_df.the_geom = gpd.GeoSeries.from_wkt(mapdata_df.the_geom)
    mapdata_gdf = gpd.GeoDataFrame(mapdata_df, geometry='the_geom')
    textdata_df = pd.read_gbq("SELECT * FROM finalproj.counts")
    counts = {'bike': textdata_df[textdata_df['Modal']=='Bike']['count'].item(),
            'subway': textdata_df[textdata_df['Modal']=='Subway']['count'].item(),
            'bus': textdata_df[textdata_df['Modal']=='Bus']['count'].item() }
    indego_df = pd.read_gbq("SELECT * FROM musa509-lab09.finalproj.indego_stations")
    # mapdata_gdf[mapdatagdf['Modal'] == ]
    # Render the data into the template.
    env = Environment(loader=FileSystemLoader(template_root))

    render_index(env.get_template('index.html'), mapdata_gdf, counts)

    render_station_pages(env.get_template('station.html'), indego_df)

if __name__ == '__main__':
    main()
