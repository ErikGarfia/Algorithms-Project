from bron_kerbosch import IK
from data import *
from reporter import Reporter
 
 
if __name__ == '__main__':
	report = Reporter('## %s' % IK.__doc__)
	IK([], set(NODES), set(), report) 
	report.print_report()
