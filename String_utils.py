def capitalize(string):
    return string.capitalize()

def reverse(string):
    return f"Reversed string: {string[::-1]}"

def count_vowels(string):
    vowels='aeiouAEIOU'
    return sum(1 for char in string if char in vowels)

def is_palindrome(string):
    string=string.lower().replace(" ","")
    return string==string[::-1]

