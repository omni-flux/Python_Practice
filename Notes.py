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

------------------------------------------------dictionary
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

------------------------------------------------conditional loops

------------------------------------------------if-elif-else

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

-----------------------------------------------------for Loop
text: str = 'Hello World'

for i in range(3):
    print(f'{i}:{text}')

people: list[str] = ['Bob', 'james', 'Maria']

for person in people:
    if len(person) > 4:
        print(f'{person} has a long name')
-----------------------------------------------------while loop

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

-------------------------------------------------functions

def pp():
    print('Hello')

pp()

------------------------------------------------pass keyword:
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

----------------------------------------------parameters and arguments

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
so this has to be in crorect order else you get missing positional arguments

greet(default='helo',language='ch',name='mario')
we can also call this way its called keyword-arguments
it can be in any order

greet('mario',language='ch')
we can also mix

----------------------------------------return types , keyword in functions

def get_length(text:str) -> int:
    print(f'Getting the length of:{text}..')
    return len(text)


def make_upper(text:str) -> str:
    return text.upper()

def connect_to_internet() -> None:
    print('connecting to internet')


----------------------------------------------------RECURSION

def func() -> None:
    print('recursion')
    func()
func()

def fact(num:int)->int:
    if num <= 1:
        return 1
    return num * fact(num-1)

def fibonacii(num:int)-> int:  #this is wrong i think its missing 1 or 2 more if conditional statements in addition to num <= 0
    if num <= 0:
        return num

    return fibonacii(num-1) + fibonacii(num-2)

print(fibonacii(40))

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


--------------------------------------------------'*'args,'**'kwargs

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

-----------------------------------------------------user input

import sys
total:int = 0
while True:
    user_input:str = input('Enter a number:')
    if user_input == 0:
        print('total:',total)
        sys.exit()

    total += int(user_input)

--------------------------------------------------------try except

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

---------------------------------------------------------------raise keyword
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


-------------------------------------------------------------------modules
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

------------------------------------------------------------Unpacking
This is called unpacking or sequence unpacking. The opposite would be packing or tuple packing. The asterisk operator
* can be used to unpack an iterable into a function's arguments or to collect multiple elements into a single variable
during unpacking.
def my_function(a, b, c):
  print(a, b, c)
my_list = [4, 5, 6]
my_function(*my_list) # Output: 4 5 6


.1 + .2 != .3 but = 0.3000000000004

------------------------------------------------------------------scope
number:int = 99 # global

def print_number()-> None:
    number =  99 # inner Shadows name •number from outer scope
    print(number)

----------------------------------------------------------------global keyword

number:int = 0 # global

def change_number()-> None:
    global number
    number =  10 # inner

print(number)
change_number()
print(number)

----------------------------------------------------------------non local keyword

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


--------------------------------------------------------------------truthy and falsy

falsy values 
data:dict = {}
my_list: list = []
my_tuple: tuple = ()
empty_string: str = ''

anything that contains a value is truthy

--------------------------------------------------------------list comprehensions 

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


# -------------------------------------------------------------------slicing

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
# un-wanted things can happen like if we remove bob in cris move to index 2 but
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



#--------------------------------------------------------------- OOP in python
#
# class Cars:
#     def __init__(self,brand:str,wheels:int)->None:
#         self.brand = brand
#         self.wheels = wheels
#
#     def turn_on(self)->None:
#         print(f'Turning on:{self.brand}')
#
#     def turn_off(self)->None:
#         print(f'Turning off:{self.brand}')
#
#     def drive(self,km:float)->None:
#         print(f'Driving {self.brand} for {km}km')
#
#     def describe(self) -> None:
#         print(f'{self.brand} is a car with {self.wheels}')
#
#
# def main() -> None:
#     bmw: Cars = Cars('BMW',4)
#     bmw.turn_on()
#     bmw.drive(10)
#     bmw.turn_off()
#     bmw.describe()
#
#     volvo:Cars = Cars('volvo',6)
#     volvo.turn_on()
#     volvo.drive(5.6)
#     volvo.turn_off()
#
# if __name__ == '__main__':
#     main()


