# Addition
# Substraction
# Division
# Multipication
import operator
import math
A = 5
B = 3
print(A+B)
print(A-B)
print(A*B)
print(A/B)

first_string = [1, 2, 3]
second_string = [4, 5, 6]
print(first_string+second_string)

print(3*'ab ')
print((3 * 'a'' ''b'' '))


# exponential...

a, b = 2, 3

print(a**b)
print(pow(a, b))

print(math.pow(a, b))

# Modulas....
print(4 % 10)

print(operator.mod(3, 4))

# Boolean Operators...
x = 3.141
if 3.14 < x < 3.142:
    print("X is near pi")

# and...
P = True
Q = True
R = P and Q
print(R)
# OR
S = P or Q
print(S)
