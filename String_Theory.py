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
new_string = ""

for i in range(0, len(string)):
    if i != 2:
        new_string = new_string + string
print("After removing the third letter in the string it becomes : " + new_string)

print(string.upper())
print(string.title())
print(string.isalpha())
print(string.split())

