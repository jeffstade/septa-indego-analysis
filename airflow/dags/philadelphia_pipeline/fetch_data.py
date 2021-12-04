#https://gbfs.bcycle.com/bcycle_indego/station_information.json

from pathlib import Path
from pipeline_tools import http_to_gcs

# GET INDEGO STATION DATA
http_to_gcs('get', 'https://gbfs.bcycle.com/bcycle_indego/station_information.json',
                'jawnt_philadelphia', 'data/indego_stations.geojson',
                request_data=None, request_files=None)


# GET SEPTA BUS STATION DATA
http_to_gcs('get', 'https://opendata.arcgis.com/datasets/05374634f1ed45f7a910fcf2599545b9_0.geojson',
                'jawnt_philadelphia', 'data/septa_bus_stations.geojson',
                request_data=None, request_files=None)


# GET SEPTA BSL DATA
http_to_gcs('get', 'https://opendata.arcgis.com/datasets/2e9037fd5bef406488ffe5bb67d21312_0.geojson',
                'jawnt_philadelphia', 'data/septa_bsl_stations.geojson',
                request_data=None, request_files=None)

# GET SEPTA MFL DATA
http_to_gcs('get', 'https://opendata.arcgis.com/datasets/8c6e2575c8ad46eb887e6bb35825e1a6_0.geojson',
                'jawnt_philadelphia', 'data/septa_mfl_stations.geojson',
                request_data=None, request_files=None)
