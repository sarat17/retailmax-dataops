# Diccionario de datos - ventas

| Columna | Tipo | Descripción |
|---|---|---|
| fecha | fecha | Día de la venta |
| pais | texto (2) | Código del país (CO, PE, CL, MX, EC) |
| tienda | texto | Ciudad de la tienda |
| mes | entero | Mes de la venta (1-12) |
| es_fin_de_semana | 0/1 | 1 si la venta fue en fin de semana |
| precio_unitario | decimal | Precio por unidad (mayor que 0) |
| unidades | entero | Unidades vendidas |
| ventas | decimal | precio_unitario × unidades |
