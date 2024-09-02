#Tuples
#Creating a tuple of colors
colors= ("red","green","blue")

#Accessing elements of tuple
print("First color: ",colors[0])
print("Last color: ",colors[-1])

#Length of the tuple
tuple_length=len(colors)
print("Length of the tuple:",tuple_length)

#Looping through the tuple
print("tuple elements")
for color in colors:
    print(color)


#Sets
fruits={"apple","banana","orange"}
fruits.add("grape")
print(fruits)
#removing an element from a set
fruits.remove("banana")

print("Is 'apple in fruits' ?","apple" in fruits)
print("Is 'banana in fruits' ?","banana" in fruits)

set_length=len(fruits)
print("Number of elements in the set: ",set_length)
#looping through sets
print("Set elements")
for fruit in fruits:
    print(fruit)


# List of dictionaries representing students information
students=[
    {"name":"Alice","age":20,"grade":"A"},
    {"name":"Bob","age":22,"grade":"B"},
    {"name":"Charlie","age":21,"grade":"C"},
    {"name":"David","age":23,"grade":"B"}
]
#Accessing and manipulating individual records
print(students[0]["name"]) #Accessing name of the first student
students[1]["age"]=24 #Modifying the age of second student

#Adding a new student record to the list
new_student={"name":"Eve","age":19,"grade":"A"}
students.append(new_student)

#iterating through the list of students
for student in students:
    print(f"Name:{student['name']},Age:{student['age']},Grade:{student['grade']}")