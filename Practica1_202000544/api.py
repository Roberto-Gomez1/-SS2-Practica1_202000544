import pyodbc
import os

def execute_sql_file(file_path):
    # Configuración de la conexión
    conn_str = 'DRIVER={SQL Server};SERVER=DESKTOP-DM8TUGO\\SQLEXPRESS;DATABASE=Seminario2;Trusted_Connection=yes;'
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Leer el archivo SQL
    with open(file_path, 'r') as file:
        sql_script = file.read()

    # Ejecutar el script SQL
    cursor.execute(sql_script)
    conn.commit()
    cursor.close()
    conn.close()

def main():
    # Configuración de la conexión
    conn_str = 'DRIVER={SQL Server};SERVER=DESKTOP-DM8TUGO\\SQLEXPRESS;DATABASE=Seminario2;Trusted_Connection=yes;'
    conn = pyodbc.connect(conn_str)

    op = 0
    while True:
        print("Bienvenido al programa")
        print("1. Borrar modelo")
        print("2. Crear modelo")
        print("3. Extraer información")
        print("4. Cargar información")
        print("5. Realizar consultas")
        print("6. Salir")
        op = int(input("Seleccione una opcion:"))

        if op == 1:
            print("Borrando modelo...")
            execute_sql_file(r"C:\Users\Roberto\Desktop\Semestre\Semi2\Lab\-SS2-Practica1_202000544\Scripts\BorrarModelo.sql")
            input("")
        elif op == 2:
            print("Creando modelo...")
            execute_sql_file(r"C:\Users\Roberto\Desktop\Semestre\Semi2\Lab\-SS2-Practica1_202000544\Scripts\CrearModelo.sql")
            input("")
        elif op == 3:
            print("Extrayendo la informacion...")
            execute_sql_file(r"C:\Users\Roberto\Desktop\Semestre\Semi2\Lab\-SS2-Practica1_202000544\Scripts\ExtraerInformacion.sql")
            input("")
        elif op == 4:
            print("Cargando informacion...")
            execute_sql_file(r"C:\Users\Roberto\Desktop\Semestre\Semi2\Lab\-SS2-Practica1_202000544\Scripts\CargarInformacion.sql")
            input("")
        elif op == 5:
            print("Haciendo consultas...")
            hacerconsultas()
        elif op == 6:
            print("Gracias por preferirnos :)")
            break
        else:
            print("Ingrese una opcion valida.")
    
    conn.close()

def ejecutarConsultas(nombre_archivo, consulta):
    connection_string = 'DRIVER={SQL Server};SERVER=DESKTOP-DM8TUGO\\SQLEXPRESS;DATABASE=Seminario2;Trusted_Connection=yes;'
    resultados_carpeta = r'C:\Users\Roberto\Desktop\Semestre\Semi2\Lab\-SS2-Practica1_202000544\Resultados'
    os.makedirs(resultados_carpeta, exist_ok=True)
    """Ejecuta una consulta y guarda el resultado en un archivo de texto."""
    try:
        # Conectar a la base de datos
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            # Eliminar posibles instrucciones 'USE' de la consulta
            consulta_sin_use = '\n'.join([line for line in consulta.split('\n') if not line.strip().upper().startswith('USE')])
            cursor.execute(consulta_sin_use)
            with open(os.path.join(resultados_carpeta, nombre_archivo), 'w', encoding='utf-8') as f:
                result_set_number = 1
                while True:
                    if cursor.description:
                        # Existe un conjunto de resultados para procesar
                        columns = [column[0] for column in cursor.description]
                        resultados = cursor.fetchall()
                        # Escribir un encabezado indicando el número del conjunto de resultados
                        f.write(f"Conjunto de resultados {result_set_number}:\n")
                        # Escribir los nombres de las columnas
                        f.write('\t'.join(columns) + '\n')
                        for fila in resultados:
                            f.write('\t'.join(map(str, fila)) + '\n')
                        f.write('\n')  # Añadir una línea en blanco entre conjuntos de resultados
                        result_set_number += 1
                    else:
                        # No hay conjunto de resultados, posiblemente debido a una declaración que no devuelve resultados
                        pass
                    if not cursor.nextset():
                        break
                
        print(f"Consulta '{nombre_archivo}' ejecutada y guardada en '{resultados_carpeta}'")
    
    except Exception as e:
        print(f"Error al ejecutar la consulta o guardar el archivo '{nombre_archivo}': {e}")

