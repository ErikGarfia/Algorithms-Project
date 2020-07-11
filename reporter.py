import tkinter as tk

class Reporter(object):
    def __init__(self, name):
        #variable que se inicializan al ejecutar el programa
        self.name = name
        self.cnt = 0
        self.cliques = []
        self.tam = 0
    #este solo es el contador que va a manejar el tamaño de los nodos del txt
    def inc_count(self):
        self.cnt += 1
 
    def record(self, clique):
        #registra si el nodo pertenece al maximo clique o no
        if(len(clique) > self.tam):
            self.cliques = clique
            self.tam = len(clique)
 
    def print_report(self):
        #imprime las veces que recorre los nodos
        print(self.name)
        print('las llamadas realizadas en total son: %d' % self.cnt)
        print(self.cliques)


