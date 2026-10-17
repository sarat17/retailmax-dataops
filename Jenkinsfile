// Pipeline equivalente para Jenkins (el que corre en este repo es GitHub Actions)
pipeline {
  agent { docker { image 'python:3.11-slim' } }
  stages {
    stage('Build & Test')     { steps { sh 'pip install -r requirements.txt && pytest tests/test_features.py tests/test_limpieza.py' } }
    stage('Test de Datos')    { steps { sh 'pytest tests/test_datos.py' } }
    stage('Train & Validate') { steps { sh 'python -m src.models.entrenar_prediccion_ventas' } }
    stage('Empaquetado')      { steps { archiveArtifacts artifacts: 'modelo/*' } }
    stage('Deploy Staging')   { steps { echo 'Desplegando en staging...' } }
    stage('Aprobación')       { steps { input message: '¿Desplegar en producción?' } }
    stage('Deploy Prod')      { steps { echo 'Desplegando en producción (Canary)...' } }
  }
}
