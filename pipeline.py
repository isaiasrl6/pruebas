from prefect import flow, task
from extract import extract_data
from transform import transform_data
from load import load_data

token = "JPM"

@task
def extract_task():
    return extract_data(token)

@task
def transform_task(df):
    return transform_data(df)

@task
def load_task(df):
    load_data(df)

@flow
def etl_pipeline():
    df = extract_task()
    df_transformed = transform_task(df)
    load_task(df_transformed)
    print("✅ Pipeline ejecutado con éxito")

if __name__ == "__main__":
    etl_pipeline()
