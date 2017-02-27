from intervaltree import Interval,Tree

tree = Tree()

inputs = [Interval(15,20), Interval(10,30), Interval(17,19), Interval(5,20), Interval(12,15), Interval(130,40)]

for interval in inputs:
        tree.insert_interval(interval)
        
def Find(x):
	if tree.search(x):
		print("interval found")
	else:
		print("not found")

Find(Interval(14,16))
Find(Interval(21,23))
Find(Interval(305,309))
