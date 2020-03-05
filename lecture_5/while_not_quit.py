## This is course material for Introduction to Python Scientific Programming
## Class 5 Example code: while_not_quit.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

animal_list = ['dog', 'cat','fish','pony','parrot','leopard','frog','mouse','snake']

index = 0
while True:
    answer = input('Would you like to adopt a '+ animal_list[index%9]+ '? [Y/N]')
    if answer.lower()=='y':
        break
    index += 1

print('We will have your ' + animal_list[index%9] + ' ready for pick up!')