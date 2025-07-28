# Filtro_Cadenas

El script `busquedaHuella.py` busca una cadena de texto específica dentro de todos los archivos de un directorio y sus subdirectorios, excluyendo el propio script y los archivos con extensión `.bal`.

## Funcionamiento

1. **Argumentos:**
   - Puedes indicar el directorio a buscar (por defecto, el actual).
   - Puedes indicar la cadena a buscar (por defecto, `"he.exe"`).
   - Puedes indicar el nombre del archivo de salida JSON (por defecto, `resultados.json`).

2. **Recorrido:**
   - Recorre todos los archivos del directorio y subdirectorios.
   - Ignora el propio script y archivos `.bal`.

3. **Búsqueda:**
   - Abre cada archivo y busca línea por línea la cadena indicada.
   - Si la encuentra, guarda el archivo, el número de línea y el contenido de la línea.

4. **Salida:**
   - Los resultados se guardan en un archivo JSON en la carpeta raíz donde está el script, sin importar desde dónde lo ejecutes.
   - También muestra los resultados en formato JSON en la terminal.

5. **Excepciones:**
   - Si no encuentra la cadena en ningún archivo, el archivo JSON contendrá una lista vacía `[]`.

## Uso en terminal

```bash
python3 /ruta/del/script/busquedaHuella.py /Ruta/Del/Directorio -s "Cadena_Busqueda" -o nombre_archivo.json
```

- El parámetro `-o` es opcional y permite definir el nombre del archivo de salida JSON.
- El archivo JSON siempre se guarda en la carpeta donde está el script.

## Ejemplo de salida en JSON

```json
[
  {
    "file": "/ruta/del/directorio/archivo.txt",
    "line": 42,
    "content": "Texto encontrado con la cadena buscada"
  }
]
```

## Requisitos

- Instalar Python 3

```bash
sudo apt-get install python3
```