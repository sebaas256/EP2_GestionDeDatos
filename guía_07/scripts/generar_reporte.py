from pathlib import Path
import pandas as pd
import numpy as np

# Ruta base del proyecto
BASE = Path('/content/EP2_GestiónDeDatos')

def generar_reporte():
    # Cargar dataset de operaciones
    ruta_csv = BASE / 'datos' / 'procesados' / 'operacion_centros.csv'
    df_operacion = pd.read_csv(ruta_csv)
    df_operacion['fecha'] = pd.to_datetime(df_operacion['fecha'])

    # Calcular déficit
    df_operacion['deficit_paquetes'] = np.maximum(
        df_operacion['demanda_paquetes'] - df_operacion['capacidad_paquetes'], 0
    )

    # Calcular totales con Pandas / NumPy
    capacidad_total = df_operacion['capacidad_paquetes'].sum()
    demanda_total = df_operacion['demanda_paquetes'].sum()
    deficit_total = df_operacion['deficit_paquetes'].sum()
    cobertura_pct = 100 * (1 - (deficit_total / demanda_total))

    # Crear diccionario de KPIs
    kpis = {
        'capacidad_total': capacidad_total,
        'demanda_total': demanda_total,
        'deficit_total': deficit_total,
        'cobertura_pct': cobertura_pct,
        'periodo': f"{df_operacion['fecha'].min().strftime('%d/%m/%Y')} al {df_operacion['fecha'].max().strftime('%d/%m/%Y')}"
    }

    # Imprimir consola
    print("KPIs DEL PERIODO - SMARTROUTE LOGISTICS")
    print("=" * 50)
    print(f"Capacidad Total:     {kpis['capacidad_total']:>12,.0f}")
    print(f"Demanda Total:       {kpis['demanda_total']:>12,.0f}")
    print(f"Déficit Total:       {kpis['deficit_total']:>12,.0f}")
    print(f"Cobertura %:         {kpis['cobertura_pct']:>11.1f}%")
    print(f"Periodo:             {kpis['periodo']}")
    print("=" * 50)

    return kpis

if __name__ == '__main__':
    generar_reporte()
