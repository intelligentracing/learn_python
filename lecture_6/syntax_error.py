## This is course material for Introduction to Python Scientific Programming
## Class 6 Example code: syntax_error.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

# Most popular syntax error examples

# ********  Case 1: Wrong text formatting  ********
while i in range(10)        # Error
    print(i)
else                        # Error
      pass

# ********  Case 2: Misuse of brackets  ********
 List = ('abc','def')        
 print(List(1))              # Error

# ********  Case 3: Wrong indentation  ********
  x = 0
  y = 1
  z = 3

# ********  Case 4: Forget to import modules  ********
print(sqrt(9))

# ********  Case 5: Call methods in the wrong type of objects  ********
String = "Hello World!"
String.reverse()

# ********  Case 6: Use the wrong operator on variable types
List = ['abcde']
List = List + 'abcde'

# ********  Case 7: Misspell a variable
animals = ['dog', 'cat', 'pony', 'fisn', 'leopard', 'rabbit','mouse']
print(Animal[0])

# ********  Case 8: Wrong use of quotation marks
wrong_string = 'Mike's story'
print(wrong_string)


