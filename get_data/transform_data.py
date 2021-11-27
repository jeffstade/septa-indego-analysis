#####
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/jeffstern/Documents/UPenn/Courses/MUSA-509/keys/musa509-lab09-46a0d7200e51.json'
#####


from pathlib import Path
from pipeline_tools import run_transform_gbq
from pipeline_tools import gcs_to_local_file
from pipeline_tools import geopandas_to_gbq
import geopandas as gpd
import json
from shapely.geometry import Point

sql_root = Path(__file__).parent / 'sql'
db_connection = 'musa509-lab09:us-central1:musa509-final'

def main():
    # testing with local files
    #local_to_gbq('data/indego-trips-2021-q3/indego-trips-2021-q3.csv', 'musa509-lab09.finalproj.indego_trips' )
    #local_to_gbq('data/indego-trips-2021-q3/indego-stations-2021-10-01.csv', 'musa509-lab09.finalproj.indego_stations' )
    #local_to_gbq('data/septa_gtfs_public/google_bus/stops.csv', 'musa509-lab09.finalproj.septa_bus_stops' )
    """ 
    indego_data = gcs_to_local_file(
        gcs_bucket_name= 'jawnt_philadelphia', 
        gcs_blob_name= 'data/indego_stations.geojson', 
        local_file_name='indego_stations.geojson')
    f = open('indego_stations.geojson')
    df = json.load(f)
    df = df['data']['stations']
    for d in df:
        d['the_geom'] = Point(d['lat'], d['lon'])
    gdf = gpd.GeoDataFrame(df).set_geometry('the_geom').set_crs('epsg:32129')
    geopandas_to_gbq(gdf, 'finalproj', 'indego_stations', replace_table=True)
    """

    for tablename in ['septa_bus_stations','septa_bsl_stations','septa_mfl_stations']:
        latloncolumnnames = ('Lat','Lon') if tablename=='septa_bus_stations' else ('Latitude','Longitude')
        data = gcs_to_local_file(
            gcs_bucket_name = 'jawnt_philadelphia',
            gcs_blob_name = 'data/'+tablename+'.geojson',
            local_file_name=tablename+'.geojson'
        )
        f = open(tablename+'.geojson')
        df = json.load(f)
        df_prop = [x['properties'] for x in df['features']]
        for d in df_prop:
            d['the_geom'] = Point(d[latloncolumnnames[0]],d[latloncolumnnames[1]])
        gdf = gpd.GeoDataFrame(df_prop).set_geometry('the_geom').set_crs('epsg:32129')
        geopandas_to_gbq(gdf, 'finalproj', tablename, replace_table=True)


if __name__ == '__main__':
    main()
