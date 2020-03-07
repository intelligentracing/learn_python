## This is course material for Introduction to Python Scientific Programming
## Class 5 Example code: for_continue.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

animal_list = ['dog', 'cat','fish','pony','parrot','leopard','frog','mouse','snake']

index = 0
adopted_animals=[]
for i in animal_list:
    answer = input('Would you like to adopt a '+ i + '? [Y/N]')
    if answer.lower()!='y':
        continue
    
    adopted_animals.append(i)

if not adopted_animals:
    print('Your adoption list is empty. See you next time!')
else:
    print('We will have your ' + str(adopted_animals) + ' ready for pick up!')