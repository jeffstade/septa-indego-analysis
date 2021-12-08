import geopandas as gpd
import pandas as pd
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from pipeline_tools import upload_to_gcs
import json

output_root = Path(__file__).parent.parent / 'output'
template_root = Path(__file__).parent.parent / 'templates'

def render_index(template, mapdata_gdf, counts):
    output = template.render(
        mapdata=mapdata_gdf.to_json(),
        counts = counts
    )

    index_location = str(output_root) + '/index.html'
    # Save the rendered output to a file in the "output" folder.
    with open(index_location, mode='w+') as outfile:
        outfile.write(output)
    upload_to_gcs(index_location, 'jawnt_philadelphia', 'index.html')

def render_station_pages(template, station_data):
    for index, row in station_data.iterrows():
        # test id: 'bcycle_indego_3004'
        # mapdata_df = pd.read_gbq(f"SELECT * FROM `musa509-lab09.finalproj.indego_neighbor_stations` WHERE station_id='bcycle_indego_3004' AND neighbor_StationID != 'bcycle_indego_3004'")

        mapdata_df = pd.read_gbq(f"SELECT * FROM `musa509-lab09.finalproj.indego_neighbor_stations` WHERE station_id='{row.station_id}' AND neighbor_StationID != '{row.station_id}'")
        mapdata_df.the_geom = gpd.GeoSeries.from_wkt(mapdata_df.the_geom)
        mapdata_gdf = gpd.GeoDataFrame(mapdata_df, geometry='the_geom')
        neighbors_nunique = mapdata_df[['neighbor_route', 'neighbor_modal','neighbor_station']].groupby('neighbor_modal').nunique()
        neighbors_count = mapdata_df[['neighbor_route', 'neighbor_modal','neighbor_station']].groupby('neighbor_modal').count()
        neighboring_bike_stations = mapdata_gdf[mapdata_gdf['neighbor_modal']=='Bike'][['neighbor_station','neighbor_StationID']]
        unique_bus_routes = mapdata_gdf[mapdata_gdf['neighbor_modal']=='Bus']['neighbor_route'].unique()
        unique_subway_routes = mapdata_gdf[mapdata_gdf['neighbor_modal']=='Subway']['neighbor_route'].unique()
        n_unique = {'bike': len(neighboring_bike_stations), 'bus_routes': len(unique_bus_routes), 'subway_routes': len(unique_subway_routes)}
        print(mapdata_df)
        output_station = template.render(
            station_name = row['name'],
            station_address = row['address'],
            lon = row['lon'],
            lat = row['lat'],
            mapdata = mapdata_gdf.to_json(),
            neighbors_count = neighbors_count.to_json(),
            neighbors_nunique = neighbors_nunique.to_json(),
            neighboring_bike_stations = json.loads(neighboring_bike_stations.to_json(orient='records')),
            unique_bus_routes = unique_bus_routes,
            unique_subway_routes = unique_subway_routes,
            n_unique = n_unique
        )
        pagename = row.station_id + '.html'
        page_location = str(output_root) + '/' + pagename
        with open(page_location, mode='w+') as outfile:
            outfile.write(output_station)
        upload_to_gcs(page_location, 'jawnt_philadelphia', pagename)

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

    # Render the data into the template.
    env = Environment(loader=FileSystemLoader(template_root))

    #render_index(env.get_template('index.html'), mapdata_gdf, counts)

    render_station_pages(env.get_template('station.html'), indego_df)

if __name__ == '__main__':
    main()
