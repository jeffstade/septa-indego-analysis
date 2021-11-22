#####
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/jeffstern/Documents/UPenn/Courses/MUSA-509/keys/musa509-lab09-46a0d7200e51.json'
#####


from pathlib import Path
from pipeline_tools import run_transform_gbq
from render_report import local_to_gbq

sql_root = Path(__file__).parent / 'sql'
db_connection = 'musa509-lab09:us-central1:musa509-final'

def main():
    local_to_gbq('data/indego-trips-2021-q3/indego-trips-2021-q3.csv', 'musa509-lab09.finalproj.indego_trips' )
    local_to_gbq('data/indego-trips-2021-q3/indego-stations-2021-10-01.csv', 'musa509-lab09.finalproj.indego_stations' )
    local_to_gbq('data/septa_gtfs_public/google_bus/stops.csv', 'musa509-lab09.finalproj.septa_bus_stops' )


if __name__ == '__main__':
    main()
