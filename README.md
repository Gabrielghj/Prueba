# PROYECTO INDIVIDUAL Nº1

## Proyecto MLOps Engineer: 
>***Recomendación de Contenido en Plataformas de Streaming***


## Descripción del proyecto
El proyecto utiliza técnicas de procesamiento del lenguaje natural (NLP) y aprendizaje automático para analizar la información de los usuarios y los datos del contenido disponible en las plataformas de streaming. A partir de estos datos, se construye un modelo de recomendación que sugiere contenido específico para cada usuario.
## Características del Repositorio
### ETL
+ Se desanidaron los campos belongs_to_collection, production_companies, genres, production_countries, spoken_languages. 

+ Los valores nulos de los campos revenue, budget deben ser rellenaron con el número 0.

+ Los valores nulos del campo release se eliminaron.

+ A las fechas se le dio el formato AAAA-mm-dd. Se creó la columna release_year donde se extrajo el año de la fecha de estreno.

+ Se creó la columna con el retorno de inversión, llamada return, dividiendo los campos revenue / budget, cuando no hay datos disponibles para calcularlo, se tomó el valor 0.

+ Se eliminaron las columnas que no serán utilizadas, video,imdb_id,adult,original_title,poster_path y homepage.

  ***El ETL en google colab se puede obtener Aquí***

### EDA
El análisis exploratorio de datos se lleva a cabo utilizando los cuadernos de google colab. Estos cuadernos contienen visualizaciones y estadísticas descriptivas que permiten comprender mejor los datos disponibles.

Algunas de las conclusiones del análisis exploratorio de datos son las siguientes:

**Budget (Presupuesto):**
+ El promedio del presupuesto de las películas es de aproximadamente 4.2 millones de dólares.
+ Hay una gran variabilidad en los presupuestos de las películas.
+ El 25% de las películas tienen un presupuesto desconocido o no tienen presupuesto registrado

**Revenue (Ingresos):**
+ El promedio de los ingresos de las películas es de aproximadamente 11.2 millones de dólares.
+ Hay una gran variabilidad en los ingresos de las películas.
+ El 25% de las películas  no generaron ingresos o no tienen información registrada.

**Runtime (Duración):**
+ La duración promedio de las películas es de aproximadamente 94 minutos.
+ El 50% de las películas tienen una duración de 95 minutos.

**Vote Average (Calificación promedio):**
+ La calificación promedio de las películas es de aproximadamente 5.6.
+ Hay una variabilidad moderada en las calificaciones de las películas.
+ El 25% de las películas tienen una calificación de 5.

**Return (Retorno):**
+ El promedio del retorno de las películas es de aproximadamente 660,042.8 dólares.
+ El valor mínimo es 0, lo que sugiere que algunas películas no tuvieron retorno o no tienen información registrada.
+ El 25% de las películas no tuvieron retorno o no tienen información registrada.

**Otras coclusiones:**
+ El 90.11% de las películas no pertenecen a una colección.
+ Hay una correlación positiva fuerte entre el presupuesto y los ingresos de las películas.

 ***El EDA en google colab se puede obtener Aquí***

## Endpoints
PELICULAS POR IDIOMA
+ Se ingresa un idioma (como están escritos en el dataset)y devuelve la cantidad de películas producidas en ese idioma.
                    
PELICULAS POR DURACION
+ Se ingresa una pelicula y devuelve la duracion y el año.

PELICULAS POR FRANQUICIA
+ Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio
                    
PELICULAS POR PAIS
+ Se ingresa un país (como están escritos en el dataset) y retorna la cantidad de peliculas producidas en el mismo.

PELICULAS POR PRODUCTORA EXITOSA
+ Se ingresa la productora, Y entrega el revunue total y la cantidad de peliculas que realizo.
                    



