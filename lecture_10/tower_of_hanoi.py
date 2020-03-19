## This is course material for Introduction to Python Scientific Programming
## Class 10 Example code: tower_of_hanoi.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from collections import deque

def the_other_rod(begin,end):
    ''' This function returns the other rod number from the set of {1, 2, 3} that is not begin or end
    '''
    rod_set = [0,1,2]
    rod_set.remove(begin)
    rod_set.remove(end)
    return rod_set.pop()

def tower_of_hanoi(tower_list, begin, end, disk_count):
    '''
    Using dynamic programming and recursion to solve tower of hanoi.
    Parameters:
    Input:  tower_list  - A list of three sublists, each recording the dishes on each rod
            begin       - Current starting rod number
            end         - Current goal rod number
            disk_count  - Indicate how many disks this step intends to achieve moving
    '''

    # This is just an example to check the input arguments
    if type(tower_list)!= list or len(tower_list)!=3 or \
        type(tower_list[0])!= deque or type(tower_list[1])!= deque or type(tower_list[2])!= deque:
        raise TypeError('Argument 1 must be a list of three integer lists')

    if disk_count == 1:
        # this is a basic movement
        if len(tower_list[begin]) <=0 or \
            (len(tower_list[end])>0 and tower_list[begin][-1]>tower_list[end][-1]):
            raise Exception('The Rule is broken. Illegal move exists!')
        
        tower_list[end].append(tower_list[begin].pop())
        print(tower_list)
    else:
        middle_rod = the_other_rod(begin, end)

        tower_of_hanoi(tower_list, begin, middle_rod, disk_count - 1)
        tower_of_hanoi(tower_list, begin, end, 1)
        tower_of_hanoi(tower_list, middle_rod, end, disk_count - 1)

rod_1 = deque([4, 3, 2, 1])
rod_2 = deque([])
rod_3 = deque([])
tower_list= []
tower_list.append(rod_1)
tower_list.append(rod_2)
tower_list.append(rod_3)

print(tower_list)
tower_of_hanoi(tower_list, 0, 1, 4)