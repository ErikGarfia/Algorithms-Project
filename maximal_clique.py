from bron_kerbosch import IK
from reporter import Reporter
 
 
def maximal_clique(NODES,NEIGHBORS):
	report = Reporter('## %s' % IK.__doc__)
	IK([], set(NODES), set(), report, NEIGHBORS) 
	report.print_report()
