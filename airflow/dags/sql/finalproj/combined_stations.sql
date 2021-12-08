(SELECT OBJECTID, 'Subway' as Modal, Route, Station, CAST(Stop_ID as string) as StationID, Longitude as lon, Latitude as lat, ST_GEOGPOINT(Longitude, Latitude) AS the_geom FROM `musa509-lab09.finalproj.septa_bsl_stations`)
UNION ALL 
(SELECT OBJECTID, 'Subway' as Modal, Route, Station, CAST(Stop_ID as string) as StationID, Longitude as lon, Latitude as lat, ST_GEOGPOINT(Longitude, Latitude) AS the_geom FROM `musa509-lab09.finalproj.septa_mfl_stations`)
UNION ALL 
(SELECT FID as OBJECTID, 'Bus' as Modal, LineAbbr as Route, StopName as Station, CAST(StopId as string) as StationID, Lon as lon, Lat as lat, ST_GEOGPOINT(Lon, Lat) AS the_geom FROM `musa509-lab09.finalproj.septa_bus_stations`
WHERE LineAbbr != 'MFL' OR LineAbbr != 'BSL')
UNION ALL
(SELECT ROW_NUMBER() over (Order by station_id ASC) AS OBJECTID, 'Bike' as Modal, '' as Route, name as Station, station_id as StationID, lon, lat, ST_GEOGPOINT(lon, lat) AS the_geom FROM `musa509-lab09.finalproj.indego_stations`)