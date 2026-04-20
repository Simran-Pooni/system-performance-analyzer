import pandas as pd
from sqlalchemy import create_engine, Column, Integer, Float, DateTime, MetaData, Table
from sqlalchemy.orm import sessionmaker
import os

# DB-Setup
engine = create_engine('sqlite:///db/system_data.db')
metadata = MetaData()

# Tabelle definieren
performance_data = Table(
    'performance_data', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('timestamp', DateTime),
    Column('temperature', Float),
    Column('cpu_usage', Float),
    Column('response_time', Float),
    Column('load', Float)
)

# Tabelle erstellen
metadata.create_all(engine)

def load_csv_to_db(csv_path='data/system_data.csv'):
    df = pd.read_csv(csv_path, parse_dates=['timestamp'])
    df.to_sql('performance_data', engine, if_exists='replace', index=False)
    print("Daten in DB geladen.")

def query_all_data():
    query = "SELECT * FROM performance_data"
    return pd.read_sql(query, engine)

def query_by_date_range(start_date, end_date):
    query = f"SELECT * FROM performance_data WHERE timestamp BETWEEN '{start_date}' AND '{end_date}'"
    return pd.read_sql(query, engine)

def query_stats(metric):
    query = f"SELECT AVG({metric}) as mean, MIN({metric}) as min_val, MAX({metric}) as max_val FROM performance_data"
    return pd.read_sql(query, engine)

if __name__ == "__main__":
    load_csv_to_db()
    # Beispiel-Queries
    print("Alle Daten (erste 5 Zeilen):")
    print(query_all_data().head())
    print("\nStats für cpu_usage:")
    print(query_stats('cpu_usage'))