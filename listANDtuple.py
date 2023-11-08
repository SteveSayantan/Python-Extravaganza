#List is a collection of similar or dissimilar datatypes.

grocery=['Daal','Chawal','Sunlight','Tel'] #Creating a list

print(grocery[3]) #Tel
print(len(grocery)) #4

#Slicing of an List (Keeps the original List intact)

numbers=[6,4,3,5,2]

numbers[:]      # returns the whole List as the default value is 0 and length of the list respectively

numbers[1:4]    # returns the elements from 1 to 3 index (n-1)

numbers[:4:2]   # returns every second element starting from index 0 till index 3  

numbers[::-1]   # returns the reversed List

#Methods of List
marks=[34,23,34,56,23,34]

marks[0]=99                 #Sets the 0 index as 99 as List is mutable
marks.sort()              #Sorts the original list, stable sorting , returns None
marks.sort(reverse=True) #Sorts the original list in reverse order
marks.reverse()         # Reverses the original  List

max(marks) # Returns the max item in the List
min(marks) # Returns the min item in the List

marks.append(45) # Adds 45 to the end of the original List, returns None
marks.insert(3,69)   # Inserts 69 at 3rd index in the original list, other elements are adjusted accordingly, returns None
marks.remove(34) # Removes 34 from the original List 
marks.pop() # Removes the last element from the original list


#Tuple (It is similar to List except that it is immutable)

tp1=(2,3,5) #Tuples use parenthesis
tp2=(2,)    #To create tuple containing one element we must use a comma
print(tp1)  

#Swapping two variables

a,b=56,67 #Declaring and initializing two vars in the same line

a,b=b,a #This is what we do for swapping
print(a) #67
print(b) #56

#Explore other list methods from Google!!





