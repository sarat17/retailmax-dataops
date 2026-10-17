# RetailMax DataOps

Repositorio del equipo de datos de RetailMax. Aquí está todo lo necesario
para reproducir nuestros pipelines, modelos y dashboards en DEV, QA y PROD.

## Cómo empezar
1. Clonar el repositorio: `git clone https://github.com/<usuario>/retailmax-dataops.git`
2. Instalar dependencias: `pip install -r requirements.txt`
3. Traer los datos versionados: `dvc pull`
4. Ejecutar las pruebas: `pytest tests/`

## Estructura
| Carpeta | Contenido |
|---|---|
| `src/` | Código: limpieza, variables y modelo de predicción de ventas |
| `notebooks/` | Notebooks exportados a `.py` y sin salidas |
| `sql/` | Consultas y migraciones de tablas (Flyway) |
| `tests/` | Pruebas de código, de esquema y de calidad de datos |
| `config/` | Configuración de cada entorno (YAML/JSON) |
| `pipelines/` | DAGs de Airflow |
| `infra/` | Infraestructura como código (Terraform) |
| `.github/workflows/` | Pipelines de CI/CD (GitHub Actions) |
| `docs/` | Procedencia de datos, diccionario y gobernanza |

## Qué se versiona (en Git)
- Código: scripts de Python en `src/`, notebooks exportados a `.py` y consultas SQL.
- Migraciones de tablas en `sql/migraciones/` (Flyway). Nunca se cambia una tabla a mano.
- Configuraciones: archivos YAML/JSON de cada entorno y parámetros del modelo.
- Dependencias: `requirements.txt` con versiones exactas y el `Dockerfile`.
- Pipelines: DAGs de Airflow, `Jenkinsfile` y workflows de GitHub Actions.
- Infraestructura: archivos de Terraform en `infra/`.
- Pruebas y reglas de calidad en `tests/`.
- Punteros de datos de DVC (`.dvc`) y documentación.

## Qué NO se versiona y por qué
- **Datos crudos o grandes** (CSV, Parquet): Git no está hecho para archivos grandes.
  Se guardan aparte y se versionan con DVC.
- **Datos personales de clientes**: por seguridad y por ley de protección de datos.
- **Contraseñas, llaves y tokens** (`.env`): se guardan en un gestor de secretos.
- **Modelos entrenados** (`.pkl`): se registran en MLflow / artefactos del pipeline.
- **Archivos temporales** (salidas de notebooks, cachés, estado de Terraform).

Todo esto está definido en `.gitignore`.

## Versionado de la procedencia de datos
No guardamos los datos en Git, pero sí registramos de dónde viene cada dato:
- Cada dataset tiene un archivo `.dvc` con un hash que identifica su versión exacta.
  Con `git checkout <versión>` y luego `dvc pull` se recuperan los datos de ese momento.
- `docs/procedencia_datos.md` documenta para cada tabla: sistema de origen,
  responsable (data owner), frecuencia de actualización y transformaciones.
- Cada ejecución del pipeline de CD guarda la métrica del modelo y el commit usado.

## Flujo de trabajo
rama feature → pull request → pruebas automáticas (CI) → revisión → merge a main → pipeline de CD → staging → aprobación → producción
