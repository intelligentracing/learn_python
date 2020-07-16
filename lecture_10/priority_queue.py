## This is course material for Introduction to Python Scientific Programming
## Class 10 Example code: priority_queue.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use
from queue import PriorityQueue

directed_graph=[(12, [0, 1]), (5, [0,3]), (3, [0, 2]), (15, [1,5]), 
    (16, [2, 4]), (2, [4,5]), (25, [3,5])]

source_node = 0
sink_node = 5
DP_path = []
is_complete = False
search_queue = PriorityQueue()
search_queue.put((0, [sink_node]))
while is_complete == False and search_queue:
    current_path = search_queue.get()
    current_node = current_path[1][0]

    if current_node == source_node:
        # The smallest cost path has arrived at the source
        DP_path = current_path
        break

    for edge in directed_graph:
        if current_node == edge[1][1]:
            updated_path = [edge[1][0]] + current_path[1]
            new_path = (current_path[0] + edge[0], updated_path)
            search_queue.put(new_path)
    
print(DP_path)