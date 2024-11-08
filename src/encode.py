import math
import cv2
import numpy as np
from os import path


bits = 2 
high_bits = 256 - (1 << bits) 
low_bits = (1 << bits) - 1
bytes_por_bit = math.ceil(8 / bits) 
bandera = "-" 


def leer_mensaje_txt(ruta_txt):

    with open(ruta_txt, 'r', encoding='utf-8') as archivo:
        mensaje = archivo.read()
    return mensaje


def insertar_imagen(ruta_img, mensaje, ruta_salida):

    imagen = cv2.imread(ruta_img, cv2.IMREAD_ANYCOLOR)
    dim_original = imagen.shape
    max_bytes_imagen = dim_original[0] * dim_original[1] 
    msg = "{}{}{}".format(len(mensaje), bandera, mensaje)
    
    try:
        if max_bytes_imagen < len(mensaje):
            raise ValueError("El mensaje es mas grande que la capacidad de la imagen la cual es: {}".format(max_bytes_imagen))
    except ValueError as e:
        print("Error:", e)
    
    datos = np.reshape(imagen, -1)
    
    for (indice, val) in enumerate(msg):
        codificacion(datos[indice * bytes_por_bit: (indice + 1) * bytes_por_bit], val)

    imagen_codificada = np.reshape(datos, dim_original)
    cv2.imwrite(ruta_salida, imagen_codificada)

    return ruta_salida

    

def codificacion(bloque, caracter):
    
    caracter_bits = ord(caracter)
    valores_bit = np.array([(caracter_bits >> (bits * i)) & low_bits for i in range(len(bloque))], dtype=np.uint8)
    bloque = np.asarray(bloque)
    bloque &= high_bits
    bloque |= valores_bit
 
