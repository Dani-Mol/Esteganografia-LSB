import math
import cv2
import numpy as np

# Configuracion de extraccion de bits
bits = 2  # Numero de bits utilizados para ocultar cada parte del mensaje en los pixeles de la imagen
low_bits = (1 << bits) - 1  # Mascara de bits para obtener los bits bajos
bytes_por_bit = math.ceil(8 / bits)  # Numero de bytes necesarios para representar cada caracter
bandera = "-"  # Caracter que marca el fin de longitud del mensaje

def extraccion(ruta):
    """
    Extrae el mensaje oculto en una imagen utilizando la tecnica LSB (Least Significant Bit).

    Args:
        ruta (str): Ruta del archivo de imagen que contiene el mensaje oculto.

    Returns:
        str: El mensaje oculto extraido de la imagen.

    Raises:
        ValueError: Si no se encuentra un mensaje oculto, si la longitud del mensaje no puede ser interpretada, 
                    o si la imagen no tiene suficiente capacidad para el mensaje.
    """
    # Cargar la imagen en formato de cualquier color (permitido por la biblioteca)
    imagen = cv2.imread(ruta, cv2.IMREAD_ANYCOLOR)
    datos = np.reshape(imagen, -1)  # Convierte la imagen en una matriz unidimensional
    total = datos.shape[0]  # Total de bytes disponibles en la imagen

    long_mensaje = ""  # Inicializa la longitud del mensaje como una cadena vacia
    indice = 0  # Indice para recorrer los datos de la imagen

    # Extraer la longitud del mensaje
    while indice < total // bytes_por_bit:
        caracter = decodificacion(datos[indice * bytes_por_bit: (indice + 1) * bytes_por_bit])
        indice += 1
        if caracter != bandera:
            long_mensaje += caracter
        else:
            break

    if not long_mensaje:
        raise ValueError("No se encontró un mensaje oculto en la imagen.")

    try:
        longitud_mensaje = int(long_mensaje)
    except ValueError:
        raise ValueError("No se pudo interpretar la longitud del mensaje oculto.")

    if longitud_mensaje + indice > total // bytes_por_bit:
        raise ValueError(f"La imagen no tiene suficiente capacidad para el mensaje. Capacidad: {total // bytes_por_bit}, requerido: {long_mensaje + indice}")

    # Extraer el mensaje oculto en la imagen
    end = longitud_mensaje + indice
    texto_secreto = ""

    while indice < end:
        texto_secreto += decodificacion(datos[indice * bytes_por_bit: (indice + 1) * bytes_por_bit])
        indice += 1

    return texto_secreto

def decodificacion(bloque):
    """
    Decodifica un bloque de datos para recuperar un caracter oculto.

    Args:
        bloque (numpy.ndarray): Array de bytes representando los bits que contienen el caracter codificado.

    Returns:
        str: El caracter recuperado del bloque de datos.
    """
    val = np.bitwise_or.reduce((bloque & low_bits) << (np.arange(len(bloque)) * bits))
    return chr(val)

def guardar_texto_en_txt(texto, ruta_salida):
    """
    Guarda el mensaje extraido en un archivo de texto.

    Args:
        texto (str): El mensaje a guardar en el archivo de texto.
        ruta_salida (str): Ruta de destino para el archivo de texto donde se almacenara el mensaje.

    Raises:
        IOError: Si ocurre un error al intentar escribir en el archivo de salida.
    """
    with open(ruta_salida, "w", encoding="utf-8") as archivo:
        archivo.write(texto)
    print(f"El mensaje oculto ha sido guardado en {ruta_salida}.")
