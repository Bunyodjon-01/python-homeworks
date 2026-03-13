import random
while True:
    num = random.randint(1, 100)
    i = 1
    while i <= 5:
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
        print("you lost...\n it was", num)
    reply = input("Want to play again?\n")

    if reply not in ['Y', 'YES', 'y', 'yes', 'ok' ]:
        break
