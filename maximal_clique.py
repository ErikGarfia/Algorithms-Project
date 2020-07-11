from bron_kerbosch import IK
from reporter import Reporter
import matplotlib.pyplot as plt
import networkx as nx
 
 #funcion que recibe los nodos y sus relaciones
def maximal_clique(NODES,NEIGHBORS,datos):
	#mandamos a llamar al archivo reporter.py
	report = Reporter('## %s' % IK.__doc__)
	#enviamos los valores de los nodos y vertices
	IK([], set(NODES), set(), report, NEIGHBORS)
	#imprimimos el valor del maximo clique 
	report.print_report(datos)
	#Para poder graficarlo, una forma sencilla es transformar la lista del txt en un 
	#diccionario para poder trabajarlo
	#DICT lo transforma en diccionario
	#ZIP toma dos listas, la primera es la longitud y la segunda son los valores de la lista
	dictionary = dict(zip(range(len(NEIGHBORS)),NEIGHBORS))
	#obtenemos los valores del diccionario
	valores = dictionary.values()
	#obtenemos la clave del diccionario, recordando que el diccionario trabaja de forma clave-valor
	claves = dictionary.keys()
	#graficamos, pasando el diccionario como parametro
	g = nx.Graph(dictionary)
	pos = nx.spring_layout(g)
	values = []
	#coloreamos los nodos que conforman al maximo clique
	for node in list(g.nodes()):
		if node in report.cliques: 
			values.append('red')
		else: 
			values.append('skyblue')
	nx.draw(g,with_labels=True,
	node_color=values,
	node_shape="h",
	node_size=1000,
	edge_color="#1b5583",
	style="solid",
	font_weight="bold")
	#guardamos el grafo creado en un archivo png para consulta del usuario
	plt.savefig("GraficoMaximoClique.png")
	#mostramos el grafo creado
	plt.show()
