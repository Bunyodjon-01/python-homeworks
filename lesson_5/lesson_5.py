## temperature.py
def convert_far_to_cel(f):
    return round((f - 32) * 5/9, 2)

def convert_cel_to_far(c):
    return round(c * 9/5 + 32, 2)

f = float(input("Enter a temperature in degrees F: "))
print(f"{f} degrees F = {convert_far_to_cel(f)} degrees C")

c = float(input("\nEnter a temperature in degrees C: "))
print(f"{c} degrees C = {convert_cel_to_far(c)} degrees F")


## invest.py

def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount *= (1 + rate)
        print(f"year {year}: ${amount:.2f}")

amount = float(input("Enter the amount: "))
rate = float(input("Enter the annual rate (e.g. 0.05): "))
years = int(input("Enter the years: "))

invest(amount, rate, years)


## factors.py
def factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(f"{i} is a factor of {n}")

n = int(input("Enter a positive integer: "))
factors(n)

## university.py

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
def stats(data):
    # def enrolment_stats(data):
    #     students = []
    #     tuition = []
    #     for i in data:
    #         students.append(i[1])
    #         tuition.append(i[2])
    #     return students, tuition
    students = [u[1] for u in data]
    tuition = [u[2] for u in data]

    def mean(values):
        return sum(values) / len(values)

    def median(values):
        v = sorted(values)
        m = len(v) // 2
        if len(v) % 2 == 0:
            return (v[m-1] + v[m]) / 2
        else :
            return v[m]

    Total_students = sum(students)
    Total_tuition = sum(tuition)

    student_mean = mean(students)
    student_median = median(students)

    tuition_mean = mean(tuition)
    tuition_median = median(tuition)

    result = (
         "*" * 30 +
        f"Total students: {Total_students}\n"
        f"Total tuition: {Total_tuition}\n\n"
        f"Student mean: {student_mean:.2f}\n"
        f"Student median: {student_median}\n\n"
        f"Tuition mean: {tuition_mean:.2f}\n"
        f"Tuition median: {tuition_median}\n\n"
         + "*" * 30 
    )
    return result
print(stats(universities))

## is_prime
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True
n = int(input("enter your number: "))
print(is_prime(n))