# ---------------------------------------------------------------- __init__()
#
# __init__() grants the ability to customise any new instance of a class it is
# called every time a new object is instantiated of the type of the class
#
# class Connection:
#     def __init__(self,type:str,rate:int)->None:
#         self.type = type
#         self.rate = rate
#         print(f'the {self.type} connection was established it costs ₹{rate}/hr')
#
#     def disconnect(self)->None:
#         print(f'{self.type} was disconnected...')
#
# def main() -> None:
#     cellular:Connection = Connection('cellular',50)
#     internet:Connection = Connection('internet',90)
#     internet.disconnect()
#     cellular.disconnect()
#
# if __name__ == '__main__':
#     main()


# ----------------------------------------------------------- self
# self refers to the current instance of a class
# so as __init__() creates an instance self helps identify which instance it is
# Also it's just a naming convention it can be named something else as well but not recommended


# class Fruit:
#     def __init__(self,name:str,grams:float)->None:
#         self.name = name
#         self.grams = grams
#
#     def eat(self)->None:
#         print(f'eating {self.grams} grams of {self.name}')
#
# def main() -> None:
#     appel: Fruit = Fruit('appel',50) #so here self would be appel
#     appel.eat()
#
#     banana: Fruit = Fruit('banana',7) #and here it would be banana
#     banana.eat()
#
#
# if __name__ == '__main__':
#     main()

#------------------------------------------------Attributes(class & instances)

# the self and __init__() were instance attributes but we can also
# have class attributes that are shared among all the instances of that class

# class Car:
#     SPEED_LIMIT: float = 140
#     def __init__(self,brand:str)->None:
#         self.brand = brand
#
#     def drive(self,*,speed:float) -> None:
#         if speed > self.SPEED_LIMIT:
#             print(f'limiter activated driving at {self.SPEED_LIMIT}')
#         else:
#             print(f'driving {self.brand} at {speed}')
#
# def main() -> None:
#     bmw:Car = Car('BMW')
#     bmw.drive(speed=150)
#     Car.SPEED_LIMIT = 200
#     bmw.drive(speed=150)
#
# if __name__ == '__main__':
#     main()


# dangerous part of class attributes

# class Animals:
#     tricks:list[str] = []  #as this is a class atrribute it is shared by each instance so dog will meow
#     def __init__(self,name:str)->None:
#         self.name = name
#
#     def teach_trick(self,trick:str)->None:
#         self.tricks.append(trick)
#
# def main() -> None:
#     cat:Animals = Animals('cat')
#     dog:Animals = Animals('dog')
#     cat.teach_trick('meow')
#     dog.teach_trick('bark')
#
#     print(cat.tricks)
#     print(dog.tricks)
# if __name__ == '__main__':
#     main()

#  so to fix that we need to declare tricks as a instance attribute

# class Animals:
#     def __init__(self,name:str)->None:
#         self.name = name
#         self.tricks:list[str] = []
#     def teach_trick(self,trick:str)->None:
#         self.tricks.append(trick)
#
# def main() -> None:
#     cat:Animals = Animals('cat')
#     dog:Animals = Animals('dog')
#     cat.teach_trick('meow')
#     dog.teach_trick('bark')
#
#     print(cat.tricks)
#     print(dog.tricks)
# if __name__ == '__main__':
#     main()
# -- note to my self study about typing module
# ------------------------------------------------------------------dunder methods

# from typing import Self
#
# class Book:
#     def __init__(self,title:str,pages:int)->None:
#         self.title = title
#         self.pages = pages
#
#     def __len__(self)->int:
#         return self.pages
#
#     def __add__(self, other:Self)->Self:
#         combined_title:str = f'{self.title} & {other.title}'
#         combined_pages:str = self.pages + other.pages
#         return Book(combined_title,combined_pages)
#
#
# def main() -> None:
#     oriely_python : Book = Book('oriely_python',500)
#     monogatari:Book = Book('monogatari',1000)
#
#     print(len(oriely_python))
#     combined_books : Book = oriely_python + monogatari
#     print(combined_books.title)
#     print(combined_books.pages)
#
# if __name__ == '__main__':
#     main()


