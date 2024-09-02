def greet(name):
    return f"Hello, {name}!"

def add(a,b):
    return "Addition of a and b is: ",a+b

def subtract(a,b):
    return "Subtraction of a and b is: ",a-b

def multiply(a,b):
    return "Multiplication of a and b is: ",a*b

def division(a,b):
    return "Division of a and b is: ",a/b

# code to execute when the module run as a script
if __name__=="__main__":
    # this block will only run if this file is executed directly
    print("Executing module as a script")
    name="world"
    print(greet(name))