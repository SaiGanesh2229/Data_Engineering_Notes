# # text="Python Programming"
# # stripped_text=text.strip()
# # print(stripped_text)
# #
# # uppercase_text=text.upper()
# # starts_with_python=text.startswith("Python")
# # #print(starts_with_python)
# #
# # replace_text=text.replace("Programming", "Coding")
# # print(replace_text)
#
#
# # Integers
# # positive_int=22
# # negative_int=-3
# # zero=0
# # print(positive_int)
# # print(negative_int)
# # print( zero)
#
# num1=10
# num2=3
# #Addition
# print("Addition: ",num2+num1)
#
# #Subtraction
# print("Subtraction: ",num1-num2)
#
# #Multiplication
# print("Multiplication: ",num1*num2)
#
# #Division
# print("Division: ",num1/num2)
#
# #Floor
# print("Floor: ",num1//num2)
#
# #Modulo
# print("Modulo: ",num1%num2)
#
# #Exponentiation
# print("Exponentiation: ",num1**num2)

#TypeCasting
# num_int=1000
# num_str=str(num_int)
# print("int to str: ", num_str)
#
# num_float=100.987
# num_int=int(num_float)
# print("Float to int: ",num_int)

# Comparison Operators
# x=10
# y=5
# is_greater= x>y
# is_equal=x==y
# print("x>y", is_greater)
# print("x=y", is_equal)
#
# #Logical Operators
# a=True
# b=False
# and_operation= a and b
# print("a and b: ",and_operation)
# or_operation=a or b
# print("a or b: ",or_operation)
# not_operation= not a
# print("a not b: ",not_operation)
#
# #int to bool
# bool_from_int=bool(1)
# #Zero to bool
# bool_from_zero=bool(0)
# #Convert string to boolean
# bool_from_str=bool("Hello")
# #empty string to boolean
# bool_from_empty_str=bool("")
#
# print("Boolean to integer: ",bool_from_int)
# print("boolean from zero: ",bool_from_zero)
# print("boolean from string: ",bool_from_str)
# print("Bool from Empty str: ",bool_from_empty_str)

#creating Lists
# empty_list=[]
# numbers=[1,2,3,4,5]
# mixed_list=[1,"Hello", 3.14, True]
#
# print(empty_list)
# print(numbers)
# print(mixed_list)

#Indexing in list
# numbers=[1,2,3,4,5,6]
# print("Original List: ",numbers)
# first_element=numbers[0]=12
# third_element=numbers[2]=14
# last_element=numbers[-1]=16
#
# print("Modified List: ",numbers)
# print("length of list: ",len(numbers))
# print("First element: ",first_element)
# print("Third element: ",third_element)
# print("Last Element: ",last_element)

#Append the elements into the list
numbers=[1,2,3,4,5]
# numbers.append(6)
# numbers.extend([14,15,17])
# numbers.insert(2,10)
# print(numbers)
# numbers.remove(1)
# print(numbers)
#Slicing a List
# first_three=numbers[:3]
# middle_two=numbers[1:3]
# last_two=numbers[-2:]
#
# print("First Three :",first_three)
# print("Middle two : ", middle_two)
# print("Last two: ", last_two)

#Iterate over a list
# for num in numbers:
#     print(num)

# Creating a list of Squares using a list comprehension
squares=[x**3 for x in range(1,6)]
print(squares)



#dictionaries
empty_dict={}
person={
    "name": "Sai Ganesh",
    "age":22,
    "Email": "Saiganesh@example.in"
}
print(empty_dict)
print(person)

#Accessing Value
person["name"]="Mark Antony"
person["age"]=35
person["Email"]="antony.mark@example.in"
print(person)

#Adding a new key-value pair
person["address"]="123 MainStr"

del person["Email"]
print(person)

#Use dictionary methods
keys=person.keys()
values=person.values()
items=person.items()

print("Keys:",keys)
print("Values",values)
print("Items: ",items)

#Iterate Over Keys,values and key-value pairs
for key in person:
    print(person[key])
for value in person:
    print(value)
for key,value in person.items():
    print(key,":",value)