#Alex Bello
#2/5/2020
#Prints Statements about different characteristics of a string value

print("Enter a string value of more than one word.")
string = input("What are your words?")
print(f"So your words are {string}")
print(len(string))
if string[0] == 'p':
    print("The first character is p")
if string[16] == 'l':
    print("The last character is l")

print(string.upper())
print("This is your string all upper case.")
print(string.title())
print("This is your string in all title case.")
print(string.isalpha())
print("Your string is not in alphabeticle order.")
print(string.split())
print("This is the string split into individual strings.")
print(string.lower())
print("This is the string in all lower case.")

