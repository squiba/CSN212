import numpy as np
import matplotlib.pyplot as plt
import sys
import random
import time 

gridsize = 100000

def distance(p, q):
    #distance between points p and q
    dx, dy = int(q[0]) - int(p[0]), int(q[1]) - int(p[1])
    return (dx * dx) + (dy * dy)

def turn(p, q, r):
    #returns -ve,0, or +ve depending on the angle p-q-r makes (with q being the angle)
    return ((int(q[0]) - int(p[0]))*(int(r[1]) - int(p[1])) - (int(r[0]) - int(p[0]))*(int(q[1]) - int(p[1])) > int(0)) - ((int(q[0]) - int(p[0]))*(int(r[1]) - int(p[1])) - (int(r[0]) - int(p[0]))*(int(q[1]) - int(p[1])) < int(0))

L_turn, R_turn, straight = (1, -1, 0)

def next_hull_point(points, p):
    #outputs the next hull point
    q = p
    for r in points:
        t = turn(p, q, r)
        if t == R_turn or t == straight and distance(p, r) > distance(p, q):
            q = r
    return q

def find_min_p(points):
    min_num = points[0]
    for i in points:
        if int(i[1]) < int(min_num[1]):
            min_num = i
        elif int(i[1]) == int(min_num[1]):
            if int(i[0]) < int(min_num[0]):
                min_num = i
    return min_num

def find_hull(points):
    min_p = find_min_p(points); hull = [min_p]
    for p in hull:
        q = next_hull_point(points, p)
        if q != hull[0]:
            hull.append(q)
    return hull

def generate_random_array(array_sizes):
    """Generate array with random points for a given sizes"""
    pts_array = {}
    for ii in range(array_sizes):
        random_x = random.randrange(0, 1000)
        random_y = random.randrange(0, 1000)
        
        #Uncomment line below and comment while line when want
        #circular_distribution, otherwise it is rectangular distribution
        #while[random_x,random_y] in pts_array.values() or circular_distribution(random_x, random_y) == False:
        
        #check if the point is unique in the list
        while [random_x, random_y] in pts_array.values():
            random_x = random.randrange(0, 1000)
            random_y = random.randrange(0, 1000)                      
        pts_array[ii] = [random_x , random_y]                         
    return list(pts_array.values())   


def analyse_time_gift(size_to_test):
    """This function takes list of array and number of trials as argument.
It prints time taken to perfrom giftwrap algorithm for given lists"""
    
    if sys.version_info < (3, 3):
        get_time = time.clock
    else:
        get_time = time.perf_counter
        REZ = time.get_clock_info('perf_counter').resolution   

    list_to_test = generate_random_array(size_to_test)
    start = get_time()
    sol = find_hull(list_to_test)
    end = get_time()

    time_taken_per_locate = end-start
    return time_taken_per_locate

def test_gift():
    no_of_pts = []
    time_taken = []    
    list_of_sizes = list(range(1000, 20001, 1000))
    no_of_trials = 1
    
    for i in range(len(list_of_sizes)):
        no_of_pts.append(list_of_sizes[i])
        time_taken.append(analyse_time(list_of_sizes[i], no_of_trials))
    print(no_of_pts)
    print(time_taken)
