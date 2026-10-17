SELECT pais, tienda, SUM(ventas) AS total_ventas
FROM ventas
GROUP BY pais, tienda
ORDER BY total_ventas DESC;
