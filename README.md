# PROYECTO INDIVIDUAL Nº1
## Proyecto MLOps Engineer: 
***Recomendación de Contenido en Plataformas de Streaming***


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

