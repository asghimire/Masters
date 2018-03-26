#Simple calculations (8 points)
#Perform the following tasks using Python within Jupyter notebook.
#1.	Add two integers together

def addtwointegers(a,b):
    sum = a+b
    return sum

print (addtwointegers(5,8))

#2.	Show how parenthesis changes the order of operations when using multiplication and addition together.

x = 1+3*4 # prints 13
y= (1+3)*4 # Prints 16

print(x)
print (y)

# from the program it is proved python follows pemdas for arithmatic calculations.
# So the operation inside parenthesis will be done first.

#3.	Show how to square and cube numbers.

a=2
print (a**2)  #prints square of a which is assigned a value of 2
print (a**3)  #prints cube of a which is assigned a value of 2

#4.	Assign numbers to variables and then perform mathematical operations (e.g., add, subtract, multiply) using the variables.

a=10
b=5
print(a-b) #subtracts two numbers assigned to variables
print(a+b)  #addition
print(a*b)   #multiplication
print(a/b)   #division

#5.	Set the variable pi = 3.14159265 and then round it to two decimal places.

pi = 3.14159265
print(round(pi,2))


#6. See what happens when you try to divide a number by 0.
a=5
print(a/0) #5 divided by zero

#I got this error:
#print(a/0)
#ZeroDivisionError: division by zero

#7.	Add an integer and a floating point number. Is the result a floating point number or an integer?

a=2
b=0.35
sum = a+b
print (sum)

#8.	Compute the remainder of an odd number when divided by 2.

x= 9
y= 2
remainder=x%y
print(remainder)

# Working with strings
# 1. Enter Hello World! as a string
string = 'Hello World'
print(string)

# 2. Assign your first name to the variable first_name and your last name to the variable last_name.
first_name = 'Archana'
last_name = 'Sharma'
print(first_name +" "+ last_name)

# 3. Calculate the number of characters in your first name.

first_name = 'Archana'
print (len(first_name))

# 4. Using string indexing, get the first letter of your first name.
first_name = 'Archana'
print(first_name[0])

# 5. Using string indexing, get the last letter in your last name.
last_name ='Sharma'
print(last_name[-1])

# 6. See what happens when you add first_name and last_name.
first_name = 'Archana'
last_name = 'Sharma'
print(first_name + last_name)


# 7. See what happens when you multiply your first_name by an integer between 1 and 5.
first_name = 'Archana'
print(first_name*2)
print(first_name*3)




#Working with lists (5 points)
#1. Create a list of numbers from 1 to 5 and assign it to the variable L.
L = [1,2,3,4,5]
print(L)

#2. Using list indexing, select the second item in the list.
print(L[1])

#3. Using slices, get a list containing only the 2nd, 3rd, and 4th numbers.
print(L[1:4])

#4. Append a 6 to the end of the list.
L.append(6)
print(L)

#5. Using slices, replace the numbers 2 and 3 with 8 and 9.
L[1:3]=[8,9]
print(L)

