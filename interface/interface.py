from tkinter import *
from tkinter import filedialog  
import tkinter as tk     
from PIL import Image, ImageTk
import os

# Para que aparezca el recuadro 

root = Tk()
root.title("Esteganografia")
root.geometry("700x500+150+180")
root.resizable(False, False)
root.configure(bg = "#2f4155")

#icono de la paginas
icono_path = os.path.join(os.path.dirname(__file__), "images-interface/wise.png")
icono = PhotoImage(file = icono_path)
root.iconphoto(False, icono)


root.mainloop()