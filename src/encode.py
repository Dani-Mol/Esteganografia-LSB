import math
import cv2
import numpy as np
from os import path

# Configuracion de extraccion de bits
bits = 2 # Numero de bits utilizados para ocultar cada parte del mensaje en los pixeles de la imagen
high_bits = 256 - (1 << bits) # Mascara de bits para obtener los bits bajos
low_bits = (1 << bits) - 1 # Mascara de bits bajos
bytes_por_bit = math.ceil(8 / bits) # Numero de bytes necesarios para representar cada caracter
bandera = "-" # Caracter que marca el fin de longitud del mensaje


def leer_mensaje_txt(ruta_txt):
    """
    Lee el mensaje desde un archivo de texto.

    Args:
        ruta_txt (str): Ruta del archivo de texto que contiene el mensaje a ocultar.

    Returns:
        str: El contenido del mensaje leido desde el archivo.
    """
    with open(ruta_txt, 'r', encoding='utf-8') as archivo:
        mensaje = archivo.read()
    return mensaje

def insertar_imagen(ruta_img, mensaje, ruta_salida):
    """
    Inserta un mensaje oculto en una imagen utilizando la tecnica LSB.

    Args:
        ruta_img (str): Ruta de la imagen de entrada donde se ocultara el mensaje.
        mensaje (str): Mensaje que se desea ocultar en la imagen.
        ruta_salida (str): Ruta de la imagen de salida con el mensaje oculto.

    Returns:
        str: La ruta de la imagen de salida generada con el mensaje oculto.

    Raises:
        ValueError: Si el tamaño del mensaje excede la capacidad de almacenamiento de la imagen.
    """
    imagen = cv2.imread(ruta_img, cv2.IMREAD_ANYCOLOR)
    dim_original = imagen.shape
    max_bytes_imagen = dim_original[0] * dim_original[1]  # Capacidad de bytes de la imagen
    msg = "{}{}{}".format(len(mensaje), bandera, mensaje)  # Mensaje con prefijo de la longitud y el marcador de fin

    # Verificacion de la capacidad de la imagen para almacenar el mensaje
    if max_bytes_imagen < len(mensaje):
        raise ValueError("El mensaje es más grande que la capacidad de la imagen, la cual es: {}".format(max_bytes_imagen))

    # Redimensionamiento de la imagen en una matriz unidimensional para la codificacion
    datos = np.reshape(imagen, -1)

    # Codificacion del mensaje en la imagen
    for (indice, val) in enumerate(msg):
        codificacion(datos[indice * bytes_por_bit: (indice + 1) * bytes_por_bit], val)

    # Reconstruccion y guardado de la imagen codificada
    imagen_codificada = np.reshape(datos, dim_original)
    cv2.imwrite(ruta_salida, imagen_codificada)

    return ruta_salida

def codificacion(bloque, caracter):
    """
    Codifica un caracter en un bloque de bytes de la imagen.

    Args:
        bloque (numpy.ndarray): Array de bytes de la imagen donde se almacenara el caracter.
        caracter (str): Caracter que se codificara en el bloque de la imagen.
    """
    caracter_bits = ord(caracter)  # Obtiene el valor ASCII del caracter
    # Divide el caracter en segmentos de bits segun el numero especificado
    valores_bit = np.array([(caracter_bits >> (bits * i)) & low_bits for i in range(len(bloque))], dtype=np.uint8)

    # Limpia los bits bajos en el bloque y los reemplaza con el caracter codificado
    bloque = np.asarray(bloque)
    bloque &= high_bits
    bloque |= valores_bit
