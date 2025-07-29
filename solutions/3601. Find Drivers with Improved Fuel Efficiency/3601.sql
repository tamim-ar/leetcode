SELECT
  t.driver_id,
  d.driver_name,
  ROUND(
    AVG(CASE WHEN MONTH(t.trip_date) BETWEEN 1 AND 6 THEN t.distance_km/t.fuel_consumed END),
    2
  ) AS first_half_avg,
  ROUND(
    AVG(CASE WHEN MONTH(t.trip_date) BETWEEN 7 AND 12 THEN t.distance_km/t.fuel_consumed END),
    2
  ) AS second_half_avg,
  ROUND(
    AVG(CASE WHEN MONTH(t.trip_date) BETWEEN 7 AND 12 THEN t.distance_km/t.fuel_consumed END)
    - AVG(CASE WHEN MONTH(t.trip_date) BETWEEN 1 AND 6 THEN t.distance_km/t.fuel_consumed END),
    2
  ) AS efficiency_improvement
FROM trips t
JOIN drivers d USING (driver_id)
WHERE t.fuel_consumed > 0
  AND MONTH(t.trip_date) BETWEEN 1 AND 12
GROUP BY t.driver_id
HAVING
  COUNT(CASE WHEN MONTH(t.trip_date) BETWEEN 1 AND 6 THEN 1 END) > 0
  AND COUNT(CASE WHEN MONTH(t.trip_date) BETWEEN 7 AND 12 THEN 1 END) > 0
  AND AVG(CASE WHEN MONTH(t.trip_date) BETWEEN 7 AND 12 THEN t.distance_km/t.fuel_consumed END)
    > AVG(CASE WHEN MONTH(t.trip_date) BETWEEN 1 AND 6 THEN t.distance_km/t.fuel_consumed END)
ORDER BY efficiency_improvement DESC, d.driver_name;
