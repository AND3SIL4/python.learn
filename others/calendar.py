import pandas as pd
import calendar

# Crear una lista para almacenar los datos del calendario
calendario = []

# Generar el calendario para cada mes
for mes in range(1, 13):
    mes_nombre = calendar.month_name[mes]
    _, num_dias = calendar.monthrange(2025, mes)
    semana_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    # Crear una lista para las filas del mes
    mes_filas = []
    dia_inicial = 1
    primera_semana = ["" if i < calendar.weekday(2025, mes, dia_inicial) else dia_inicial + i - calendar.weekday(2025, mes, dia_inicial) for i in range(7)]
    mes_filas.append(primera_semana)
    
    dia_inicial += len([d for d in primera_semana if isinstance(d, int)])
    while dia_inicial <= num_dias:
        semana = [dia_inicial + i if dia_inicial + i <= num_dias else "" for i in range(7)]
        mes_filas.append(semana)
        dia_inicial += 7
    
    # Añadir los datos al calendario
    calendario.append((mes_nombre, pd.DataFrame(mes_filas, columns=semana_dias)))

# Crear un archivo Excel con una hoja para cada mes
ruta_archivo = '/mnt/data/Calendario_2025.xlsx'
with pd.ExcelWriter(ruta_archivo, engine='xlsxwriter') as writer:
    for mes_nombre, df in calendario:
        df.to_excel(writer, sheet_name=mes_nombre, index=False)

ruta_archivo

