### Manual Tecnico
## Roberto Carlos Gómez Donis - 202000544

Este código es una función en Python diseñada para ejecutar un archivo SQL utilizando una conexión a una base de datos SQL Server.
``` def execute_sql_file(file_path):
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
```

En esta funcion hace la conexion a la base de datos lo cual nos permite ejecutar nuestros archivos .sql como si estuvieramos en "SSMS", apartir de aca se puede armar el menu, el cual es el siguiente:

```
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
            execute_sql_file(r"C:\Users\Roberto\Desktop\Semestre\Semi2\Lab\-SS2-Practica1_202000544\Scripts\BorrarModelo.sql", conn)
            input("")
        elif op == 2:
            print("Creando modelo...")
            execute_sql_file(r"C:\Users\Roberto\Desktop\Semestre\Semi2\Lab\-SS2-Practica1_202000544\Scripts\CrearModelo.sql", conn)
            input("")
        elif op == 3:
            print("Extrayendo la informacion...")
            execute_sql_file(r"C:\Users\Roberto\Desktop\Semestre\Semi2\Lab\-SS2-Practica1_202000544\Scripts\ExtraerInformacion.sql", conn)
            input("")
        elif op == 4:
            print("Cargando informacion...")
            execute_sql_file(r"C:\Users\Roberto\Desktop\Semestre\Semi2\Lab\-SS2-Practica1_202000544\Scripts\CargarInformacion.sql", conn)
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
  
```

En esta parte se crea lo que es el menu dando al usuario una interfaz por consola para seleccionar sus opciones, aca manda a llamar lo que es la conexion (del metodo anterior explicado) y asi ejecutar nuestro .sql

```
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
```

La conexión a la base de datos se establece utilizando pyodbc.connect(connection_string).
Se crea un cursor para ejecutar la consulta.
Se eliminan las instrucciones USE del script SQL (en caso de que existan) usando una comprensión de lista.
La consulta se ejecuta usando cursor.execute(consulta_sin_use). Se procesan y escriben los resultados:
Se verifica si hay un conjunto de resultados disponible (cursor.description).
Se obtienen los nombres de las columnas y los datos de las filas.
Se escribe la información en el archivo en formato tabulado.
Se maneja la presencia de múltiples conjuntos de resultados y se agregan separadores entre ellos.

Por ultimo queda el metodo "hacerconsultas():" este es un manejo de diccionario el cual contiene la consulta dentro del diccionario, tambien el nombre con el cual se guardara el archivo de salida.