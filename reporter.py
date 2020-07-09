class Reporter(object):
    def __init__(self, name):
        self.name = name
        self.cnt = 0
        self.cliques = []
        self.tam = 0
 
    def inc_count(self):
        self.cnt += 1
 
    def record(self, clique):
        if(len(clique) > self.tam):
            self.cliques = clique
            self.tam = len(clique)
 
    def print_report(self):
        print(self.name)
        print('llamadas recursivas realizadas en total son: %d' % self.cnt)
        print(self.cliques)


