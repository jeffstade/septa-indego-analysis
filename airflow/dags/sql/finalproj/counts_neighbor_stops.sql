SELECT station_id, name, neighbor_modal, COUNT(*) as n_stops FROM
(SELECT DISTINCT station_id, name, neighbor_modal, neighbor_stationID
FROM `musa509-lab09.finalproj.indego_neighbor_stations`
)
GROUP BY station_id, name, neighbor_modal