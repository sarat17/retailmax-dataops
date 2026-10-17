# Gobernanza del dato maestro "Cliente"

## 1. Definición de cliente activo (v1, vigente desde 2026-11-01)
Persona o empresa con al menos una compra (tienda o e-commerce) en los últimos 12 meses
en cualquiera de los 5 países. Sin compras en 12 meses: inactivo. En 36 meses: histórico.

## 2. Limpieza y duplicados
- Documento sin puntos, guiones ni espacios, con tipo de documento y país.
- Nombres sin espacios de más; correos en minúscula y con formato válido.
- Dos registros son el mismo cliente si tienen el mismo tipo y número de documento en el mismo país.
- Ningún registro se borra al unir duplicados; los casos dudosos los revisa el data steward.

## 3. Flujo de aprobación de cambios
Solicitud (ticket) → análisis del data steward → aprobación del data owner o del comité
→ cambio por pull request → QA → registro con versión y fecha.

## 4. Acceso y seguridad
Mínimo privilegio, datos personales cifrados y enmascarados en DEV/QA, registro de accesos,
revisión de permisos cada 3 meses y cumplimiento de la Ley 1581 de 2012.
