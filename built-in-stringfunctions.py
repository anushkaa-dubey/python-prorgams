#SEARCH
s="hello world"
print(s.find("world"))

#COUNT
print(s.count("o")) #output 2

#isDigit
d="12345"
print(d.isdigit())

#isalphanumeric
s = "abc123"
print(s.isalnum())  # Output: True

#Returns a string where a specified value is replaced with another value:

s = "hello world"
print(s.replace("world", "Python"))  # Output: hello Python

#Returns true if the string starts with the specified value:

s = "hello world"
print(s.startswith("hello"))  # Output: True

#Converts a string into upper case:

s = "hello world"
print(s.upper())  # Output: HELLO WORLD

#Converts the first character of each word to upper case:

s = "hello world"
print(s.title())  # Output: Hello World

#Splits the string at the specified separator, and returns a list:

s = "hello,world"
print(s.split(","))  # Output: ['hello', 'world']

# Returns a trimmed version of the string:
s = "  hello world  "
print(s.strip())  # Output: hello world
