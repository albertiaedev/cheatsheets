#PYTHON CHEATSHEET

#Math Operators
1. Addition == +
2. Substraction == -
3. Multiplication == *
4. Division == /
5. Integer Division == //
6. Modulus == %
7. Exponent == **

#Aumented Assigment Operators
1. var += n == var + n
2. var -= n == var - n
3. var *= n == var * n
4. var /= n == var / n
5. var %= n == var % n

#Data Types
1. Integers == 1,2,3,4,5,6
2. Floating Numbers == 0.1,0.2,0.3,0.4,0.5,0.6
3. Strings == 'a','A','b','B','c','C'
4. Booleans == True/False

#Naming Variables
1. var = 'hello world'
2. my_var = 'hello world'
3. var2 = 'hello world'
4. my_var3 = 'hello world'
5. 1var #can't begin with a number
6. _var #shouldn't be used again in the code

#Built-in Functions
1. print() #it prints the arguments you give to it on screen #takes keywords 'end' & 'sep'
2. input() #it takes the input from the user and prints it on screen converted into a string
3. len() #it counts the characters in a string or values in a list or dictionary and returns an integer number

#User Input
1. name=input("What's your name? -> ") #input a string of characters
   print(name)
2. age=int(input("How old are you? -> ")) #input an integer number
   print(age)
3. pi=float(input("What's the value of pi -> ")) #input a floating number
   print(pi)

#Tuples
1. tuple = ("Summer", "Winter", "Fall", "Spring") #tuples are inmutable

#Lists
1. colors = ['red','blue','green','yellow','orange','white','black'] #create a list
2. print(colors[0]) #get the first item in the list #forward
3. print(colors[1]) #get the second item in the list #forward
4. print(colors[-1]) #get the last item in the list #backwards
5. for color in colors: #looping throgh a list
      print(color)
6. colors = []
   colors.append('red') #adding items to a list
7. colors = ['red','blue','green','yellow','orange','white','black'] #slicing through a list
   print(colors[1:3]) = ['blue', 'green'] #slicing includes the first item you pass to it
                                          #and excludes the last one you pass to it

#Dictionaries
ppl_age = {'Brad':21, 'Jane':30, 'Bianca':24, 'Josh':30} #create a dictionary #dictionaries are a pair of key:value
for k in ppl_age:
   print(ppl_age[key]) #access to keys
   'Brad', 'Jane', 'Bianca', 'Josh'
for v in ppl_age:
   print(ppl_age[value]) #access to values
   21, 30, 24, 30
