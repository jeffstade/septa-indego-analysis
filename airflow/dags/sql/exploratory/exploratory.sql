-- with indego station data loaded into GBQ, can use this to see all stations 
-- using BigQuery Geo Viz

SELECT ST_GEOGPOINT(lon, lat) AS coord
FROM finalproj.indego_stations