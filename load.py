import psycopg2
import numpy as np
from extract import extract_data
from transform import transform_data

def load_data(df):
    conn = psycopg2.connect(
        dbname="mydatabase", user="admin", password="admin", host="127.0.0.1", port="5432"
    )
    cursor = conn.cursor()
    
    # Crear la tabla si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stock_data (
            id SERIAL PRIMARY KEY,
            avg_price FLOAT,
            volume BIGINT
        )
    """)
    
    # Convertir datos a tipos compatibles con PostgreSQL
    for _, row in df.iterrows():
        avg_price = float(row["avg_price"])  # Asegurar que sea float estándar
        volume = int(row["Volume"])  # Asegurar que sea int estándar
        cursor.execute("INSERT INTO stock_data (avg_price, volume) VALUES (%s, %s)", (avg_price, volume))
    
    conn.commit()
    conn.close()
    print("✅ Datos cargados en PostgreSQL correctamente")

if __name__ == "__main__":
    df = extract_data("JPM")
    df_transformed = transform_data(df)
    load_data(df_transformed)
