"""
starting my udemy course python date 3/3/2025

some usefull pycharm shortcuts
   shift + F10 -> run file
   shift + Alt + , or . -> increase or decrease font size
   ctrl + d -> duplicate the line
   ctrl + alt + l -> short-cut for formating
"""
# print("hello")
# python is case-sensitive so ✔️print()  and Print()❌
# print("hello"+" bob")

# variables and constants
# imvar = 'Variable'
# IMCONST = 'Constant'
# python has no true constant so
# you could still change the value of a constant

# Data type

# imaginary = 9j
# print(type(imaginary))

# Nummeric type
# number = -100
# percent = 1.50
# imaginary = 9j

# Bool types
# bool = True
# bool = False

# Sequence types
# numbers = [1,2,3] list
# coordinates = (2.5,1.0) tuple

# mapping types
# dictionary = {'Mario': 1,'Luigi': 2}

# set types
# raffel = {1,2,3,4} can change
# frozenraffel = frozenset({1,2,3,4}) cant change

# Type hints / anotations only for dev python dont care
# text : str  = '10' ✔️
# text : str = 10 will  give warning but python will still coppile

# Integer
# age: int = 21
# money: int = 0
# self_esteem: int = -100

# Float
# PI: float = 3.14

# Operators

# + - / *
# floor division //
# exponentioal **
# modulus %

# x: int = 2
# x += 2 # x = x + 2
# += -= *= **= /= //= %=

# comparision
# a == b
# a != b
# a > b
# a < b
# a >= b
# a <= b
# a > d > c

# logical
#  a == b and a == b
#  or
#  not((a==b))

# string
# name : str = 'omkar'
# name : str = "omkar"
#say i want to adress some thing thats mine
# name : str = "omkar's"  python be like :😊
# name : str = 'omkar's' python be like :😠
# so
# name : str = 'omkar\'s' python be like :😊👍

# quote : str = "he said:"hello"" python be like :😒👎
# quote : str = "he said:\"hello\"" python be like :😊👍
#
# str concatination
# print(name +" "+ quote)

# poem : str = """
# dhsbhd
# sdcshb
# sdcnjsk
# cdjk
# """

# type conversion
# txt_value = '100'
# int_value = 50
#
# print(txt_value + str(int_value) ) -> 10050
#
# also if trying to convert incompatible
# values we get value error for exp
#
# print(int('ten')) -> value error

# - made simple adder project

# Lists
# my_list: list = ['hello',2,8+9j,[22,False]]
# people : list[str] = ['bob','romane conti','natsuki subaru','rem']
# print(people[0])
# people.append('ram')
# people.remove('romane conti')
# people.pop() -> removes the last element
# people[0] = "ecidina"
# people.insert(2,'beti')

# Tuples
# tuples are immutable -> denoted by ,
# items : tuple = 1,4,True
# coord : tuple = 55,66
# new_tuple : tuple = ()

# crrt type annotation for tuple
# coordinates: tuple[float,bool] = (55.0,True)

# sets
# set has no order unlike lists
# they can not contain duplicates

# elements: set  = {True,99,'bob'}
# elements.add('James')
# elements.remove('bob')
# elements.pop() -> removes some thing randon
# elemts.clear() -> removes every thing
# elements.clear()
# after clear iinstead of printing an empty set it prints set()
# print(elements)
# to create a empty set we need to do this beacause doing {} will create a dict
# empty: set = set()
# same can be done for any data type

# frozenset -> immutable set
# things : frozenset = frozenset({1,33,33,45})
# print(things)

# dictnory
# weather: dict = {'time': '12:00','weather':{'morning':'rain',
#                                             'evening':'more rain'}}
# print(weather['weather']['morning'])
#
# users: dict = { 1: 'Luigi',2 : 'Mario'}
# users[3] = 'bob'
# del users[3]
# # users.pop(3)
# print("{} is a reletive of {}".format(users[2],users[1]))

# None data type
# no_value: None = None
#
# 🤨 union data type so it can be either or using '|'
# possible_user : str | None = 'str'
#
# - MADE MADLIB PROJECT
#
# conditional loops
#
# if-elif-else
#
#weather:str = 'cloudy'
#
# if weather == 'clear':
#     print("it's a nice day")
# elif weather == 'cloudy':
#     print("The weather could be cloudy.")
# else:
#     print("IDK....🙄")
#
# the order of the checks matter

# age : int = 22
#
# if age < 12:
#     print("your a teenager")
# elif age >= 18:
#     print("your a young adult") #python gets to here and prints which is wrong
# elif age > 25:
#     print("your an adult")
# else:
#     print("unknown number")
#
# Correct way ✔️
# if age > 25:
#     print("your an Adult")
# elif age >= 18:
#     print("your a young adult")
# elif age < 12:
#     print("your a Teenager")
# else:
#     print("unknown number")

# if-else shorthand
# cannot short had if elif and else ladder
# number:int = 0
# value:str = 'above 0' if number > 0 else '0 and below 0'

# for Loop




















