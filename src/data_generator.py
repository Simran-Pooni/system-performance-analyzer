import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_data(num_rows=1000):
    # Timestamps: letzte 30 Tage, stündlich
    end_time = datetime.now()
    start_time = end_time - timedelta(days=30)
    timestamps = pd.date_range(start=start_time, end=end_time, periods=num_rows)
    
    # Simulierte Daten
    np.random.seed(42)  # Für Reproduzierbarkeit
    temperature = np.random.normal(25, 5, num_rows)  # Normalverteilt
    cpu_usage = np.random.uniform(10, 90, num_rows)  # Gleichverteilt
    response_time = np.random.exponential(100, num_rows)  # Exponential
    load = 50 + 10 * np.sin(np.linspace(0, 4*np.pi, num_rows)) + np.random.normal(0, 5, num_rows)  # Trend mit Rauschen
    
    # Ausreißer hinzufügen (5%)
    outlier_indices = np.random.choice(num_rows, size=int(0.05 * num_rows), replace=False)
    temperature[outlier_indices] += np.random.choice([-20, 20], len(outlier_indices))
    cpu_usage[outlier_indices] = np.random.choice([5, 95], len(outlier_indices))
    
    # DataFrame erstellen
    df = pd.DataFrame({
        'timestamp': timestamps,
        'temperature': temperature,
        'cpu_usage': cpu_usage,
        'response_time': response_time,
        'load': load
    })
    
    return df

if __name__ == "__main__":
    df = generate_data()
    df.to_csv('data/system_data.csv', index=False)
    print("Daten generiert und in data/system_data.csv gespeichert.")