# ----------------------------------------------------------- __str__(),__repr__()
# by default when you print an instantiated object lets say from class book it returns <__main__.book object at x00000347634>
# which is a memory location which is what repr returns this is helpful for devs but say a user print the object and their puny brain
# if flash banged by looking at an actual memory location we could prevent that by defining __str__() now when they print it, they will get a
# well abstracted string and the dev has to call repr() on the obj to see its location if we dont define __str__ it fallbacks to __repr__


# class Person:
#     def __init__(self,name:str,age:int)->None:
#         self.name = name
#         self.age = age
# def main() -> None:
#     mario:Person  = Person('mario',27)
#     print(mario) # <__main__.Person object at 0x000002A71561AD50>
# if __name__ == '__main__':
#     main()
#
#now lets change that
#
# class Person:
#     def __init__(self,name:str,age:int)->None:
#         self.name = name
#         self.age = age
#         self.location = hex(id(self))
#     def __str__(self) -> str:
#         return f'the person is named {self.name} and they are {self.age} years old'
#
#     def __repr__(self) -> str:
#         return f'person(name={self.name},age={self.age},location={self.location})'
#
# def main():
#     mario:Person  = Person('mario',27)
#     print(mario)
#     print(repr(mario))
# if __name__ == '__main__':
#     main()

#------------------------------------------------------------- __eq()__
# __dict__

# so the __eq()__ dunder method lets you check weather an instance of a class is equal or not it compares the
# memory locations for comparision wich can return false even if all the attributes we declared are same so we can change
# how that behaves and __dict__ dunder method just returns a dictionary of all the instance attributes and their values

# class Car:
#     def __init__(self,brand:str,car_id:int,colour:str) -> None:
#         self.brand = brand
#         self.car_id = car_id
#         self.colour = colour
# def main() -> None:
#     car1:Car = Car('volvo',1,'red')
#     car2:Car = Car('volvo',1,'red')
#     print(car1 == car2) # returns false even if the attributes are same cause it has diff memory location
# if __name__ == '__main__':
#     main()

