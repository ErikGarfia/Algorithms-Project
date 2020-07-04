import tkinter as ttk
from tkinter import *
from tkinter import filedialog
import os
import Pmw, sys


class Aplicacion():

    def abrir_archivo():
        #obtenemos el directorio actual del usuario
        directorio_actual= os.getcwd()
        archivo=filedialog.askopenfilename(initialdir = directorio_actual, title="Selecciona el archivo", filetypes= [("txt files","*.txt")])
#-  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  
# #Esta es la parte donde aparece el texto del archivo txt 
        text = Pmw.ScrolledText(
        borderframe=0, 
        vscrollmode='dynamic', 
        hscrollmode='dynamic',
        labelpos='n', 
        label_text='file %s' % archivo,
        text_width=20, 
        text_height=4,
        text_wrap='none',
       )
        text.place(x=18, y=20)
        text.insert('end', open(archivo,'r').read())
#-  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   
#-  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
#Propiedades de la ventana principal.
    raiz = Tk()
    raiz.geometry('500x400')
    raiz.configure(bg = 'beige')
    raiz.title('Maximo Clique')
    ttk.Button(raiz, text='Cargar Archivo', command=abrir_archivo).place(x=80, y=180)
    ttk.Button(raiz, text='Enviar', command=raiz.destroy).place(x=240, y=180)
    ttk.Button(raiz, text='Salir', command=raiz.destroy).place(x=360, y=180)
    raiz.mainloop()
#-  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
# Define la función main() 
def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()