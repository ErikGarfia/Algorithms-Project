""" 
PROYECTO FINAL: MÁXIMO CLIQUE
ANÁLISIS DE ALGORITMOS
AUTORES:    GARFIA ACEVEDO ERIK   &&   MEDERO LUJÁN ALEJANDRO
"""
#!Importamos las librerías necesarias para poder trabajar con la interfaz grafica
import tkinter as ttk
from tkinter import *
from tkinter import filedialog
from functools import partial
import matplotlib.pyplot as plt
from tkinter.ttk import *
import networkx as nx
import os
import Pmw
import sys
from maximal_clique import *



class Aplicacion():

    def __init__(self):
        #variables que ocuparemos, inicializadas
        self.NEIGHBORS = []
        self.NODES = 0

    #-  -   -   -   FUNCION ABRIR-  -   -   -   
    def abrir_archivo(self, text):
    # obtenemos el directorio actual del usuario para poder abrir la ventana de seleccionar el txt
        text.clear()
        directorio_actual = os.getcwd()
        archivo = filedialog.askopenfilename(
            initialdir=directorio_actual, title="Selecciona el archivo", filetypes=[("txt files", "*.txt")])
        text.insert('end', open(archivo, 'r').read())

    #-  -   -   -   FUNCION CARGAR-  -   -   -   
    def cargar_archivo(self, text):
        #obtenemos la variable inicializada al inicio, y trabajamos con el formato introducido del txt
        NEIGHBORS = self.NEIGHBORS
        NEIGHBORS = text.get().strip()
        NEIGHBORS = NEIGHBORS.split('\n')
        for i in range(len(NEIGHBORS)):
            NEIGHBORS[i] = "".join(NEIGHBORS[i])
            NEIGHBORS[i] = NEIGHBORS[i].replace('[', '')
            NEIGHBORS[i] = NEIGHBORS[i].replace(']', '')
            NEIGHBORS[i] = NEIGHBORS[i].split(',')
            for c in range(len(NEIGHBORS[i])):
                NEIGHBORS[i][c] = int(NEIGHBORS[i][c])
        self.NEIGHBORS = NEIGHBORS
        self.NODES = set(range(len(NEIGHBORS)))
        print(NEIGHBORS)
        print(type(NEIGHBORS))
        #mandamos a llamar al algoritmo que realizara el trabajo de buscar el maximo clique
        maximal_clique(self.NODES, self.NEIGHBORS)

    #-  -   -   -   FUNCION BORRAR-  -   -   -   
    def borrar_texto(self,text):
        text.clear()


#!Este ese el main, mandamos llamar a la funcion APLICACION
if __name__ == '__main__':
    mi_app = Aplicacion()
    
# Propiedades de la ventana principal, es la que aparece al principio
    raiz = Tk()
    raiz.geometry('400x240')
    raiz.configure(bg = '#3F8BBA')
    raiz.title('Máximo Clique')
# Esta es la parte donde aparece el texto del archivo txt, en donde se despliegan los datos
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
#-  -   -   -   -   -   -  SECCION DE LOS BOTONES-  -   -   -   -   -   -   -   -   
    text.place(x=18, y=20)
    abrir = partial(mi_app.abrir_archivo, text)
    cargar = partial(mi_app.cargar_archivo, text)
    borrar = partial(mi_app.borrar_texto, text)
    #-  -   -   -   BOTON CARGAR ARCHIVO-  -   -   -   
    ttk.Button(raiz,
    text='Cargar Archivo',
    bg="#3F8BBA",
    relief=FLAT,
    width=15,
    height=2,
    activebackground="white",
    fg="white",
    activeforeground="#3F8BBA",
    command=abrir).place(x=240, y=20)
    #-  -   -   -   BOTON ENVIAR  -   -   -   
    ttk.Button(raiz,
    text='Enviar',
    bg="#3F8BBA",
    width=15,
    height=2,
    activebackground="white",
    fg="white",
    activeforeground="#3F8BBA",
    relief=FLAT,
    command=cargar).place(x=240, y=119)
    #-  -   -   -   BOTON BORRAR-  -   -   -   
    ttk.Button(raiz,
    text='Borrar datos',
    width=15,
    height=2,
    activebackground="white",
    bg="#3F8BBA",
    activeforeground="#3F8BBA",
    fg="white",
    relief=FLAT,
    command=borrar).place(x=240, y=69)
    #-  -   -   -   BOTON SALIR  -   -   -   
    ttk.Button(raiz,
    text='Salir',
    bg="#3F8BBA",
    width=15,
    height=2,
    activeforeground="#3F8BBA",
    activebackground="white",
    fg="white",
    relief=FLAT,
    command=raiz.destroy).place(x=240, y=169)
    #-  -   -   -   EJECUTAMOS PARA MOSTRAR LA VENTANA PRINCIPAL-  -   -   -   
    raiz.mainloop()
