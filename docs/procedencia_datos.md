# Procedencia de los datos

| Tabla / archivo | Sistema de origen | Data owner | Frecuencia | Transformaciones | Versionado |
|---|---|---|---|---|---|
| ventas | POS de tiendas y e-commerce (5 países) | Gerente Comercial | Diaria | Limpieza, conversión de moneda | Delta Lake + DVC |
| clientes | CRM, e-commerce, POS | Director de Mercadeo | Diaria | Limpieza, unión de duplicados (MDM) | Snapshots diarios |
| productos | ERP, catálogo e-commerce | Gerente de Categorías | Diaria | Estandarización de SKU | Snapshots diarios |
| data/muestra/ventas_muestra.csv | Muestra anonimizada para pruebas | Equipo de datos | Fija | Ninguna | Git (archivo pequeño) |
