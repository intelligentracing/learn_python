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

def tower_of_hanoi(tower, begin, end, disk_count):
    '''
    Using dynamic programming and recursion to solve tower of hanoi.
    Parameters:
    Input:  tower  - A list of three stacks, each recording the dishes on each rod
            begin       - Current starting rod number
            end         - Current goal rod number
            disk_count  - Indicate how many disks this step intends to achieve moving
    '''

    # This is just an example to check the input arguments
    if type(tower)!= list or len(tower)!=3 or \
        type(tower[0])!= deque or type(tower[1])!= deque or type(tower[2])!= deque:
        raise TypeError('Argument 1 must be a list of three stacks')

    if disk_count == 1:
        # this is a basic movement
        if len(tower[begin]) <=0 or \
            (len(tower[end])>0 and tower[begin][-1]>tower[end][-1]):
            raise Exception('The Rule is broken. Illegal move exists!')
        
        tower[end].append(tower[begin].pop())
        print(tower)
    else:
        middle_rod = the_other_rod(begin, end)

        tower_of_hanoi(tower, begin, middle_rod, disk_count - 1)
        tower_of_hanoi(tower, begin, end, 1)
        tower_of_hanoi(tower, middle_rod, end, disk_count - 1)

rod_1 = deque([4, 3, 2, 1])
rod_2 = deque([])
rod_3 = deque([])
tower= []
tower.append(rod_1)
tower.append(rod_2)
tower.append(rod_3)

print(tower)
tower_of_hanoi(tower, 0, 1, 4)