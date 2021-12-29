# Dagster
Data Orchestration with python 

## pipeline 
Se ha construido una aplicación donde recopile información de un archivo excel y este sea leido, transformado y cargado a la base de datos local.

## Ejecución
Necesario python 3.7+

Para el el correcto funcionamiento de _daemon_ en windows es necesario acceder a las variables de entorno del sistema y declarar una variable llamada **DAGSTER_HOME** con la ruta en donde se encuentra la carpeta *dagster_home**

_**Ejemplo**_
```
 #Ejemplo: \c\Users\Usuario\Documents\data-engineering\pipelines\dagster\dagster_home
```
Por ahora se puede ejecutar en un entorno local añadiendo un archivo en el directorio raíz con nombre ".env" con la información como se muestra a continuación.
```
DAGSTER_HOME = path\dagster_home        #Ejemplo: \c\Users\Usuario\Documents\data-engineering\pipelines\dagster\dagster_home
DAGSTER_PG_USERNAME = usuario
DAGSTER_PG_PASSWORD = contraseña
DAGSTER_PG_HOST = host
DAGSTER_PG_DB = nombre_bd
DAGSTER_PG_PORT = puerto
```
Y tambien es necesario actualizar la información de la base de datos en el archivo _dagster.yaml_ situada en la carpeta en donde se declaró la variable de entorno **dagster_home**. Cambiar los siguientes valores:
```
postgres_db:
      username: postgres
      password: password
      hostname: localhost
      db_name: dagster
      port: 5432
```

Para ejecutar el script es necesario situarse en la carpeta raíz del proyecto y ejecutar la siguiente sentencia:

```
python ETL.py
```
O a través de dagit (IU) hay que ejecutar la siguiente sentencia:

```
dagit -f ETL.py
```
Y dentro del servidor en la pestaña de _launchpad_ presionar el boton _**launch run**_ y llevará a cabo el pipeline.

## Schedule

**Importante** 

Para el schedule de este pipeline es necesario correr el siguiente comando en una terminal y mantenerlo activo, el cual leera el archivo _dagster.yaml_
```
dagster-daemon run
```

Una vez activado el _daemon_, en otra terminal ejecutamos el comando:

```
dagit -f ETL.py
```

Dentro de la IU de dagit ingresamos revisamos el status y nos dirigiremos a _schedules_, una vez estemos dentro de la ruta, activamos el schedule _**update_warehouse_schedule**_ presionando el toogle
### Final
Ya que se activo esta funcionalidad, el pipeline se ejecutará cada 24hrs a las 2:00AM.

# Muestras
![dagster_schedule](https://user-images.githubusercontent.com/66045880/147633364-9383614e-25db-4542-8f56-5671b420343b.png)

![postgres_relations](https://user-images.githubusercontent.com/66045880/147635212-e310345e-b9c7-4287-894e-63a9bc5fdc15.png)

