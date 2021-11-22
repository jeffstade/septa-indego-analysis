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
   # mapdata_df = pd.read_gbq('SELECT * FROM lab09.blockgroups_mapdata')
   # mapdata_df.blockgroup_geom = gpd.GeoSeries.from_wkt(mapdata_df.blockgroup_geom)
   # mapdata_gdf = gpd.GeoDataFrame(mapdata_df, geometry='blockgroup_geom')

    # Download the chart data.
  #  chartdata_df = pd.read_gbq('SELECT * from lab09.blockgroups_chartdata')

    # Download the population density list data.
 #   listdata_df = pd.read_gbq('SELECT * from lab09.blockgroups_listdata')

    # Render the data into the template.
    env = Environment(loader=FileSystemLoader(template_root))
    print(os.getcwd())
    template = env.get_template('index.html')
    output = template.render(
    #    mapdata=mapdata_gdf.to_json(),
    #    chartdata=chartdata_df.to_dict('list'),
    #    listdata=listdata_df.to_dict('records'),
    )

    # Save the rendered output to a file in the "output" folder.
    print(output_root)
    with open(output_root + '/index.html', mode='w') as outfile:
        outfile.write(output)
        print(output)
        print(os.getcwd())
    upload_to_gcs('output/index.html', 'jawnt_philadelphia', 'index.html')

if __name__ == '__main__':
    main()
