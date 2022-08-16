myStr= "Steve is a good boy"

print(len(myStr)) # 19 the length of the string
print(myStr[4]) # e (The character at 4th index of the string)

print(myStr[0:3]) # Ste (prints the characters from 0 to 2nd (n-1) index. If any index exceeds the range, it shows output till the last index )

print(myStr[:4]) # Stev (The default value of the first index is 0, it prints the characters from 0 to 3rd (n-1) index

print(myStr[:]) # Steve is a good boy (Takes the first index as 0 and the last index as the second index)

print(myStr[4:]) # e is a good boy (The default value of the second index is the last index, hence it prints the characters from 4 to last index

print(myStr[0:9:2]) # Seei (First, it takes the string from 0 to 8 index, but prints every second index such as 0,2,4,6 etc. (+2 getting added) . The default value of third argument is 1 i.e. by default, it prints all the indices in the given range)

print(myStr[::3]) #Sviao y (First, it takes the entire string , but prints every third index such as 0,3,6,9 etc. (+3 getting added))

print(myStr[-5]) # d (In case of negative indices, the last character of the string is indexed as -1, the character before it is indexed as -2 and so on)

print(myStr[-7:-1]) # ood bo (Prints from -7 till -2 (n-1) index. Can not be written as -1:-7 as it operates from left to right )

print(myStr[::-2]) # ybdo  ieeS  (Reverses the entire string, and prints every second value. In case of -1, it returns the entire reversed string)

#### String Methods (Print the output as required)####

#For further details about different String methods, checkout https://www.w3schools.com/python/python_ref_string.asp

myStr.isalnum() # false (Checks if the String is an alphanumeric one. Returns true or false)

myStr.isalpha() # false (Checks if the String is an alphabetic string. Returns true or false)

myStr.endswith("boy") # true (Checks if the String ends with the given value. Returns true or false)

myStr.count('o') # 3 (returns the number of occurences of given string)

myStr.capitalize() # Capitalizes the first character of the String. Does not modify the original String

myStr.find("is") # 6 (Returns the first occurence index of supplied string. -1 is not found)

myStr.upper() # Capitalizes the entire string. Does not modify the original String

myStr.lower() # Converts the entire string into lowercase. Does not modify the original String

print(myStr.replace('boy','girl')) # Steve is a good girl . Does not modify the original String


