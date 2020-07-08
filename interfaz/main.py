import tkinter as ttk
from tkinter import *
from tkinter import filedialog
from functools import partial
import os
import Pmw, sys
from maximal_clique import *

class Aplicacion():

    def __init__(self):
        self.NEIGHBORS = []
        self.NODES = 0
#-  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
    def abrir_archivo(self,text):
    #obtenemos el directorio actual del usuario
        text.clear()
        directorio_actual= os.getcwd()
        archivo=filedialog.askopenfilename(initialdir = directorio_actual, title="Selecciona el archivo", filetypes= [("txt files","*.txt")])
        text.insert('end', open(archivo,'r').read())
#-  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
    def cargar_archivo(self,text):
        NEIGHBORS = self.NEIGHBORS
        NEIGHBORS = text.get().strip()
        NEIGHBORS = NEIGHBORS.split('\n')
        for i in range(len(NEIGHBORS)):
            NEIGHBORS[i] = "".join(NEIGHBORS[i])
            NEIGHBORS[i] = NEIGHBORS[i].replace('[','')
            NEIGHBORS[i] = NEIGHBORS[i].replace(']','')
            NEIGHBORS[i] = NEIGHBORS[i].split(',')
            for c in range(len(NEIGHBORS[i])):
                NEIGHBORS[i][c] = int(NEIGHBORS[i][c])
        self.NEIGHBORS = NEIGHBORS
        self.NODES = set(range(len(NEIGHBORS)))
        maximal_clique(self.NODES,self.NEIGHBORS)
#-  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
    def datos(self):
        print(self.NEIGHBORS)
        print(self.NODES)
#-  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
    def borrar_texto(self,text):
        text.clear()
#-  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -

if __name__ == '__main__':
    mi_app = Aplicacion()
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
    abrir = partial(mi_app.abrir_archivo, text)
    cargar = partial(mi_app.cargar_archivo, text)
    borrar = partial(mi_app.borrar_texto, text)
    ttk.Button(raiz, text='Cargar Archivo', command=abrir).place(x=80, y=180)
    ttk.Button(raiz, text='Enviar', command=cargar).place(x=240, y=180)
    ttk.Button(raiz, text='Datos', command=mi_app.datos).place(x=240, y=250)
    ttk.Button(raiz, text='Borrar datos', command=borrar).place(x=80, y=250)
    ttk.Button(raiz, text='Salir', command=raiz.destroy).place(x=360, y=180)
    raiz.mainloop()
