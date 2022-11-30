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
1. abs() #returns the absolute value of a number
2. all() #returns True if all the elements in the iterable are true
3. any() #returns True if any element of the iterable is true
4. bin() #convert an integer number to a binary string
5. bool() #returns a boolean value
6. callable() #returns True if the object argument is callable and False if not
7. dict() #creates an empty dictionary
6. eval() #evaluates and executes an expression
8. filter() #construct an iterator from an iterable and returns True
9. float() #returns a floating point number from a number or string
10. format() #convert a value to a 'formatted' representation
11. getattr() #returns the value of the named attribute of object
12. help() #invoke the built-in help system
13. hex() #convert an integer number to a lowercase hexadecimal string
14. input() #takes the input from the user and prints it on screen converted into a string
15. int() #returns an integer object constructed from a number or a string
16. isinstance() #returns True if the object argument is an instance of an object
17. issubclass() #returns True is class is a subclass
18. len() #counts the characters in a string or values in a list or dictionary and returns an integer number
19. list() #creates an empty list #a list is a mutable object
20. map() #returns an iterator that applies function to every item of iterable
21. max() #returns the largest item in an iterable
22. min() #returns the smallest item in an iterable
23. next() #retrieves the next item from the iterator
24. open() #open file and return a corresponding file object
25. print() #prints the arguments you give to it on screen #takes keywords 'end' & 'sep'
26. round() #returns an integer after ndigits is rounded from the decimal point
27. slice() #returns a sliced object representing a set of indices
28. sorted() #returns a new sorted list from the items in iterable
29. str() #returns a string version of an object
30. sum() #sums all the items in iterable
31. tuple() #converts a list into a tuple #a tuple is an inmutable object
32. type() #returns the type of an object

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
1. ppl_age = {'Brad':21, 'Jane':30, 'Bianca':24, 'Josh':30} #create a dictionary #dictionaries are a pair of key:value
2. for k in ppl_age:
      print(ppl_age[key]) #access to keys
      'Brad', 'Jane', 'Bianca', 'Josh'
3. for v in ppl_age:
      print(ppl_age[value]) #access to values
      21, 30, 24, 30

#Functions
1. #a funtion can take arguments and return values
2. def function_name(): #function with no arguments
      print("Hello World")
   function_name()
3. def function_name(name): #function recives an arguments
      print(f"Hello {name}")
   function_name("World")
4. def add(num1,num2): #most times the function has a return value that indicates the value the function should return
      return num1 + num2
   add("2,2")

#Conditional Statements
1. a == 10 #equals
2. a != 10 #not equal
3. a > 10 #greater than
4. a >= 10 #greater than or equal to
5. a < 10 #less than
6. a <= 10 #less than or equal to
7. and #if a>10 and a<=20: #both conditions have to occur for it to be true, otherwise it's false
8. or #if a<10 or a>=20: #only one has to occur for it to be true, if none occur it's false
9. not #if not a==10: #it's true only if the variable is not equal to 10, otherwise it's false
10. colors = ['red','blue','green','yellow','orange','white','black'] #conditionañ test with list
    'red' in colors == True
    'green' not in colors == False
11. if age < 13:
      print("You are a kid.")
    elif age < 20:
      print("You are a teenager.") #if-elif-else statements
    else:
      print("You are an adult.")
12. <expression1> if <condition> else <expression2> #ternary conditional operator

#Handling Exceptions
1. #TRY/EXCEPT:
   divident = float(input("divident: "))
   divisor = float(input("divisor: "))
   try:
      print(divident/divisor)
   except ZeroDivisionError:
      print("You cannot divide by 0.")
2. #FINALLY:
   try:
      print(dividend / divisor)
   except ZeroDivisionError:
      print('You can not divide by 0')
   finally:
      print('Execution finished') #the finally code is always executed even if the exception is raised or not

#sys Variables
1. argv #command line args
2. builtin_module_names #linked C modules
3. byteorder #native byte order
4. check_interval #signal check frequency
5. exec_prefix #root directory
6. executable #name of executable
7. exitfunc #exit function name
8. modules #loaded modules
9. path #search path
10. platform #current platform
11. stdin, stdout, stderr #file objects for i/o
12. version_info #python version info
13. winver #version number
     
#os Variables
1. altsep #alternative sep
2. curdir #current dir string
3. defpath #default search path
4. devnull #path of null device
5. extsep #extension separator
6. linesep #line separator
7. name #name of os
8. pardir #parent dir string
9. pathsep #patch separator
10. sep #path separator

#Date Formatting
1. %a #abbreviated weekday (sun, mon, tue...)
2. %A #weekday (sunday, monday, tuesday...)
3. %b #abbreviated month (jan, feb, mar...)
4. %B #month (january, february, march...)
5. %c #date and time
6. %d #day(01 to 31)
7. %H #24 hour (00 to 23)
8. %I #12 hour (01 to 12)
9. %j #day of the year (001 to 366)
10. %m #month (01 to 12)
11. %M #minute (00 to 59)
12. %p #am or pm
13. %S #second (00 to 61)
14. %U #week number #starting on sunday (00 to 53)
15. %W #week number #starting on monday (00 to 53)
16. %w #weekday (0 to 6)
17. %x #date
18. %X #time
19. %y #year without century (00 to 99)
20. %Y #year (2008)
21. %Z #time zone (GMT)
22. %% #a literal % character 
