# 1.Numeric
a = float(input("insert number: "))
b = round(a, 2)

print(b)
# 2.Numeric
a = float(input("first number: "))
b = float(input("second number: "))
c = float(input("third number: "))

print(f"largest: {max(a, b, c)}")
print(f"smallest: {min(a, b, c)}")
# 3.Numeric
a = float(input("insert distance in km: "))
meter = 1000 * a
centimeter = 100 * meter

print("meter:", meter)
print("centimeter:", centimeter)
# 4.Numeric
a = float(input("insert number 1: "))
b = float(input("insert number 2: "))

main = a//b
rest = a % b
print("main:", main)
print("rest:", rest)
# 5.Numeric
Celsius = float(input("insert temperature in Celsius: "))
Fahrenheit = Celsius * 9/5 + 32

print("temperature in Fahrenheit: ", Fahrenheit)
# 6.Numeric
a = int(input("insert your number: "))
c = a % 10
print("last digit: ", c)
# 7.Numeric
a = int(input("insert your number: "))
b = a % 2

if b == 1 :
    print(f"your number: {a} is not even")
else :
    print(f"your number: {a} is even")
# 1.String
from datetime import datetime

current_year = datetime.now().year

name = input("your name: ")
birth_year = int(input("your birth year: ")) 
age = current_year - birth_year

print(f"{name} is {age} years old")
# 2.String
txt = 'LMaasleitbtui'
#      0123456789 
print(txt[1:3] + txt[5::2])
print(txt[::2])
# 3.String
word = input("insert your word: ")
length = len(word)
uppercase = word.upper()
lowercase = word.lower()

print("length: ", length)
print("uppercase: ", uppercase)
print("lowercase: ", lowercase)
# 4.String
word = input("insert your word: ")
reverse = word[::-1]
if word == reverse:
    print("your word is palindrome")
else:
     print("your word is not palindrome")

# 5.String
text = input("insert your word: ")

vowels = ""
consonants = ""

for char in text.lower():
    if char in "aeiou":  
        vowels += char
    elif char.isalpha():
        consonants += char
vowels_cn = len(vowels)
consonants_cn = len(consonants)
print("Vowels:", vowels_cn)
print("Consonants:", consonants_cn)

# 6.String
string1 = input("insert first word: ")
string2 = input("insert second word: ")
a = string2 in string1
print(a)
# 7.String
sentence = input("Input sentence: ")
replace_word = input("Replace: ")
with_word = input("with: ")
new_sentence = sentence.replace(replace_word, with_word)
print("output:", new_sentence)
# 8.String
word = input("insert your word: ")
last_char = word[-1]
first_char = word[0]
print("first char: ", first_char)
print("last char: ", last_char)
# 9.String
word = input("insert your word: ")
reverse = word[::-1]
print(reverse)
# 10.String
sentence = input("Input sentence: ")
words = len(sentence.split())
print(f"{words} ta so'z")
# 11.String
string = input("input string: ")
if any(char.isdigit() for char in string):
    print("String raqam o'z ichiga oladi")
else:
    print("Raqam yo'q")
# 12.String
words = input("So'zlarni kiriting, bo'shliq bilan ajrating: ").split()
result = "-".join(words)
print("Natija:", result)

# 13.String
words = input("So'zlarni kiriting: ")
result = words.replace(" ", "")
print("Natija:", result)

# 14.String
string1 = input("insert first word: ")
string2 = input("insert second word: ")
a = string2 == string1
print(a)
# 15.String

sentence = input("Enter a sentence: ")

words = sentence.split()

acronym = ""
for word in words:
    acronym += word[0].upper() 

print("Acronym:", acronym)

# 16.String
text = input("Enter a string: ")
char_to_remove = input("Enter a character to remove: ")
new_text = text.replace(char_to_remove, "")
print("Result:", new_text)

# 17.String

text = input("Enter a string: ")

vowels = "aeiouAEIOU"

new_text = ""
for char in text:
    if char in vowels:
        new_text += "*"
    else:
        new_text += char

print("Result:", new_text)

# 18.String
sententce = input("insert sentence: ")
startwith = sententce.split()[0]
endwith = sententce.split()[-1]
print("starts with:",startwith)
print("ends with:", endwith)
# 1.Boolean
username = input("insert your username: ")
password = input("insert your password: ")

if username =="":
    print("username can not be empty")
else :
    if password =="":
        print("password can not be empty")
    else :
        print("welcome")

# 2.Boolean
a = int(input("insert first number: "))
b = int(input("insert second number: "))

if a==b:
    print("a = b")
else:
    print("a != b")
# 3.Boolean
a = int(input("enter your number: "))
if a > 0 and a % 2 == 0: 
    print(f"{a} is positive and even")
else:
    print(f"{a} is not positive and even")

# 4.Boolean
a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if a != b and b !=c and a != c:
    print("they are different")
else :
    print("they are not all different")
# 5.Boolean
string1 = input("enter first word: ")
string2 = input("enter second word: ")
s1_len = len(string1)
s2_len = len(string2)
if s1_len == s2_len:
    print("both words have the same length")
else :
    print("both words don't have the same length")
# 6.Boolean
a = int(input("enter your number: "))
if a % 3==0 and a % 5 == 0:
    print(" it’s divisible by both 3 and 5")
else:
    print(" it’s not divisible by both 3 and 5")

# 7.Boolean
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a + b > 50.8:
    print("The sum is greater than 50.8")
else:
    print("The sum is not greater than 50.8")

#-------------------------------------------------
num = float(input("Enter a number: "))

if 10 <= num <= 20:
    print(f"{num} is between 10 and 20 (inclusive)")
else:
    print(f"{num} is NOT between 10 and 20")
