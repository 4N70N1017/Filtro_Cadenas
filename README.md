# Filtro_Cadenas

El script busquedaHuella.py busca una cadena de texto específica dentro de todos los archivos de un directorio y sus subdirectorios, excluyendo el propio script y los archivos con extensión `.bal`.

**Funcionamiento:**
1. **Argumentos:**  
   - Puedes indicar el directorio a buscar (por defecto, el actual).
   - Puedes indicar la cadena a buscar (por defecto, `"he.exe"`).

2. **Recorrido:**  
   - Recorre todos los archivos del directorio y subdirectorios.
   - Ignora el propio script y archivos `.bal`.

3. **Búsqueda:**  
   - Abre cada archivo y busca línea por línea la cadena indicada.
   - Si la encuentra, muestra el archivo, el número de línea y la línea donde aparece.

4. **Salida:**  
   - Si no encuentra la cadena en ningún archivo, lo indica al final.

**Uso en terminal:**
```bash
python busquedaHuella.py /ruta/del/directorio -s "cadena_a_buscar"
```


**Requisitos**
--Instalar python3 : npm i python3


