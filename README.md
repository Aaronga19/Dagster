# Dagster
Data Orchestration with python 

## pipeline 
Se ha construido una aplicación donde recopile información de un archivo excel y este sea leido, transformado y cargado a la base de datos local.

## Ejecución
Necesario python 3.7+

Por ahora se puede ejecutar en un entorno local añadiendo un archivo en el directorio raíz con nombre ".env" con la información como se muestra a continuación.
```
DAGSTER_HOME = path\dagster_home        #Ejemplo: \c\Users\Usuario\Documents\GitHub\data-engineering\pipelines\dagster\dagster_home
DAGSTER_PG_USERNAME = usuario
DAGSTER_PG_PASSWORD = contraseña
DAGSTER_PG_HOST = host
DAGSTER_PG_DB = nombre_bd
DAGSTER_PG_PORT = puerto
```

Para ejecutar el script es necesaria situarse en la carpeta raíz del proyecto y ejecutar la siguiente sentencia.

```
python3 ETL.py
```
O a través de dagit hay que ejecutar la siguiente sentencia

```
dagit -f ETL.py
```
Y dentro del servidor en la pestaña de _launchpad_ presionar el boton _**launch run**_
