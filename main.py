# single_quote_String='This is a single quoted string - " hey "'
#
# double_quote_string="This is a double Quoted string 'Hey' "
#
# multi_line_str=''' this is
# a multiple line string
# '''
# print(single_quote_String)
# print(double_quote_string)
# print(multi_line_str)
#
# greeting='hello'
# name='Alice'
# full_greeting=greeting+' '+name
# print(full_greeting)
#
# # using format() method
# greeting='hello'
# name='Alice'
# formatted_greeting="{}, {}! ".format(greeting,name)
#
# #Using Format() method
# greeting='hello'
# name='Alice'
# f_str=f"{greeting},{name}!"
# print(f_str)


# from mypackage import * #arithmetic
# # from mypackage import geometry
# print("Addition:",arithmetic.add(100,100))
# print("Subtraction: ",arithmetic.subtract(100,50))
# print("Division: ",arithmetic.division(20,10))
# print("Area of circle: ",geometry.area_of_circle(6))
# print(geometry.perimeter_of_circle(6))
# print(geometry.area_of_rectangle(10,8))
# print(geometry.perimeter_of_rectangle(9,10))


# Keyword Arguments
def describe_pet(pet_name,animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}")

# using keyword arguments
describe_pet(animal_type="Cat",pet_name="Whiskers")
describe_pet(pet_name="Rover")


# Arbitrary Positional Arguments
def make_pizza(size,*toppings):
    print(f"Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# Calling with an arbitrary positional arguments
make_pizza(12,"Pepperoni","mushrooms","green peppers")

# Arbitrary keyword arguments
def build_profile(first,last,**user_info):
    return {"first name": first, "Last name":last,**user_info}
#Calling with arbitrary keyword arguments
user_profile=build_profile("john","doe",location="New york",field="Engineering")
print(user_profile)