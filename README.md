# PyEPH Data

Almacenamiento estandarizado de las bases de microdatos de las Encuesta Permanante de Hogares publicadas por INDEC y el resto de las bases de datos necesarias para el tratamiento de las EPH. 

## Obtener nuevos microdatos

Para obtener nuevos periodos publicados hay que ejecutar el archivo `getter.py` y pasarle como argumento la dirección del archivo `txt` que provee indec. 

```bash
python getter.py <URI_TXT>
```

Esto ejecuta todo el procesamiento hasta dejar listas las bases en sus carpetas pertinentes (individual y hogar). Luego hay que hacer un commit y enviar. Y Listo!

## Breve descripción

En este repositorio se albergan:
- Las bases de datos de las EPH de 1996 en adelante
- Diccionario de aglomerados y regiones de las EPH
- La serie de tiempo de la Canasta Básica Alimentaria (CBA) y Canasta Básica Total (CBT) regional
- La tabla de valores de adulto equivalente por sexo y edad
- La tabla de Clasificación de Actividades Económicas para Encuestas Sociodemográficas (CAES)
- La tabla de Clasificación Nacional de Ocupaciones (CNO)

### Microdatos de Encuesta Permanentes de Hogares

#### EPH Puntual

> Desde 1995 a mayo 2003 INDEC publica la "Base Usuaria Ampliada (BUA) EPH Puntual" de cada aglomerado por separado y también la base del Total de Aglomerados (desde mayo 1999). 

Vale mencionar que a partir de octubre de 2003 solo se realiza relevamiento puntual para Rawson-Trelew, San Nicolás-Villa Constitución y Viedma-Carmen de Patagones hasta mayo 2006. La EPH Puntual se realiza con una período de modalidad puntual en dos ondas anuales (mayo y octubre).

Dado que las bases de datos se publicaron separadas por aglomerado, se recurrió a juntar las mismas, creando una base de datos completa que incluye información sobre cada aglomerado y sobre el total de aglomerados. Estas bases completas fueron generadas por el [Instituto Humai](https://ihum.ai/).


Fuente: https://www.indec.gob.ar/indec/web/Institucional-Indec-bases_de_datos_eph_amp


#### EPH Continua

> Desde el año 2003 al 2007, se publican las bases de datos trimestrales y semestrales de las EPH continua de personas y hogares en formato DBF.

Bases trimestrales: del tercer trimestre de 2003 al primer trimestre de 2007

Bases semestrales: del segundo semestre de 2003 al segundo semestre de 2006

Estas bases de datos fueron homogeneizadas y recopiladas por [Instituto Humai](https://ihum.ai/).

Fuente: https://www.indec.gob.ar/indec/web/Institucional-Indec-bases_de_datos_eph_buc

#### EPH

> Desde el año 2003 al 2015, se publican las bases REDATAM de las EPH individual y de hogar en formato: SPSS, Stata, DBF.



> Desde el año 2016 al 2021, se publican las bases de microdatos de las EPH individual y de hogar en formato: txt y xls.

Fuente: https://www.indec.gob.ar/indec/web/Institucional-Indec-BasesDeDatos

## Especificaciones de nombre

estandarizando el nombre para la facil obtencion y manipulacion de los datos en la libreria pyeph

base_{base_type}_{year}_{freq}_{period}.csv 


* desde 2004 hasta 2016 no hay 4° trimestre