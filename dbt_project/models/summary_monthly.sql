{{ config(
    materialized='table'
) }}

SELECT 
    CURRENT_DATE AS month,  -- Usamos la fecha actual ya que no hay una columna "date"
    AVG(s.avg_price) AS avg_price_monthly,
    AVG(s.volume) AS avg_volume_monthly
FROM {{ source('public', 'stock_data') }} AS s  -- Ahora DBT sabe que 'stock_data' es una fuente externa
GROUP BY CURRENT_DATE


