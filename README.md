# PROYECTO INDIVIDUAL Nº1
## Proyecto MLOps Engineer: 
***Recomendación de Contenido en Plataformas de Streaming***


## Descripción del proyecto
El proyecto utiliza técnicas de procesamiento del lenguaje natural (NLP) y aprendizaje automático para analizar la información de los usuarios y los datos del contenido disponible en las plataformas de streaming. A partir de estos datos, se construye un modelo de recomendación que sugiere contenido específico para cada usuario.
## Características del Repositorio
### ETL
Algunos campos, como belongs_to_collection, production_companies y otros (ver diccionario de datos) están anidados, esto es o bien tienen un diccionario o una lista como valores en cada fila, ¡deberán desanidarlos para poder y unirlos al dataset de nuevo hacer alguna de las consultas de la API! O bien buscar la manera de acceder a esos datos sin desanidarlos.

Los valores nulos de los campos revenue, budget deben ser rellenados por el número 0.

Los valores nulos del campo release date deben eliminarse.

De haber fechas, deberán tener el formato AAAA-mm-dd, además deberán crear la columna release_year donde extraerán el año de la fecha de estreno.

Crear la columna con el retorno de inversión, llamada return con los campos revenue y budget, dividiendo estas dos últimas revenue / budget, cuando no hay datos disponibles para calcularlo, deberá tomar el valor 0.

Eliminar las columnas que no serán utilizadas, video,imdb_id,adult,original_title,poster_path y homepage.

