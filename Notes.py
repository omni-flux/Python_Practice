"""
starting my udemy course python date 3/3/2025

some usefull pycharm shortcuts
   shift + F10 -> run file
   shift + Alt + , or . -> increase or decrease font size
   ctrl + d -> duplicate the line
   ctrl + alt + l -> short-cut for formating
   refactor -> shift + F6
"""
'''
print("hello")
python is case-sensitive so ✔️print()  and Print()❌
print("hello"+" bob")

variables and constants
imvar = 'Variable'
IMCONST = 'Constant'
python has no true constant so
you could still change the value of a constant

Data type

imaginary = 9j
print(type(imaginary))

Nummeric type
number = -100
percent = 1.50
imaginary = 9j

Bool types
bool = True
bool = False

Sequence types
numbers = [1,2,3] list
coordinates = (2.5,1.0) tuple

mapping types
dictionary = {'Mario': 1,'Luigi': 2}

set types
raffel = {1,2,3,4} can change
frozenraffel = frozenset({1,2,3,4}) cant change

Type hints / anotations only for dev python dont care
text : str  = '10' ✔️
text : str = 10 will  give warning but python will still compile

Integer
age: int = 21
money: int = 0
self_esteem: int = -100

Float
PI: float = 3.14

Operators

+ - / *
floor division //
exponential **
modulus %

x: int = 2
x += 2 # x = x + 2
+= -= *= **= /= //= %=

comparison
a == b
a != b
a > b
a < b
a >= b
a <= b
a > d > c

logical
 a == b and a == b
 or
 not((a==b))

string
name : str = 'omkar'
name : str = "omkar"
say i want to adress some thing that's mine
name : str = "omkar's"  python be like :😊
name : str = 'omkar's' python be like :😠
so
name : str = 'omkar\'s' python be like :😊👍

quote : str = "he said:"hello"" python be like :😒👎
quote : str = "he said:\"hello\"" python be like :😊👍

str concatination
print(name +" "+ quote)

poem : str = """
dhsbhd
sdcshb
sdcnjsk
cdjk
"""

type conversion
txt_value = '100'
int_value = 50

print(txt_value + str(int_value) ) -> 10050

also if trying to convert incompatible
values we get value error for exp

print(int('ten')) -> value error

- made simple adder project

Lists
my_list: list = ['hello',2,8+9j,[22,False]]
people : list[str] = ['bob','romane conti','natsuki subaru','rem']
print(people[0])
people.append('ram')
people.remove('romane conti')
people.pop() -> removes the last element
people[0] = "ecidina"
people.insert(2,'beti')

Tuples
tuples are immutable -> denoted by ,
items : tuple = 1,4,True
coord : tuple = 55,66
new_tuple : tuple = ()

crrt type annotation for tuple
coordinates: tuple[float,bool] = (55.0,True)

sets
set has no order unlike lists
they can not contain duplicates

elements: set  = {True,99,'bob'}
elements.add('James')
elements.remove('bob')
elements.pop() -> removes some thing randon
elemts.clear() -> removes every thing
elements.clear()
after clear instead of printing an empty set it prints set()
print(elements)
to create a empty set we need to do this because doing {} will create a dict
empty: set = set()
same can be done for any data type

frozenset -> immutable set
things : frozenset = frozenset({1,33,33,45})
print(things)

dictnory
weather: dict = {'time': '12:00','weather':{'morning':'rain',
                                            'evening':'more rain'}}
print(weather['weather']['morning'])

users: dict = { 1: 'Luigi',2 : 'Mario'}
users[3] = 'bob'
del users[3]
# users.pop(3)
print("{} is a reletive of {}".format(users[2],users[1]))

None data type
no_value: None = None

🤨 union data type so it can be either or using '|'
possible_user : str | None = 'str'

- MADE MADLIB PROJECT

conditional loops

if-elif-else

weather:str = 'cloudy'

if weather == 'clear':
    print("it's a nice day")
elif weather == 'cloudy':
    print("The weather could be cloudy.")
else:
    print("IDK....🙄")

the order of the checks matter

age : int = 22

if age < 12:
    print("your a teenager")
elif age >= 18:
    print("your a young adult") #python gets to here and prints which is wrong
elif age > 25:
    print("your an adult")
else:
    print("unknown number")

Correct way ✔️
if age > 25:
    print("your an Adult")
elif age >= 18:
    print("your a young adult")
elif age < 12:
    print("your a Teenager")
else:
    print("unknown number")

if-else shorthand
cannot short had if elif and else ladder
number:int = 0
value:str = 'above 0' if number > 0 else '0 and below 0'

for Loop

text:str = 'Hello World'

for i in range(3):
    print(f"{i}:{text}")

people: list[str] = ['Bob','james','Maria']

for person in people:
    if len(person) > 4:
        print(f'{person} has a long name')



while loop

i: int = 5

while i > 0 :
    print('hello')
    i -= 1

while True:
    user_input: str = input('you:')
    if user_input == '💀' :
        print("bot:yes you are cooked")
    elif user_input == 'exit':
        quit(0)
    else:
        print("bot:what?")


while i > 0:
    i -= 1
    if i == 2
      break

while i > 0:
    i -= 1
    if i == 3:
        print('skipping')
        continue
    print(i)

total:int = 0

while True:
    try:
        user_input:int = int(input("Enter a positive number:"))

    except ValueError:
        print('i said a number dum dum..')
        continue

    if user_input < 0:
        print('A +ve NUMBERRRR!!!.....')
        continue

    if user_input == 0:
        print(f'Total: {total}')
        break

    total += user_input

break and continue work same for 'for' loops

as a rare functionality the else block can be
added to a for loop or a while loop and it works
as a sucess block so if you break in between the else
block will not be executated

num : int = 5

for i in range(num):
    if i < 5:
        print(i)
else:
    print('sucess') # will print sucess as no break

for i in range(num):
    if i < 5:
        print(i)
        break
else:
    print('sucess') # will not print as the loop was broken

- made rock paper sissors game

functions

def pp():
    print('Hello')

pp()

pass keyword:
(placeholde)

def get_status():
    pass
def connect_to_interne():
    pass

pass not just used in function could be used anwwhere:

if 1>0:
    pass
coluld also use ... insread of pass so

def connect:
    ...

parameters and arguments

def greet(name:str): # -> when you define it it's called the parameter
    print(f'Hello {name}')

greet("Mario")
greet("Luigi")  -> this is called an argument

def greet(name: str,language:str,default:str='Hello'):
    if language == 'ch':
        print(f"NI hao ma,{name}!")
    else:
        print(f"{default},{name}!")

greet('mario','','')
so this has to be in correct order else you get missing positional arguments

greet(default='helo',language='ch',name='mario')
we can also call this way its called keyword-arguments
it can be in any order

greet('mario',language='ch')
we can also mix

return types , keyword in functions

def get_length(text:str) -> int:
    print(f'Gettinng the length of:{text}..')
    return len(text)


def make_upper(text:str) -> str:
    return text.upper()

def connect_to_internet() -> None:
    print('connecting to internet')


RECURSION

def func() -> None:
    print('recursion')
    func()

def fact(num:int)->int:
    if num <= 1:
        return 1
    return num * fact(num-1)

def fibonacii(num:int)-> int:
    if num <= 0:
        return num

    return fibonacii(num-1) + fibonacii(num-2)

print(fibonacii(48))


import time
def connect_to_internet(signal:bool,delay:int) -> None:
     if delay < 5:
         signal = True

     if signal:
         print("connected ...")
     else:
         print(f'failed to connect trying again in {delay}s...')
         time.sleep(delay)
         connect_to_internet(signal,delay+1)

connect_to_internet(False,0)


'*'args,'**'kwargs

args denoted by a '*' it absorbs all the arguments and converts it into a tuple (3,4,4) ex code: func(3,4,4)
kwargs denoted ba a '**' it absorbs all the keyword arguments and converts them into a dictionary {x:2,Y:7} ex code: func(x=2,y=7)

def add(*args:int) -> int:
    return print(sum(args))

add(2,3,4,5,6)

one rule after a * you must call ** kwargs

def coordinates(**kwargs:int) -> None:
    print(kwargs)

coordinates(x=2,y=3,z=1)

one more rule for keyword arguments they must follow a order they are declared in


* & / in functions

/ and * used inside a function force every thing before / to be positional and after * to be kwargs
in between could be both
def exp(palce:str,/,time:int,*, name:str) -> None:
    print("sucess")

exp('tokyo',7,name="omm")✔️
exp(place="tokyo",7,'omm')❌

- made simple chatbot project.

user input
import sys
total:int = 0
while True:
    user_input:str = input('Enter a number:')
    if user_input == 0:
        print('total:',total)
        sys.exit()

    total += int(user_input)

try except

try:
    result:float = 10/0
    print(result)
except Exception as e:
    print(f'error:{e}')

while True:
    try:
        user_input:str= input('Enter anumber:')
        print(f'10/{user_input}= {10/float(user_input)}')
    except ZeroDivisionError :
        print('can not divide by zero')
    except ValueError:
        print('please enter a valid error')
    except Exception as e:
        print(f'some thing went wrong{e}')

total:int = 0
while True:
    user_input:str = input('Enter a number:')
    if user_input == '0':
        print('total:',total)
        sys.exit()
    try:
        total += int(user_input)
    except ValueError:
        print('enter a valid number')

else finally

user_input:str='10'

try:
    result:float = 1/float(user_input)
    print(f'1/{user_input}={result}')
except ValueError:
    print(f'\'{user_input}\' is not valid')
except ZeroDivisionError:
    print('you can\'t divide by 0 silly')
else:
    print('Executed successfully with out any errors ')
finally:
    print('no matter what ill execute')

raise keyword
raise Exception('this is a general exception')

def check_age(age:int) -> bool:
    if age < 0:
        raise ValueError('not a valid age...')
    elif age >= 21:
        print('you are old enough')
        return True
    else:
        print('you are not old enough ')
        return False


- made project letters only


modules

import time

print(time.sleep(2))


import greetings as g
from greetings import * # can be dangerous
from greetings import greet
g.greet('omm')
print(g.AUTHOR)

def main() -> None:
    ...

if __name__ == '__main__':
    logic()


so if you create a module and import it in the main py file and run it the logic
the logic in the module file and main file will run twice so to prevent that
we write if __name__ == '__main__': so logic only runs if the file is being ran on its own

modules -> pacakeges -> libraries

-made website status project

Unpacking
This is called unpacking or sequence unpacking. The opposite would be packing or tuple packing. The asterisk operator
* can be used to unpack an iterable into a function's arguments or to collect multiple elements into a single variable
during unpacking.
def my_function(a, b, c):
  print(a, b, c)
my_list = [4, 5, 6]
my_function(*my_list) # Output: 4 5 6


.1 + .2 != .3 but = 0.3000000000004




scope
number:int = 99 # global

def print_number()-> None:
    number =  99 # inner Shadows name •number from outer scope
    print(number)

global keyword
number:int = 0 # global

def change_number()-> None:
    global number
    number =  10 # inner

print(number)
change_number()
print(number)

non local keyword

def outer_func() -> None:
    name: str=''
    value: int= 0

    def inner_func() -> None:
        name = 'tom' #Shadows name 'value' from outer scope
        value = 100


def outer_func() -> None:
    name: str = ''
    value: int = 0

    def inner_func() -> None:
        nonlocal name, value
        name = 'tom'
        value = 100


-truthy and falsy

falsy values 
data:dict = {}
my_list: list = []
my_tuple: tuple = ()
empty_string: str = ''

anything that contains a value is truthy

--list comprehensions 

doubled_list:list[int]=[]
numbers:list[int]= [1,3,4,5,6]
# this
for num in numbers:
    doubled_list.append(num*2)
# or
doubled_list = [num*2 for num in numbers ]

# doubled_list:list[int]=[]
print(doubled_list)

names: list[str] = ['mario','james','luigi','john']
j_names:list[str]=[]

for name in names:
    if name.startswith('j'):
        j_names.append(name)

# or
j_names = [name
           for name in names
           if name.startswith('j')]



numbers: list[int] = [3,4,56,23,3,302,8,5,65]
even_number:list[int]=[]

for num in numbers:
    if num%2 == 0:
        even_number.append(num)

# or

even_number_lc = [num
                  for num in numbers
                  if num%2 ==0]


# --slicing

numbers:list[int] = [1,2,3,4,5,6]
print(numbers[0:3]) #[1,2,3]
print(numbers[3:6]) #[4,5,6]
# same
print(numbers[:3])
print(numbers[3:])

# reverse
print(numbers[-1]) #6

print(numbers[::-1]) #:: everything and -1 reverses it

print(numbers[0:6:3]) #:3  steps to 3

name:str = 'mario'
rev=name[::-1]
print(rev)


# if you loop through a list and try to modify it
# un-wanted things csn happen like if we remove bob in cris move to index 2 but
# the for loop has already gone to index 2 so it will not go again and chris just went missing in the void
# hence do this

people:list[str]= ['Anna','BOb','Chris','David','Fred']
new_people: list[str] = []

for person in people:
    print(f'-{person}, {people. index(person)}')
    if person == 'Bob':
        print (f' Removing: {person}' )
        continue
    new_people.append(person)

print(new_people)



--made project Grocery list 

'''















