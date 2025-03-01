from prefect import flow, task
import subprocess
from prefect.server.schemas.schedules import IntervalSchedule
from datetime import timedelta

@task
def check_new_data():
    """Verifica si hay nuevos datos en la tabla stock_data"""
    result = subprocess.run(
        ["docker", "exec", "postgres_db", "psql", "-U", "admin", "-d", "mydatabase", "-t", "-c",
         "SELECT COUNT(*) FROM stock_data;"],
        capture_output=True, text=True
    )
    count = int(result.stdout.strip())
    return count > 0  # Retorna True si hay datos nuevos

@task
def run_dbt():
    """Ejecuta dbt run dentro de la carpeta dbt_project"""
    try:
        result = subprocess.run(
            ["bash", "-c", "cd /Users/isaiasrosario/Desktop/SBTEST/dbt_project && dbt run"],
            check=True, capture_output=True, text=True, shell=True
        )
        print("✅ DBT ejecutado correctamente.")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("❌ Error ejecutando DBT:")
        print(e.stdout)
        print(e.stderr)

@flow
def etl_pipeline():
    """Pipeline completo con verificación de nuevos datos"""
    if check_new_data():
        print("🔄 Nuevos datos detectados. Ejecutando DBT...")
        run_dbt()
    else:
        print("⚠️ No hay nuevos datos. No se ejecuta DBT.")

# Programar la ejecución cada 6 horas
if __name__ == "__main__":
    from prefect.deployments import run_deployment

    etl_pipeline().serve(name="ETL_Scheduler", interval=timedelta(hours=6))


    schedule = IntervalSchedule(interval=timedelta(hours=6))
    deployment = Deployment.build_from_flow(
        flow=etl_pipeline,
        name="ETL_Scheduler",
        schedule=schedule,
    )
    deployment.apply()

    etl_pipeline()

