#Exercise 1: Create a List
#Create a list called fruits with the following items: "apple", "banana", "cherry", "date", and "elderberry".
#Print the list.
fruits=["apple","banana","cherry","date","elderberry"]
print(fruits)

#Exercise 2: Access List Elements
#Print the first and last items from the fruits list.
first_element=fruits[0]
last_element=fruits[-1]
print("First Element: ",first_element)
print("Last Element: ",last_element)
#Print the second and fourth items from the list
second_element=fruits[1]
fourth_element=fruits[3]
print("Second_Element: ",second_element)
print("Fourth Element: ",fourth_element)

#Exercise 3: Modify a List
#Replace "banana" in the fruits list with "blueberry".
#Print the modified list
fruits[1]="blueberry"
print("Modified List: ",fruits)

#Exercise 4: Add and Remove Elements
# Append "fig" and "grape" to the fruits list.
# Remove "apple" from the list.
# Print the final list.
fruits.append("fig")
fruits.append("grape")
fruits.remove("apple")
print("Final List: ",fruits)

# Exercise 5: Slice a List
# Slice the first three elements from the fruits list and assign them to a new list called first_three_fruits.
# Print first_three_fruits.
first_three_fruits=fruits[:3]
print("First three Fruits are: ",first_three_fruits)

#Exercise 6: Find List Length
#Find and print the length of the fruits list.
length_of_list=len(fruits)
print("Length of list is : ",length_of_list)

# Exercise 7: List Concatenation
# Create a second list called vegetables with the following items: "carrot", "broccoli", "spinach".
# Concatenate the fruits and vegetables lists into a new list called food.
# Print the food list.
vegetables=["carrot","broccoli","spinach"]
food=fruits+vegetables
print("Food list is: ",food)

# Exercise 8: Loop Through a List
# Loop through the fruits list and print each item on a new line.
for fruit in fruits:
    print(fruit)

# Exercise 9: Check for Membership
# Check if "cherry" and "mango" are in the fruits list. Print a message for each check.
if "cherry" in fruits:
    print("cherry is in the fruits list")
else:
    print("Cherry is not in the fruits list")

if "mango" in fruits:
    print("mango is in fruits list")
else:
    print("mango is not in fruits list")

# Exercise 10: List Comprehension
# Use list comprehension to create a new list called fruit_lengths that contains the lengths of each item in the fruits list.
# Print the fruit_lengths list.
fruit_lengths=[len(fruit) for fruit in fruits]
print("Length of each item in list: ",fruit_lengths)

#Exercise 11: Sort a List
# Sort the fruits list in alphabetical order and print it.
# Sort the fruits list in reverse alphabetical order and print it.
fruits.sort()
print("Fruits list in alphabetical_Order: ",fruits)

fruits.sort(reverse=True)
print("Fruits in reverse alphabetical order: ",fruits)

#Exercise 12: Nested Lists
# Create a list called nested_list that contains two lists: one with the first three fruits and one with the last three fruits.
# Access the first element of the second list inside nested_list and print it
nested_list=[fruits[:3], fruits[-3:]]
print("First and Second element from nested list: ",nested_list[1][0])

#Exercise 13: Remove Duplicates
# Create a list called numbers with the following elements: [1, 2, 2, 3, 4, 4, 4, 5].
# Remove the duplicates from the list and print the list of unique numbers.
numbers=[1,2,2,3,4,4,4,5]
unique_numbers=[]
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
print("Unique number list: ",unique_numbers)

#split and Join Strings
string="This is an Example string"
words=string.split()
new_string=" ".join(words)
print("Splitting of string: ",words)
print("joining the string: ",new_string)
