# Proyecto de Esteganografía en Imágenes

## Descripción
Este proyecto utiliza la técnica de esteganografía de bits menos significativos (LSB) para ocultar y extraer mensajes de texto en imágenes. Permite al usuario insertar un mensaje secreto en una imagen y recuperarlo posteriormente utilizando métodos robustos y configurables. Los mensajes se almacenan en los bits de menor significancia de cada píxel, preservando la calidad visual de la imagen.

## Estructura del Proyecto

- `main.py`: Controlador principal que permite ocultar y extraer mensajes desde la línea de comandos.
- `encode.py`: Contiene las funciones necesarias para leer el mensaje desde un archivo de texto y almacenarlo en una imagen.
- `decode.py`: Contiene las funciones para extraer el mensaje de una imagen y guardarlo en un archivo de texto.

## Requisitos

- Python 3.x
- Bibliotecas:
  - `opencv-python` (para manipulación de imágenes)
  - `numpy` (para procesamiento de datos)
- Sistema operativo compatible (Windows, macOS, Linux)

### Instalación


Clonar repositorio

```
git clone https://github.com/Dani-Mol/Esteganografia-LSB.git
cd Esteganografia-LSB
```

Instala las dependencias utilizando `pip`:

```
pip install opencv-python 
pip install numpy
```

## Uso

### Sintaxis

```
python main.py <opcion> <argumentos>
```

### Opciones

1. **Ocultar un mensaje en una imagen (`h`)**
   
   ```
   python main.py h <archivo_texto> <imagen_entrada> [imagen_salida]
   ```
   - `archivo_texto`: Ruta del archivo de texto que contiene el mensaje a ocultar.
   - `imagen_entrada`: Ruta de la imagen en la que se ocultará el mensaje.
   - `imagen_salida` (opcional): Nombre de la imagen de salida que contendrá el mensaje oculto. Si no se especifica, el nombre será `<nombre_imagen_entrada>_codificada.png`.

2. **Extraer un mensaje oculto de una imagen (`u`)**
   
   ```
   python main.py u <imagen_entrada_codificada> [archivo_texto_salida]
   ```
   - `imagen_entrada_codificada`: Ruta de la imagen que contiene el mensaje oculto.
   - `archivo_texto_salida` (opcional): Nombre del archivo donde se guardará el mensaje extraído. Si no se especifica, el nombre por defecto será `mensaje_oculto.txt`.

### Ejemplos

1. **Ocultar un mensaje en una imagen**

   ```
   python main.py h mensaje.txt imagen.png imagen_codificada.png
   ```

   Este comando oculta el contenido de `mensaje.txt` en `imagen.png` y guarda el resultado en `imagen_codificada.png`.

2. **Extraer un mensaje oculto de una imagen**

   ```
   python main.py u imagen_codificada.png mensaje_extraido.txt
   ```

   Este comando extrae el mensaje oculto de `imagen_codificada.png` y lo guarda en `mensaje_extraido.txt`.

## Descripción Técnica de los Archivos

### `main.py`

Este archivo actúa como la interfaz principal para el usuario, permitiéndole ejecutar las funciones de esteganografía a través de opciones en la línea de comandos.

- **Funciones clave**:
  - `main()`: Gestiona la ejecución del programa según la opción elegida (ocultar o develar).
  - Verifica los argumentos y gestiona los errores de capacidad y de archivo.
  
### `encode.py`

Contiene las funciones necesarias para leer y ocultar mensajes en una imagen.

- **Funciones clave**:
  - `leer_mensaje_txt(ruta_txt)`: Lee el mensaje desde un archivo de texto.
  - `insertar_imagen(ruta_img, mensaje, ruta_salida)`: Oculta el mensaje en la imagen de entrada y guarda el resultado en la imagen de salida.
  - `codificacion(bloque, caracter)`: Codifica cada carácter del mensaje en los píxeles de la imagen usando la técnica LSB.

### `decode.py`

Proporciona las funciones necesarias para extraer y guardar mensajes desde una imagen codificada.

- **Funciones clave**:
  - `extraccion(ruta)`: Extrae el mensaje oculto de una imagen codificada.
  - `guardar_texto_en_txt(texto, ruta_salida)`: Guarda el mensaje extraído en un archivo de texto.

## Ejecución y Errores Comunes

1. **Error: El mensaje es más grande que la capacidad de la imagen**
   - La imagen debe tener una capacidad suficiente para almacenar el mensaje. Si el mensaje es muy grande, utilice una imagen de mayor resolución o reduzca el tamaño del mensaje.

2. **Error: No se encontró un mensaje oculto en la imagen**
   - Esto indica que la imagen no contiene un mensaje oculto o que la codificación fue alterada.

3. **Error: No se pudo interpretar la longitud del mensaje oculto**
   - Puede ocurrir si la imagen fue manipulada después de ocultar el mensaje.


## Consideraciones de Seguridad

Este método no proporciona encriptación, por lo que cualquier persona que conozca el método LSB y tenga acceso al script puede extraer el mensaje. Para mayor seguridad, se recomienda aplicar un cifrado adicional al mensaje antes de ocultarlo en la imagen.

## Licencia

Este proyecto está disponible bajo la licencia MIT.