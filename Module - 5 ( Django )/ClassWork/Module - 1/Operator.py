#arithmetic operators(+, -, , /, //, %, *)
# a = 10
# b = 3 
# print("addition:", a + b) #13
# print("subtraction:", a - b) #7 
# print("multiplication:", a * b) #30
# print("division:", a / b) #3.3333333333333335
# print("floor division:", a // b) #3
# print("modulus:", a % b) #1
# print("exponentiation:", a ** b) #1000



#comparison operators (==, !=, >, <, >=, <=)
a = 10
b = 20  
print("equal to:", a == b) #False
print("not equal to:", a != b) #True
print("greater than:", a > b) #False
print("less than:", a < b) #True
print("greater than or equal to:", a >= b) #False
print("less than or equal to:", a <= b) #True

#logical operators (and, or, not)
a = True
b = False
print("logical and:", a and b) #False
print("logical or:", a or b) #True
print("logical not:", not a) #False

#assignment operators (=, +=, -=, =, /=, //=, %=, *=)
a = 10
a += 5 # a = a + 5
print("after += 5:", a) #15
print("after -= 5:", a) #10
print("after *= 5:", a) #50
print("after /= 5:", a) #10.0
print("after //= 5:", a) #2.0
print("after %= 5:", a) #0.0
print("after **= 5:", a) #0.0

#identity operators (is, is not)
a = [1,2,3]
b = [1,2,3]
c = a
print("a is b:", a is b) #False
print("a is c:", a is c) #True
print("a is not b:", a is not b) #True

#membership operators (in, not in)
a = [1,2,3,4,5]
print("3 in a:", 3 in a) #True
print("6 in a:", 6 in a) #False
print("3 not in a:", 3 not in a) #False
print("6 not in a:", 6 not in a) #True