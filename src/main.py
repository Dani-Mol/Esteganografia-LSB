import sys
from encode import leer_mensaje_txt, insertar_imagen
from decode import extraccion, guardar_texto_en_txt
import os

def main():
    """
    Programa principal de esteganografia para ocultar y develar mensajes en imagenes.

    Este programa permite:
      - Ocultar un mensaje de texto en una imagen.
      - Develar un mensaje oculto desde una imagen.

    Uso:
        Para ocultar: python main.py h <archivo_texto> <imagen_entrada> [imagen_salida]
        Para develar: python main.py u <imagen_entrada_codificada> [archivo_texto_salida]
    """
    if len(sys.argv) < 3:
        print("Uso:")
        print("Para ocultar: python main.py h <archivo_texto> <imagen_entrada> [imagen_salida]")
        print("Para develar: python main.py u <imagen_entrada_codificada> [archivo_texto_salida]")
        sys.exit(1)
    
    opcion = sys.argv[1]
    
    if opcion == 'h':
        # Validacion de argumentos para la opcion "ocultar"
        if len(sys.argv) < 4:
            print("Uso para ocultar: python main.py h <archivo_texto> <imagen_entrada> [imagen_salida]")
            sys.exit(1)
        
        archivo_texto = sys.argv[2]
        imagen_entrada = sys.argv[3]
        
        # Nombre de archivo de salida para la imagen codificada
        if len(sys.argv) == 5:
            imagen_salida = sys.argv[4]
        else:
            nombre_base, _ = os.path.splitext(imagen_entrada)
            imagen_salida = f"{nombre_base}_codificada.png"
        
        # Verifica que el archivo de salida tiene una extension de imagen valida
        if not imagen_salida.lower().endswith(('.png', '.jpg', '.jpeg')):
            imagen_salida += '.png'
        
        # Lee el mensaje del archivo de texto y lo inserta en la imagen
        mensaje = leer_mensaje_txt(archivo_texto)
        
        try:
            img_codificada = insertar_imagen(imagen_entrada, mensaje, imagen_salida)
            if img_codificada:
                print("Imagen codificada guardada como:", imagen_salida)
        except ValueError as e:
            print("Error:", e)
    
    elif opcion == 'u':
        # Validacion de argumentos para la opcion 'develar'
        if len(sys.argv) < 3:
            print("Uso para develar: python main.py u <imagen_entrada_codificada> [archivo_texto_salida]")
            sys.exit(1)
        
        imagen_codificada = sys.argv[2]
        
        # Nombre de archivo de salida para el mensaje extraido
        if len(sys.argv) == 4:
            archivo_texto_salida = sys.argv[3]
        else:
            archivo_texto_salida = "mensaje_oculto.txt"
        
        # Asegura que el archivo de salida tiene una extensión .txt
        if not archivo_texto_salida.lower().endswith('.txt'):
            archivo_texto_salida += '.txt'
        
        # Extrae el mensaje de la imagen codificada y lo guarda en el archivo de texto
        try:
            mensaje = extraccion(imagen_codificada)
            guardar_texto_en_txt(mensaje, archivo_texto_salida)
            print("Mensaje oculto extraido y guardado en:", archivo_texto_salida)
        except ValueError as e:
            print("Error:", e)
    else:
        print("Opción no válida. Usa 'h' para ocultar o 'u' para develar.")

if __name__ == '__main__':
    main()
