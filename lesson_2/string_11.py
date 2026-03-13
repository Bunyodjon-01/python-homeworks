string = input("input string: ")
if any(char.isdigit() for char in string):
    print("String raqam o'z ichiga oladi")
else:
    print("Raqam yo'q")