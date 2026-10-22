
# WriteUp CTF: Hidden Flag

## 1. Encontré los dos archivos públicos

Ingresé a la página web y exploré los documentos disponibles. Encontré dos archivos para descargar: `welcome.txt` e `incident_report.txt`.

Al leer el informe de incidentes, descubrí una pista que indicaba que algunos archivos históricos podían no aparecer en el índice público y que la rotación de backups estaba pendiente.

Esto me hizo sospechar que podía existir un archivo oculto que contuviera información importante.

## 2. Busqué el archivo robots.txt

Investigué el archivo `robots.txt`, accediendo a la siguiente ruta:

```text
/robots.txt
```

Encontré el siguiente contenido:

```text
User-agent: *
Disallow: /backup/
Disallow: /download
```

La línea `Disallow: /backup/` llamó mi atención, ya que indicaba una ruta relacionada con copias de seguridad.

Aunque `robots.txt` no protege los archivos, puede proporcionar pistas sobre rutas interesantes que conviene investigar.

## 3. Analicé el sistema de descargas

Observé cómo se descargaban los documentos públicos y encontré el endpoint `/download`, que recibía un parámetro llamado `file`.

Por ejemplo:

```text
/download?file=welcome.txt
```

Esto me permitió deducir que el servidor utilizaba el valor del parámetro `file` para determinar qué archivo debía descargar.

Entonces, me planteé si era posible modificar ese parámetro para acceder a archivos ubicados fuera del directorio público.

## 4. Encontré la ruta al backup oculto

Investigué la posibilidad de explotar una vulnerabilidad de **Path Traversal**.

Esta vulnerabilidad se produce cuando una aplicación permite manipular las rutas de los archivos sin comprobar correctamente que permanezcan dentro del directorio autorizado.

El elemento clave es `../`, que permite subir un nivel en la estructura de directorios.

Al combinar esta técnica con la información obtenida anteriormente, probé la siguiente ruta:

```text
/download?file=../backup/old_backup.txt
```

La solicitud funcionó y pude descargar el archivo `old_backup.txt`, que no aparecía entre los documentos públicos.

## 5. Encontré la flag cifrada

Abrí el archivo `old_backup.txt` y encontré el siguiente contenido:

```text
// LEGACY BACKUP

Recovery token: synt{cngu_genirefny_ebg13}
```

El archivo indicaba que el token estaba cifrado mediante ROT13, una variante del cifrado César que desplaza cada letra 13 posiciones en el alfabeto.

Por lo tanto, todavía debía descifrar el texto para obtener la flag original.

## 6. Descifré el token con ROT13

Utilicé Python para descifrar el token:

```python
import codecs

token = "synt{cngu_genirefny_ebg13}"
flag = codecs.decode(token, "rot_13")

print(flag)
```

El resultado fue:

```text
flag{path_traversal_rot13}
```

De esta manera, obtuve la flag final del desafío.

## Conclusión

Para resolver este CTF, comencé explorando los archivos públicos de la web y encontré pistas sobre la existencia de copias de seguridad. Después, consulté `robots.txt` y descubrí la ruta `/backup/`. Al analizar el endpoint de descarga, identifiqué que el parámetro `file` podía manipularse para acceder a archivos fuera del directorio público, lo que me permitió explotar una vulnerabilidad de Path Traversal y recuperar el backup oculto. Finalmente, apliqué ROT13 al token encontrado y obtuve la flag `flag{path_traversal_rot13}`.
