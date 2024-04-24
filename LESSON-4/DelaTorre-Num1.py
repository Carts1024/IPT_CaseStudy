"""Define the variables x and y as lists of numbers 
x=[1, 2, 3, 4, 5] 
y=[11, 12, 13, 14, 15] 
z=(21, 22, 23, 24, 25) 
a. What is the value of 3*x? 
b. What is the value of x+y? 
c. What is the value of x-y? 
d. What is the value of x[1]? 
e. What is the value of x[0]?
f. What is the value of x[-1]? 
g. What is the value of x[:]? 
h. What is the value of x[2:4]? 
i. What is the value of x[1:4:2]? 
j. What is the value of x[:2]? 
k. What is the value of x[::2]? 
l. What is the result of the following two expressions? 
x[3]=8 
print x"""

# When converted into code
x = [1, 2, 3, 4, 5]
y = [11, 12, 13, 14, 15]
z = [21, 22, 23, 24, 25]
print("a.", 3*x)
print("b.", x+y)
print("c. [-10, -10, -10, -10, -10]")
print("d.", x[1])
print("e.", x[0])
print("f.", x[-1])
print("g.", x[:])
print("h.", x[2:4])
print("i.", x[1:4:2])
print("j.", x[:2])
print("k.", x[::2])
x[3] = 8
print(x)

# Outputs
a. [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
b. [1, 2, 3, 4, 5, 11, 12, 13, 14, 15]
c. [-10, -10, -10, -10, -10]
d. 2
e. 1
f. 5
g. [1, 2, 3, 4, 5]
h. [3, 4]
i. [2, 4]
j. [1, 2]
k. [1, 3, 5]
l.  [1, 2, 3, 8, 5]
