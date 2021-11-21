import datetime as dt
import pandas as pd
import sqlalchemy as sqa
import requests

# INDEGO
# Station feed: http://www.rideindego.com/stations/json/ (updated live)
# Ride data: https://u626n26h74f16ig1p3pt0f2g-wpengine.netdna-ssl.com/wp-content/uploads/2021/10/indego-trips-2021-q3.zip (updated quarterly)
# Stations: https://www.rideindego.com/wp-content/uploads/2021/01/indego-stations-2021-01-01.csv (updated irregularly)

# SEPTA
# Locations API: https://www3.septa.org/hackathon/locations/get_locations.php?lon=-75.33299748&lat=40.11043326&radius=40
# Bus stop dataset: https://septaopendata-septa.opendata.arcgis.com/datasets/fall-2021-stops-by-route/explore?location=39.908217%2C-75.166495%2C13.00
  # https://opendata.arcgis.com/datasets/05374634f1ed45f7a910fcf2599545b9_0.geojson
# Norristown: https://septaopendata-septa.opendata.arcgis.com/datasets/septa-norristown-highspeed-line-stations/explore?location=39.984164%2C-75.265104%2C12.63
  # https://opendata.arcgis.com/datasets/f106f00a4ac34885ab35f4ebabb2aee0_0.geojson
# Broad: https://septaopendata-septa.opendata.arcgis.com/datasets/septa-broad-street-line-stations/explore
  # https://opendata.arcgis.com/datasets/2e9037fd5bef406488ffe5bb67d21312_0.geojson  
# MFL: https://septaopendata-septa.opendata.arcgis.com/datasets/septa-market-frankford-line-stations/explore
  # https://opendata.arcgis.com/datasets/8c6e2575c8ad46eb887e6bb35825e1a6_0.geojson
# store locally
## Philadelphia neighborhoods

def getData():
    # this will get the correct dataset from the web and store it locally
    print("TK")


def loadData():
    #this will load the data into database
    print("TK")

