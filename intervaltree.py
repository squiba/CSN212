RED = "RED"
BLACK = "BLACK"

class NilNode(object):
    def __init__(self):
        self.color = BLACK

NIL = NilNode()

class Interval:
    def __init__(self,low,high):
        self.low = low
        self.high = high

class Node:
    def __init__(self,interval,color=RED,left=NIL,right=NIL,p=NIL):
        self.color = color
        self.interval = interval
        self.key = interval.low
        self.maxi = interval.high
        self.left = left
        self.right = right
        self.p = p

    def updatemax(self):
        if self == NIL:
            pass
        else:
            if self.left != NIL:
                self.maxi = max(self.maxi,self.left.maxi)
            if self.right != NIL:
                self.maxi = max(self.maxi,self.right.maxi)
        
class Tree:
    def __init__(self,root=NIL):
        self.root = root

    def tree_insert(self,z):
        y = NIL
        x = self.root
        while x != NIL:
            y = x
            if z.key < x.key:
                x = x.left
	    else:
                x = x.right
        z.p = y
        if y== NIL:
            self.root = z
	elif z.key < y.key:
            y.left = z
	else:
	    y.right = z


    def right_rotate(self,x):
        assert (x.left != NIL)
        y = x.left
        x.left = y.right
        if y.right != NIL:
            y.right.p = x
        y.p = x.p
        if x.p == NIL:
            self.root = y
	elif x == x.p.right:
            x.p.right = y
	else:
            x.p.left = y
        y.right = x
        x.p = y

        x.updatemax()
        x.p.updatemax()

    def left_rotate(self,x):
        assert (x.right != NIL)
        y = x.right
        x.right = y.left
        if y.left != NIL:
            y.left.p = x
        y.p = x.p
        if x.p == NIL:
            self.root = y
	elif x == x.p.left:
            x.p.left = y
	else:
            x.p.right = y
        y.left = x
        x.p = y

        x.updatemax()
        x.p.updatemax()


    def rb_insert(self,x):
        self.tree_insert(x)
        x.color = RED
	while x != self.root and x.p.color == RED:
            if x.p == x.p.p.left:
                y = x.p.p.right
                if y.color == RED:
                    x.p.color = BLACK
                    y.color = BLACK
                    x.p.p.color = RED
                    x = x.p.p
	        else:
                    if x == x.p.right:
                        x = x.p
                        self.left_rotate(x)
                    x.p.color = BLACK
                    x.p.p.color = RED
                    self.right_rotate(x.p.p)
            else:
                y = x.p.p.left
                if y.color == RED:
                    x.p.color = BLACK
                    y.color = BLACK
                    x.p.p.color = RED
                    x = x.p.p
                else:
                    if x == x.p.left:
                        x = x.p
                        self.right_rotate(x)
                    x.p.color = BLACK
                    x.p.p.color = RED
                    self.left_rotate(x.p.p)
        self.root.color = BLACK


    def insert_node(self,x):
        self.rb_insert(x)

    def insert_interval (self,interval):
        if interval.low > interval.high:
            print("invalid interval as low >high---->",interval.low,interval.high)
            pass
        new_node = Node(interval)
        self.insert_node(new_node)

    def search(self,i):
        x=self.root
        while x!= NIL and (i.low > x.interval.high or x.interval.low > i.high):
            if x.left!=NIL and i.low<x.left.maxi:
                x=x.left
            else:
                x=x.right
        if x==NIL:
            return False
        return x
