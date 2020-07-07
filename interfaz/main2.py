import tkinter as ttk
from tkinter import *
from tkinter import filedialog
from functools import partial
import os
import Pmw, sys


class Aplicacion:

    def __init__(self):
        NEIGHBORS = []
        NODES = 0

    def abrir_archivo(text):
    #obtenemos el directorio actual del usuario
        text.clear()
        directorio_actual= os.getcwd()
        archivo=filedialog.askopenfilename(initialdir = directorio_actual, title="Selecciona el archivo", filetypes= [("txt files","*.txt")])
        text.insert('end', open(archivo,'r').read())
#-  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
    def cargar_archivo(text):
        NEIGHBORS = text.get().strip()
        NEIGHBORS = NEIGHBORS.split('\n')
        NODES = set(range(1, len(NEIGHBORS)))
        print(NEIGHBORS)
        print(NODES)
#-  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
    def borrar_texto(text):
        text.clear()
#-  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
#Propiedades de la ventana principal.
    raiz = Tk()
    raiz.geometry('500x400')
    raiz.configure(bg = 'beige')
    raiz.title('Maximo Clique')
#Esta es la parte donde aparece el texto del archivo txt
    text = Pmw.ScrolledText(
    borderframe=0,
    vscrollmode='dynamic',
    hscrollmode='dynamic',
    labelpos='n',
    label_text='datos.txt',
    text_width=20,
    text_height=4,
    text_wrap='none',
    )
    text.place(x=18, y=20)
    abrir = partial(abrir_archivo, text)
    cargar = partial(cargar_archivo, text)
    borrar = partial(borrar_texto, text)
    ttk.Button(raiz, text='Cargar Archivo', command=abrir).place(x=80, y=180)
    ttk.Button(raiz, text='Enviar', command=cargar).place(x=240, y=180)
    ttk.Button(raiz, text='Borrar datos', command=borrar).place(x=80, y=250)
    ttk.Button(raiz, text='Salir', command=raiz.destroy).place(x=360, y=180)
    raiz.mainloop()
#-  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
# Define la función main() 
def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()