def hacerconsultas():
    consultas={
        'Consulta1.txt':'''Select count(*) from  Pasajero
                            Select count(*) from Aeropuerto
                            Select count(*)  from Piloto
                            Select count(*)  from Vuelo''',
        'Consulta2.txt':'''Use Seminario2
                            SELECT 
                                Gender,
                                COUNT(*) AS TotalByGender,
                                (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Pasajero)) AS Percentage
                            FROM 
                                Pasajero
                            GROUP BY 
                                Gender;
                            ''',
        'Consulta3.txt':'''USE Seminario2;

                            WITH MonthlyFlightCounts AS (
                                SELECT 
                                    p.Nationality,
                                    FORMAT(v.DepartureDate, 'MM-yyyy') AS MonthYear,
                                    COUNT(v.HechoID) AS FlightCount
                                FROM 
                                    Vuelo v
                                JOIN 
                                    Pasajero p ON v.PassengerID = p.PassengerID
                                GROUP BY 
                                    p.Nationality,
                                    FORMAT(v.DepartureDate, 'MM-yyyy')
                            ),
                            MaxMonthlyFlights AS (
                                SELECT
                                    Nationality,
                                    MAX(FlightCount) AS MaxFlightCount
                                FROM
                                    MonthlyFlightCounts
                                GROUP BY
                                    Nationality
                            )
                            SELECT
                                m.Nationality,
                                m.MonthYear,
                                m.FlightCount
                            FROM
                                MonthlyFlightCounts m
                            JOIN
                                MaxMonthlyFlights maxf
                                ON m.Nationality = maxf.Nationality
                                AND m.FlightCount = maxf.MaxFlightCount
                            ORDER BY
                                m.Nationality,
                                m.MonthYear;
                            ''',
        'Consulta4.txt':'''Use Seminario2
                            SELECT 
                                a.CountryName AS Country,
                                COUNT(*) AS FlightCount
                            FROM 
                                Vuelo v
                            JOIN 
                                Aeropuerto a ON v.ArrivalAirportID = a.ArrivalAirportID
                            GROUP BY 
                                a.CountryName
                            ORDER BY 
                                FlightCount DESC;
                            ''',
        'Consulta5.txt': '''Use Seminario2
                            SELECT TOP 5
                                a.AirportName,
                                COUNT(v.PassengerID) AS PassengerCount
                            FROM 
                                Vuelo v
                            JOIN 
                                Aeropuerto a ON v.ArrivalAirportID = a.ArrivalAirportID
                            GROUP BY 
                                a.AirportName
                            ORDER BY 
                                PassengerCount DESC;
                            ''',
        'Consulta6.txt': '''Use Seminario2
                            SELECT TOP 3
                                FlightStatus AS Status,
                                COUNT(*) AS FlightCount
                            FROM 
                                Vuelo
                            GROUP BY 
                                FlightStatus
                            ORDER BY 
                                FlightCount DESC;
                            ''',
        'Consulta7.txt': '''Use Seminario2
                            SELECT TOP 5
                                a.CountryName AS Country,
                                COUNT(v.HechoID) AS FlightCount
                            FROM 
                                Vuelo v
                            JOIN 
                                Aeropuerto a ON v.ArrivalAirportID = a.ArrivalAirportID
                            GROUP BY 
                                a.CountryName
                            ORDER BY 
                                FlightCount DESC;
                            ''',
        'Consulta8.txt': '''Use Seminario2
                            SELECT TOP 5
                                a.AirportContinent AS Continent,
                                COUNT(v.HechoID) AS FlightCount
                            FROM 
                                Vuelo v
                            JOIN 
                                Aeropuerto a ON v.ArrivalAirportID = a.ArrivalAirportID
                            GROUP BY 
                                a.AirportContinent
                            ORDER BY 
                                FlightCount DESC;
                            ''',
        'Consulta9.txt': '''Use Seminario2
                            SELECT TOP 5
                                p.Gender,
                                p.Age,
                                COUNT(v.HechoID) AS FlightCount
                            FROM 
                                Vuelo v
                            JOIN 
                                Pasajero p ON v.PassengerID = p.PassengerID
                            GROUP BY 
                                p.Gender,
                                p.Age
                            ORDER BY 
                                FlightCount DESC;
                            ''',
        'Consulta10.txt': '''Use Seminario2
                            SELECT 
                                FORMAT(v.DepartureDate, 'MM-yyyy') AS MonthYear,
                                COUNT(v.HechoID) AS FlightCount
                            FROM 
                                Vuelo v
                            GROUP BY 
                                FORMAT(v.DepartureDate, 'MM-yyyy')
                            ORDER BY 
                                MonthYear;
                            '''
    }
    for nombre_archivo, r_consulta in consultas.items():
        ejecutarConsultas(nombre_archivo,r_consulta)

if __name__ == "__main__":
    main()
