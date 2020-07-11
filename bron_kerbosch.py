def IK(clique, candidates, excluded, reporter,NEIGHBORS):
    #algoritmo principal, determina si el nodo pertenece al maximo clique o no
    '''Bron–Kerbosch algorithm with pivot'''
    #Suma 1 al total de llamadas recursivas
    reporter.inc_count()
    #Verifica si hay nodos en candidates o en excluded  
    #Si no hay màs nodos entonces reporta el clique
    if not candidates and not excluded: 
            reporter.record(clique)
            return
    else:
        #Si hay nodos en candidates saca uno para que sea el pivote
        #Si ya no tiene nodos entonces lo saca de excluded
        if len(candidates) > 0:
            pivot = max(candidates)
        else:
            pivot = max(excluded)
        #v va a tomar el valor de los nodos que estèn en candidates pero que no estèn en las relaciones del nodo pivote
        for v in candidates.difference(NEIGHBORS[pivot]):
            #quita al nodo v de los candidatos para no volverlo a usar
            candidates = candidates.difference([v])
            #crea una nueva lista del clique y le agrega el nodo v
            clique_new = clique[:]
            clique_new.append(v)
            #se crea un set con la intersecciòn de los candidatos y las relaciones del nodo v
            candidates_new = candidates.intersection(NEIGHBORS[v])
            #se crea un set con la intersecciòn de los excluidos y las relaciones del nodo v
            excluded_new = excluded.intersection(NEIGHBORS[v])
            #manda a llamar la funciòn IK con los nuevos datos
            IK(clique_new, candidates_new, excluded_new, reporter,NEIGHBORS)
            #agrega a los excluidos el nodo v
            excluded = excluded.union([v])
