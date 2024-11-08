import math
import cv2
import numpy as np


bits = 2
low_bits = (1 << bits) - 1
bytes_por_bit = math.ceil(8 / bits)
bandera = "-"


def extraccion(ruta):
    
    imagen = cv2.imread(ruta, cv2.IMREAD_ANYCOLOR)
    datos = np.reshape(imagen, -1)
    total = datos.shape[0]
    
    long_mensaje = ""
    indice = 0
    
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
        raise ValueError(f"La imagen no tiene suficiente capacidad para el mensaje. Capacidad: {total // bytes_por_bit}, requerido: {longitud_mensaje + indice}")
    
    end = longitud_mensaje + indice
    texto_secreto = ""

    while indice < end:
        texto_secreto += decodificacion(datos[indice * bytes_por_bit: (indice + 1) * bytes_por_bit])
        indice += 1

    return texto_secreto


def decodificacion(bloque):

    val = np.bitwise_or.reduce(
        (bloque & low_bits) << (np.arange(len(bloque)) * bits))
    return chr(val)


def guardar_texto_en_txt(texto, ruta_salida):

    with open(ruta_salida, "w", encoding="utf-8") as archivo:
        archivo.write(texto)
    print(f"El mensaje oculto ha sido guardado en {ruta_salida}.")