# from typing import Self
# class Car:
#     def __init__(self,brand:str,car_id:int,colour:str) -> None:
#         self.brand = brand
#         self.car_id = car_id
#         self.colour = colour
# 
#     def __eq__(self, other:Self)->bool:
#         print(self.__dict__) #{'brand': 'volvo', 'car_id': 1, 'colour': 'red'}
#         print(other.__dict__) #{'brand': 'volvo', 'car_id': 1, 'colour': 'red'}
#         return self.__dict__ == other.__dict__
#     
# def main() -> None:
#     car1:Car = Car('volvo',1,'red')
#     car2:Car = Car('volvo',1,'red')
#     print(car1 == car2)# now it returns True 
# if __name__ == '__main__':
#     main()
"""

# -------------------------------inheritance
#
# class Animal:
#     def __init__(self,name:str)->None:
#         self.name = name
#
#     def drink(self)->None:
#         print(f'{self.name} is drinking.')
#
#     def eat(self)->None:
#         print(f'{self.name} is eating')
#
# class Dog(Animal):
#     def __init__(self,name:str)->None:
#         super().__init__(name)
#     def bark(self)->None:
#         print(f'{self.name}: bark! bark!')
#
#     def routine(self)->None:
#         self.eat()
#         self.bark()
#         self.drink()
#
# class Cat(Animal):
#     def __init__(self,name:str)->None:
#         super().__init__(name)
#     def meow(self)->None:
#         print(f'{self.name}: meow!')
#
# def main() -> None:
#     dog:Dog = Dog('destroyer')
#     dog.bark()
#     cat:Cat = Cat('oiae')
#     cat.meow()
#
# if __name__ == '__main__':
#     main()

# ---------------------------------------super()
#
# from typing import override
#
# class Shape:
#     def __init__(self,name:str,sides:int)->None:
#         self.name = name
#         self.sides = sides
#
#     def describe(self)->None:
#         print(f'{self.name}({self.sides} sides)')
#
#     def shape_method(self)->None:
#         print(f'{self.name}: shape_method()')
#
# class Square(Shape):
#     def __init__(self, size:float):
#         super().__init__('Square', 4)
#         self.size = size
#     @override
#     def describe(self) ->None:
#         print(f'i am a {self.name} with a size of {self.size}')
#
#
# def main() -> None:
#     square: Square = Square(20)
#     square.describe()
#     square.shape_method()
# if __name__ == '__main__':
#     main()

# ----------------------------------@staticmethod
# when a method has nothing to do with the class its called a static method so it
# should be declared outside the class but if you want to keep it in side the class
# you write the decorator @staticmethod on top of it
# class Calculator:
#     def __init__(self,version:int)->None:
#         self.version = version
#
#     @staticmethod
#     def add(*numbers:float)->float:
#         return sum(numbers)
#
#     def get_version(self) -> int:
#         return self.version
# def main() -> None:
#     calc:Calculator = Calculator(version=1)
#     result: float = calc.add(1,2,3,4,56,7,8,9,9,0)
#     result: float = Calculator.add(1,2,3,4,56)
# if __name__ == '__main__':
#     main()

# ----------------------------------------@classmethod
# class method takes cls as argument instead of self and modifies
# class attributes whose change can be felt in all the instances
# of a class
#
# from typing import Self
# class Car:
#     LIMITER:int = 200
#
#     def __init__(self,brand:str, max_speed:int)->None:
#         self.brand = brand
#         self.max_speed = max_speed
#
#     @classmethod
#     def change_limit(cls,new_limit: int)-> None:
#         cls.LIMITER = new_limit
#
#     def display_info(self)->None:
#         print(f'{self.brand} (max{self.max_speed},limiter={self.LIMITER})')
#         if self.max_speed > self.LIMITER:
#             print(f'Pullover right now {self.brand}, stop right there!! 🚓🚨')
#
# def main() -> None:
#     bmw: Car = Car('BMW', 240)
#     toyota: Car = Car('Toyota',190)
#     lambo: Car = Car('lambo', 340)
#
#     bmw.display_info()
#     toyota.display_info()
#     lambo.display_info()
#
#     Car.change_limit(300)
#
#     bmw.display_info()
#     toyota.display_info()
#     lambo.display_info()
#
# if __name__ == '__main__':
#     main()

# -------------------------------factorymethod

# from typing import Self
# class Car:
#     LIMITER:int = 200
#
#     def __init__(self,brand:str, max_speed:int)->None:
#         self.brand = brand
#         self.max_speed = max_speed
#
#     @classmethod
#     def change_limit(cls,new_limit: int)-> None:
#         cls.LIMITER = new_limit
#
#     @classmethod
#     def autogenerate_max_speed(cls,brand:str) -> Self:
#         lowered: str = brand.lower()
#         max_speed:int = 200
#         if lowered == 'toyota':
#             max_speed = 270
#         elif lowered == 'bmw':
#             max_speed = 290
#         elif lowered == 'volvo':
#             max_speed = 300
#         return cls(brand, max_speed)
#
#
#     def display_info(self)->None:
#         print(f'{self.brand} (max{self.max_speed},limiter={self.LIMITER})')
#         if self.max_speed > self.LIMITER:
#             print(f'Pullover right now {self.brand}, stop right there!! 🚓🚨')
#
# def main() -> None:
#     volvo:Car = Car.autogenerate_max_speed('volvo')
#     volvo.display_info()
#
# if __name__ == '__main__':
#     main()

# -------------------------------------@abstractmethhod
# it basically creates a blueprint for a  class inheriting to follow
# or else python will throw a squiggly line and
# TypeError: Can't instantiate abstract class name without an
# implementation for abstract methods 'turn_off', 'turn_on'.
# ABC -> Abstract base class

# from abc import ABC, abstractmethod
#
# class Appliance(ABC):
#     def __init__(self, brand:str,version_no: int) -> None:
#         self.brand = brand
#         self.version_no = version_no
#         self.is_turned_on: bool = False
#
#     @abstractmethod
#     def turn_on(self)->None:
#         ...
#     @abstractmethod
#     def turn_off(self)->None:
#         ...
#
# class Lamp(Appliance):
#     def __init__(self, brand: str, version_no: int):
#         super().__init__(brand, version_no)
#
#     def turn_on(self) ->None:
#         if self.is_turned_on:
#             print(f'{self.brand} is already turned on!')
#         else:
#             self.is_turned_on = True
#             print(f'{self.brand} is now turned on!')
#     def turn_off(self) ->None:
#         if self.is_turned_on:
#             self.is_turned_on = False
#             print(f'{self.brand} is now turned off')
#         else:
#             print(f'{self.brand} is already turned off!')
#
# class Oven(Appliance):
#     def __init__(self, brand: str, version_no: int):
#         super().__init__(brand, version_no)
#
#     def turn_off(self) ->None:
#         raise NotImplementedError('Need to add functionality for turn_off()')
#
#     def turn_on(self) ->None:
#         raise NotImplementedError('Need to add functionality for turn_on()')
#
# def main() -> None:
#      oven:Oven = Oven('bosh',1)
#      lamp: Lamp = Lamp('Z-Lite',1)
#      lamp.turn_on()
#      lamp.turn_on()
#      lamp.turn_off()
#      lamp.turn_off()
# if __name__ == '__main__':
#     main()


# ------------------------------------Name Mangling
# basically public,private and protected in the case of python
# when you declare a attribute or a var by __attribute python internally
# changes its name to _class__attribute so we cant acess it even if we did
# self.__attribute we have to do self._class__attribute i dont kow if its a complete
# implementation like in java or c with separate keywords like private protected or not
# ALSO __YEAR makes it so you cant even use it in subclasses so to do that you have to
# declare it as _YEAR
#
# class Car:
#     __YEAR:int = 2000
#
#     def __init__(self,brand:str, fuel_type:str) -> None:
#         self.__brand = brand
#         self.__fuel_type = fuel_type
#         self.var:str = 'red'
#
#     def drive(self)->None:
#         print(f'driving: {self.__brand}')
#
#     def __get_description(self)-> None:
#         print(f'{self.__brand}: {self.__fuel_type}')
#
#     def display_colour(self)->None:
#         print(f'{self.__brand} is \'{self.var.capitalize()}\'')
#
# # class Toyota(Car):
# #     def __init__(self, brand: str, fuel_type: str):
# #         super().__init__(brand, fuel_type)
# #         self.var = 100 #this will cause AttributeError: 'int' object has no attribute 'capitalize'
# #         # because var was a str in the Car class which could have
# #         #been prevented if we used __var to make it protected
#
# def main() -> None:
#     car:Car = Car('toyota','electric')
#     car.drive()
#     # print(car.__get_description()) AttributeError: 'Car' object has no attribute '__get_description'.
#     car._Car__get_description() #Access to a protected member _Car__get_description of a class
#     print(car._Car__YEAR)
# if __name__ == '__main__':
#     main()

# -------------------------------------- built in functions
#

# ---------------------------------------print()
# # @overload
# # def print(*values: object,
# #           sep: str | None = " ",
# #           end: str | None = "\n",
# #           file: SupportsWrite[str] | None = None,
# #           flush: Literal[False] = False) -> None
#
# print('luke','von','emia',sep=',',end='.\n')
# print('2003','06','21',sep='/',end='.')
#
# lst:list[str] = ['orange','carrot','tomato','ginger']
# print(*lst,sep='\n')
'''
# ---------------------------------enumerate()

# elements: list[str] = ['A', 'B', 'C']
# i: int = 0

# for element in elements:
#     i += 1
#     print(f'{i}:{elements}')

# elements: list[str] = ['A', 'B', 'C']
# enumeration: enumerate = enumerate(elements, start=1)
# print(enumeration)
# print(list(enumeration))

# for i, element in enumerate(elements):
#     print(f'{i}:{element}')

# --------------------------------------round()

# a: float = 200.312399
# b: float = 18.12132
# c: float = 47.12312

# result: float = a + b + c
# print(round(result, 2))   # 265.56
# print(round(result, 1))  # 265.6
# print(round(result, 0))  # 266.0
# print(round(result, -1))  # 270.0
# print(round(result, -2))  # 300.0

# print(round(2.333333 ,1))

# ------------------------------------------range()

# my_range: range = range(1, 6)
# # the upper bound is exclusive not included i.e 6 is not included
# print(my_range)
# print(list(my_range))
# # range(1, 6)
# # [1, 2, 3, 4, 5]

# my_range1: range = range(0, 10, 2)  # steps by 2
# print(my_range1)
# print(list(my_range1))
# # range(0, 10, 2)
# # [0, 2, 4, 6, 8]

# my_range2: range = range(5)  # range is (0,5)
# print(my_range2)
# print(list(my_range2))
# # range(0, 5)
# # [0, 1, 2, 3, 4]

# my_range3: range = range(0, -5, -1)
# # if we want to count downwards we have to specify -1 in step which is 1 by default
# print(my_range3)
# print(list(my_range3))
# # range(0, -5, -1)
# # [0, -1, -2, -3, -4]


# # range objs are iterable

# for i in range(3):
#     print(i)

# -------------------------------------slice()
# used to create a slice object that is reuseable

# numbers: list[int] = [1, 2, 3, 4, 5]
# print(numbers[2:3])

# text: str = "Hello, world!"
# text2: str = "will i get a job?"

# first_three: slice = slice(0, 3)
# reverse_slice: slice = slice(None, None, -1)
# step_two: slice = slice(None, None, 2)

# print(text[first_three])
# print(text[reverse_slice])
# print(text[step_two])

# print(text2[first_three])
# print(text2[reverse_slice])
# print(text2[step_two])

# -------------------------------------globals()
# tells us every thing present in the global namespace , global scope everything that is visible their globals() returns a dir of every thing there

# from typing import Any

# text: str = "Bob"
# my_list: list[int] = [1, 2, 3]


# def func() -> None: ...


# my_globals: dict[str, Any] = dict(globals())

# for k, v in my_globals.items():
#     print(f"{k}:{v}")

# ----------------------------------------locals()
# locals() similar to globals when used inside a local scope returna a dictionary of every thing defined in that local scope

# but if you call locals() in the gllobal scope then the scope for locals is global scope and its out put is same as the globals output.

# def add(a: int, b: int) -> None:
#     result: int = a + b
#     print(f"{a} + {b} = {result}")

#     print("add() has:", locals())
#     print('add() can see:', globals())

# add(2, 3)

# 2 + 3 = 5
# add() has: {'a': 2, 'b': 3, 'result': 5}


# ---------------------------------------------all()
# all() is a helper function it takes an iterable and
# Return True if bool(x) is True for all values x in the iterable.
# If the iterable is empty, return True.
#
# wifi_enabled: bool = True
# has_electricity: bool = True
# has_subscription: bool = True
#
# #for example without all() 😔
# if wifi_enabled and has_subscription and has_electricity:
#     print('connected to internet')
#
# # but with all() 😎
# requirements: list[bool] = [wifi_enabled,has_electricity,has_subscription]
#
# if all(requirements):
#     print('connected to internet')
#
# peopele_voted: list[int] = [1,1,1,1,1,1,1,1,1,0]
#
# if not all(peopele_voted):
#     print('Some one didnt vote ...')
# else:
#     print('Every one has voted!')

#-----------------------------------------------any()
# Return True if bool(x) is True for any x in the iterable.
# If the iterable is empty,return False.

# people_voted: list[int] = [0,1,0,0,0]
#
# if any(people_voted):
#     print('Atleast one person voted')
# else:
#     print('No one voted...')

#-------------------------------------------isinstance()
# isinstance()
# Return whether an object is an instance of a class or of a subclass thereof.
# A tuple, as in ``isinstance(x, (A, B, ...))``, maybe given as the target to
# check against.This is equivalent to ``isinstance(x, A) or isinstance(x, B) or ...
# `` etc.

# number: int = 10
# pi: float = 3.14
# text: str = 'banana'
# my_list: list[int] = [1,2,3]
#
# print(isinstance(number,int)) #True
# print(isinstance(pi,float | int)) #True
# print(isinstance(text,str | int | dict)) #True
#
# class Animal:
#     ...
#
# class Cat(Animal):
#     ...
#
# print(isinstance(Cat(),Animal)) #True

# ------- made improved chat-bot in projects/











