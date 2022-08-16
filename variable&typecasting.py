var1= "Hello World "
var2= 4
var3= 36.7
var4= "Steve"
# print(type(var1))     # <class 'str'> as it stores a string
# print(type(var2))     # <class 'int'> as it stores a string
# print(type(var3))     # <class 'float'> as it stores a string


print(var2+var3)  #40.7

# print(var1+var4) # Hello World Steve (Concatenation)

''' Type Casting '''

var5="45"
var6= "36"

print(int(var5) + int(var6)) #TypeCasting a String to an Integer

"""
Some Other Methods for Type Casting

str()
float()

"""

# print(10*var1)            #Prints Hello World 10 times as it is a string
# print(3*str(int(var5) + int(var6)))           #Type Casts the final result (int) to String and prints 5 times