List = list("Python")

# Method 1, using loop
reversed_list = []
index = len(List) # index point to last character + 1
while index>0:
    index = index -1
    reversed_list.append(List[index])

print(reversed_list)

# Method 2: extended slicing
reversed_list = List[::-1]
print(reversed_list)

# Method 3: use object method
reversed_list = List.copy()
reversed_list.reverse()  # reverse in-place
print(reversed_list)

# Let's compare Method 2 and Method 3's runtime
import time

List = list('abcdefghijklmnopqrstuvwxyz' * 10)
repeat_time = 1000000

# Test total time running while 100 times
begin_time = time.time()
for i in range(repeat_time):
    reversed_list = []
    index = len(List) # index point to last character + 1
    while index>0:
        index = index -1
        reversed_list.append(List[index])
elapsed_time = time.time() - begin_time
print('WHILE METHOD: Elapsed time: %.2f seconds' % elapsed_time)

# Test total time running slicing 100 times
begin_time = time.time()
for i in range(repeat_time):
    reversed_list = []
    reversed_list = List[::-1]
elapsed_time = time.time() - begin_time
print('SLICE METHOD: Elapsed time: %.2f seconds' % elapsed_time)

# Test total time running in-place reverse() 100 times
begin_time = time.time()
for i in range(repeat_time):
    reversed_list=List.copy()
    reversed_list.reverse()
elapsed_time = time.time() - begin_time
print('REVERSE METHOD: Elapsed time: %.2f seconds' % elapsed_time)