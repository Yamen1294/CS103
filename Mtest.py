#-----------Variables and Data Types-----------#
#-----------Multiple Assignment-----------#
print("-----------Multiple Assignment-----------")
a = b = c = 9
x, y, z = 1, 3.5, "Hello"
var1, var2, var3 = "Apple", "Banana", "Cherry"
print(a, b, c)
print(x, y, z)
print(var1, var2, var3)
#-----------EXPRESSIONS-----------#
print("-----------EXPRESSIONS-----------")
a = 7 - 4 #3
b = a **2 #9
print(a,b) #3 9 
print(a + b) #12
#-----------Print(Function)-----------#
print("-----------Print(Function)-----------")
print("Hello World!")
print("Hello", "World", sep="-")
print("Hello", end=" ")
print("World")
print(2 + 3 * 5) #17
print("Sum:", 2 + 3) #Sum: 5
print("Hello","World!",1,2,3) #Hello World! 1 2 3
#-----------Escape Sequence-----------#
print("-----------Escape Sequence-----------")
"""
\b => Backspace
\n => New Line
\t => Tab (4 spaces,horizontal tab)
\\ => Backslash
\' => Single Quote
\" => Double Quote
\"\"\" => Triple Double Quotes
\'\'\' => Triple Single Quotes

"""
print("Hello\bWorld!") #HelloWorld!
print("Hello\nWorld!")
print("Hello\tWorld!")
print("This is a backslash: \\")
print('He said, \'Hello World!\'')
print("He said, \"Hello World!\"")
#-----------Input-----------#
print("-----------Input-----------")
name = input("Enter your name: ")
#print("Hello " + name + "! Welcome to the program.")
print(f"Hello {name}! Welcome to the program.") #better
"""
input() function is used to take input from the user.
input() function always returns a string.
"""
#-----------Converting Variable Type(Type casting)-----------#
print("-----------Converting Variable Type(Type casting)-----------")
num1 = input("Enter first number: ") #string
age = int(input("Enter your age: ")) #int
height = float(input("Enter your height in meters: ")) #float
print(f"You are {age} years old and {height} meters tall.")
#-----------Data Types-----------#
print("-----------Data Types-----------")
"""
int => Integer (whole numbers) Range: -2147483648 to 2147483647
float => Floating-point numbers (decimal numbers)
complex => Complex numbers (real and imaginary parts)

str => String (text)
list => List (ordered, mutable collection)
tuple => Tuple (ordered, immutable collection)


bool => Boolean (True or False)

set => Set (unordered collection of unique items)

dict => Dictionary (key-value pairs)


"""
number = 10 #int
pi = 3.14 #float
complex_num = 2 + 3j #complex
text = "Hello, World!" #str
fruits = ["apple", "banana", "cherry"] #list
coordinates = (10.0, 20.0) #tuple
is_valid = True #bool
unique_numbers = {1, 2, 3, 4, 5} #set
person = {"name": "Alice", "age": 30} #dict

#-----------Sequence Data Type(string)-----------#
print("-----------Sequence Data Type(string)-----------")
text = "Hello, World!"
print(text[0]) #H
print(text[7]) #W
print(text[-1]) #!
print(text[0:5]) #Hello
print(text[7:12]) #World
a = "Hello"
b = "Yash"
print(a+b) #HelloYash
print(a*3) #HelloHelloHello
print("lo" in a) #True
print("world" in a) #False

#-----------Funs in string-----------#
print("-----------Funs in string-----------")
"""
len() => Returns the length of the string
title() => Converts the first character of each word to uppercase
upper() => Converts all characters to uppercase
lower() => Converts all characters to lowercase
strip() => Removes leading and trailing whitespace
replace() => Replaces a specified substring with another substring
split() => Splits the string into a list of substrings based on a delimiter
find() => Returns the index of the first occurrence of a substring
islower() => Checks if all characters are lowercase
isupper() => Checks if all characters are uppercase
isspace() => Checks if the string contains only whitespace characters

"""

str1="Hello world!"
print(len(str1)) #13
print(str1.title()) #Hello World!
print(str1.upper()) #HELLO WORLD!
print(str1.lower()) #hello world!
print(str1.find("world")) #6
print(str1.find("o",5))
print(str1.find("x")) #-1
print(str1.replace("world","Yash")) #Hello Yash!
print(str1.islower()) #False
print(str1.isupper()) #False
print(str1.isspace()) #False
#-----------Container Type(List)lisr tuples dic-----------#
print("-----------Container Type(List)lisr tuples dic-----------")
list1 = [1, 2, 3, 4, 5]
list2 = ["apple", "banana", "cherry"]
list3 = [True, False, True]
list4 = [1, "apple", True, 3.14]

print(list1[0]) #1
print(list2[1:3]) #['banana', 'cherry']
print(list3[-1]) #True
print(list3 * 2) #[True, False, True, True, False, True]
print(list2 + list4) #['apple', 'banana', 'cherry', 1, 'apple', True, 3.14]
list2.append("date")
print(list2) #['apple', 'banana', 'cherry', 'date']
list1.remove(3)
print(list1) #[1, 2, 4, 5]
list1.insert(1, 3)
print(list1) #[1, 3, 2, 4, 5]
list4.extend([False, "banana"])
print(list4) #[1, 'apple', True, 3.14, False, 'banana']
list3.pop()
print(list3) #[True, False]
list4.remove("apple")
print(list4) #[1, True, 3.14, False, 'banana']
list6= ["a","b","c","d","e","f","g"]
del list6[2:5]

len(list2) #4
list5=list2.copy()
list5.extend(["fig","grape"])
list5.count("fig") 
list5.index("banana")   
num_list = [5, 2, 9, 1, 5, 6,20,4404,321]
num_list.sort(reverse=True)#descending order
num_list.sort()#ascending order
min(num_list)
max(num_list)
sum(num_list)
print(list1,list2,list3,list4,list5,num_list,list6)
#########For loop########
"""
for loop is used to loop on each element in list or tuple or even strings

we can use for loop with range function to loop from specific range
"""

for char in "Hello":
        print(char,end=" ")

for i in range(5):
        print(i,end=" ")

for j in range(0,11):
        print(j,end=" ")

"""
we can even make nested loop 

and the meaning is when making the first loop x is taking values from 1 to 4 because we stop at 5 and not taking it

the secode loop is j in range of x we know x is 1 2 3 4 
so it's basically j in range 1 then 2 then 3 then 4
"""
for x in range(1,5):
    for y in range(x):
        print(y,end=" ")
    print()



#if statements 

"""
we use if to run code in specific condition if the condition is true then the code will execute if not the code will not execute 
"""

age =18
if age >=18:
   print("You are adult")
else:
  print("You underage")


x =5
y =10

if x>y: #x is not more than y so it's false
   print("x is greater")
elif y<x:
    print("y is greater")
else:
   print("they are equal")


#While loop
"""
while loop is used when we don't know the range specific and we can make infinite loop with while loop too
"""

#normal loop

i=0
while i<10:
   print(i)
   i+=1

# the output is 0 1 2 3 4 5 6 7 8 9
#it compares between i and 10 while i is #smaller print it and add one to it till it #reaches 10 and stop

#infinite loop

n=0
while n<10:
   print("Hello world")
"""
it will print Hello world for infinite time because 10 is always greater than 0 and there nothing change this condition 
"""

while True:
   print("i love python")

"""
same concept while True and it always true so it's infinite loop
"""