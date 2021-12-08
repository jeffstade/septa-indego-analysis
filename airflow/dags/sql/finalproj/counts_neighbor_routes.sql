SELECT station_id, name, neighbor_modal, COUNT(*) as n_routes FROM
    (SELECT DISTINCT station_id, name, neighbor_modal, neighbor_route
    FROM `musa509-lab09.finalproj.indego_neighbor_stations`
    WHERE neighbor_modal != 'Bike'
    )
GROUP BY station_id, name, neighbor_modal