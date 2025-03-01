Pipeline de Calidad de Datos - Superintendencia de Bancos

Descripcion
Este proyecto extrae datos financieros de Yahoo Finance, los transforma y los carga en PostgreSQL, automatizando todo el proceso con Prefect y DBT.

Estructura del Proyecto
SBTEST/
- venv/ Entorno virtual de Python
- dbt_project/ Proyecto DBT para transformacion de datos
- models/ Modelos SQL en DBT
- docs/ Documentacion y diagramas del pipeline
- extract.py Script para extraer datos desde Yahoo Finance
- transform.py Script para transformar los datos
- load.py Script para cargar los datos en PostgreSQL
- prefect_pipeline.py Orquestacion del pipeline con Prefect
- docker-compose.yml Configuracion de contenedores Docker
- README.md Documentacion del proyecto

Instalacion
1. Clonar el repositorio
git clone https://github.com/isaiasrl6/pruebas.git
cd pruebas

2. Crear el entorno virtual e instalar dependencias
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3. Levantar las bases de datos con Docker
docker-compose up -d

4. Ejecutar el pipeline manualmente con Prefect
python prefect_pipeline.py

5. Verificar los datos en PostgreSQL
docker exec -it postgres_db psql -U admin -d mydatabase -c "SELECT * FROM stock_data LIMIT 10;"

6. Automatizacion del Pipeline (Prefect)
Prefect ejecuta el pipeline cada 6 horas automaticamente.
Para revisar las tareas en ejecucion:
prefect server start
prefect agent start --work-queue "default"

Herramientas Utilizadas
- Python Scripts de extraccion, transformacion y carga de datos
- PostgreSQL Base de datos para almacenar datos
- ClickHouse Almacen OLAP para analisis de datos
- DBT Transformacion y validacion de datos
- Prefect Orquestacion y automatizacion del pipeline
- Docker Contenedores para PostgreSQL y ClickHouse

Diagramas del Pipeline
Arquitectura del Pipeline
docs/Pipeline_Arquitectura.png

Contacto
Desarrollado por: Isaias Rosario
Repositorio: https://github.com/isaiasrl6/pruebas

