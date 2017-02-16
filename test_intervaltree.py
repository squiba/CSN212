from intervaltree import Interval,Tree

tree = Tree()
tree.insert_interval(Interval(15,20))
tree.insert_interval(Interval(10,30))
tree.insert_interval(Interval(17,19))
tree.insert_interval(Interval(5,20))
tree.insert_interval(Interval(12,15))
tree.insert_interval(Interval(130,40))
#tree.insert(Interval(60,70))
#tree.delete(Interval(60,70))

def Find(x):
	if tree.search(x):
		print("interval found")
	else:
		print("not found")

Find(Interval(14,16))
Find(Interval(21,23))
Find(Interval(305,309))
