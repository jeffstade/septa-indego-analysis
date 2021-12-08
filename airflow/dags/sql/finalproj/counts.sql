SELECT DISTINCT Modal, Route as routes, COUNT(*) AS stop_count
FROM finalproj.combined_stations
GROUP BY Modal, Route