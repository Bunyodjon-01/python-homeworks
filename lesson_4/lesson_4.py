'''
2. Difference between continue and break in Python

The break statement is used to immediately terminate a loop. When break is executed, the loop stops completely and control moves to the code after the loop.

The continue statement is used to skip the current iteration of the loop. When continue is executed, the loop does not stop; instead, it jumps to the next iteration.

In short:

--break exits the loop

--continue skips one iteration and continues the loop

3. Difference between for loop and while loop

A for loop is used when the number of iterations is known in advance. It works by iterating over a sequence such as a list, range, or string.

A while loop is used when the number of iterations is not known beforehand. It continues running as long as a given condition remains true.

Key difference:

for loop is sequence-based

while loop is condition-based
4. Nested for loop explanation with example

A nested for loop is a loop placed inside another loop. The inner loop runs completely for each iteration of the outer loop.

This means the total number of executions equals:
outer loop iterations x inner loop iterations
'''

# 1
list1 = [1, 1, 2]
list2 = [2, 3, 4]
a = []
for i in list1:
    if i not in list2:
        a.append(i)
for j in list2:
    if j not in list1:
        a.append(j)
print(a)
###############################################
list1 = [1, 2, 3]
list2 = [4, 5, 6]
a = []
for i in list1:
    if i not in list2:
        a.append(i)
for j in list2:
    if j not in list1:
        a.append(j)
print(a)
##################################################
list1 = [1, 3, 4, 5]
list2 = [1, 1, 2, 3, 4, 2]
a = []
for i in list1:
    if i not in list2:
        a.append(i)
for j in list2:
    if j not in list1:
        a.append(j)
print(a)
# 2
n = 5
i = 0
while i < n:
    print(i**2)
    i += 1
# 3
txt = input("enter your text: ")
vowels = "aeiou"
result = ""
count = 0
i = 0

while i < len(txt):
    result += txt[i]
    count += 1

    if count == 3:
        if txt[i] in vowels and i + 1 < len(txt) - 1:
            result += txt[i + 1]
            i += 1
        if i < len(txt) - 1:
            result += "_"
        count = 0

    i += 1

print(result)
# 4
import random
while True:
    num = random.randint(1, 100)
    i = 1
    while i <= 10:
        a = int(input("enter guessed number: "))
        if a == num:
            print("You guessed it right!")
            break
        elif a > num:
            print("Too high!")
        else:
            print("Too low!")
        i += 1
    else :
        print("you lost...")
    reply = input("Want to play again?\n")

    if reply not in ['Y', 'YES', 'y', 'yes', 'ok' ]:
        break
# 5
while True:
    password = input("Enter password: ")

    if len(password) < 8:
        print("Password is too short.")
    elif not any(ch.isupper() for ch in password):
        print("Password must contain an uppercase letter.")
    else:
        print("Password is strong.")
        break
# 6
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num**0.5) + 1): 
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
