import sys
from encode import leer_mensaje_txt, insertar_imagen
from decode import extraccion, guardar_texto_en_txt
import os

def main():
    if len(sys.argv) < 3:
        print("Uso:")
        print("Para ocultar: python main.py h <archivo_texto> <imagen_entrada> [imagen_salida]")
        print("Para develar: python main.py u <imagen_entrada_codificada> [archivo_texto_salida]")
        sys.exit(1)
    
    opcion = sys.argv[1]
    
    if opcion == 'h':
        if len(sys.argv) < 4:
            print("Uso para ocultar: python main.py h <archivo_texto> <imagen_entrada> [imagen_salida]")
            sys.exit(1)
        
        archivo_texto = sys.argv[2]
        imagen_entrada = sys.argv[3]
        
        if len(sys.argv) == 5:
            imagen_salida = sys.argv[4]
        else:
            nombre_base, _ = os.path.splitext(imagen_entrada)
            imagen_salida = f"{nombre_base}_codificada.png"
        
        if not imagen_salida.lower().endswith(('.png', '.jpg', '.jpeg')):
            imagen_salida += '.png'
        
        mensaje = leer_mensaje_txt(archivo_texto)
        
        try:
            img_codificada = insertar_imagen(imagen_entrada, mensaje, imagen_salida)
            if img_codificada:
                print("Imagen codificada guardada como:", imagen_salida)
        except ValueError as e:
            print("Error:", e)
    
    elif opcion == 'u':
        if len(sys.argv) < 3:
            print("Uso para develar: python main.py u <imagen_entrada_codificada> [archivo_texto_salida]")
            sys.exit(1)
        
        imagen_codificada = sys.argv[2]
        
        if len(sys.argv) == 4:
            archivo_texto_salida = sys.argv[3]
        else:
            archivo_texto_salida = "mensaje_oculto.txt"
        
        if not archivo_texto_salida.lower().endswith('.txt'):
            archivo_texto_salida += '.txt'
        
        try:
            mensaje = extraccion(imagen_codificada)
            guardar_texto_en_txt(mensaje, archivo_texto_salida)
            print("Mensaje oculto extraído y guardado en:", archivo_texto_salida)
        except ValueError as e:
            print("Error:", e)
    else:
        print("Opción no válida. Usa 'h' para ocultar o 'u' para develar.")

if __name__ == '__main__':
    main()
