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
List.reverse()  # reverse in-place
print(List)