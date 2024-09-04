Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
num = 5
# box called num with value 5
id(num)
4363637856
# the address of the box
name = 'Jakub'
id(name)
4355257616
a = 10
b = a
a
10
b
10
#the same value for a and b
id(a)
4363638016
id(b)
4363638016
#the same address for a and b
# so a and b have 1 box
id(10)
4363638016
# the address is based not on value it based on itself, so a and b and 10 are
#...are objects based on the same address
>>> k = 10
>>> id(k)
4363638016
>>> #still the same address because we are tagging a new variable on the...
>>> #...the same value which is 10
>>> a = 9
>>> id(a)
4363637984
>>> # the address changed because a have a new value
>>> id(b)
4363638016
>>> b
10
>>> # after changing a to new value 9, b is still pointed to 10 even if the previous statement says that b = a
>>> id(k)
4363638016
>>> k = a
>>> id(k)
4363637984
>>> # I need to make a new statement to point that variable to a new value/new box
>>> b = 8
>>> id(b)
4363637952
>>> # now a and k are pointed to one box with the same address and b is pointed to  another box with different address, and any of the variables are pointed to box with value 10, which is called "Garbage Collection"
>>> 
>>> PI = 3.14
>>> PI
3.14
>>> # PI is constant, but I can change it
>>> PI = 3.15
>>> PI
3.15
>>> type(PI)
<class 'float'>
>>> #with concept 'type()' I can see what type is the variable ( int, float etc)
>>> #I can create my own types
