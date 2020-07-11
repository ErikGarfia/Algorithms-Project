class Reporter(object):
#Constructor de la clase
    def __init__(self, name):
        self.name = name
        self.cnt = 0
        self.cliques = []
        self.tam = 0
 #Cuenta el nùmero de recursiones totales
    def inc_count(self):
        self.cnt += 1
 #Guarda el màximo clique
    def record(self, clique):
        if(len(clique) > self.tam):
            self.cliques = clique
            self.tam = len(clique)
 #Imprime los datos
    def print_report(self,datos):
        datos.settext(self.cliques)
        print(self.name)
        print('llamadas recursivas realizadas en total son: %d' % self.cnt)
        print(self.cliques)

