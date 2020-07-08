def IK(clique, candidates, excluded, reporter,NEIGHBORS):
    '''Bron–Kerbosch algorithm with pivot'''
    reporter.inc_count()
    if not candidates:
            reporter.record(clique)
            return
    else:
        pivot = max(candidates)
        for v in candidates.difference(NEIGHBORS[pivot]):
            candidates = candidates.difference([v])
            clique_new = clique[:]
            clique_new.append(v)
            candidates_new = candidates.intersection(NEIGHBORS[v])
            excluded_new = excluded.intersection(NEIGHBORS[v])
            IK(clique_new, candidates_new, excluded_new, reporter,NEIGHBORS)
            excluded = excluded.union([v])
