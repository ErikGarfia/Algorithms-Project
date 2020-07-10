from bron_kerbosch import IK
from reporter import Reporter
import matplotlib.pyplot as plt
import networkx as nx
 
 
def maximal_clique(NODES,NEIGHBORS):
	report = Reporter('## %s' % IK.__doc__)
	IK([], set(NODES), set(), report, NEIGHBORS) 
	report.print_report()
	#Para poder graficarlo, una forma sencilla es transforma la lista en un 
	#diccionario para poder trabajarlo
	#DICT lo transforma en diccionario
	#ZIP toma dos listas, la primera es la longitud y la segunda son los valores de la lista
	dictionary = dict(zip(range(len(NEIGHBORS)),NEIGHBORS))
	print(dictionary)
	print(type(dictionary))
	valores = dictionary.values()
	print(valores)
	claves = dictionary.keys()
	print(claves)
	g = nx.Graph(dictionary)
	pos = nx.spring_layout(g)
	values = []
	for node in list(g.nodes()):
		if node in report.cliques: 
			values.append('red') 
		else: 
			values.append('blue')
	nx.draw(g,with_labels=True,node_color=values)
	plt.savefig("GraficoMaximoClique.png")
	plt.show()
