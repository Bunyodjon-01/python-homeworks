## Farm model
class Animals:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
        type_of_obj = type(self)
        self.name_of_obj = type_of_obj.__name__
    def __repr__(self):
        return f"{self.name_of_obj} is {self.color} and {self.weight} kg"
    def run(self):
        print(f"{self.name_of_obj} runs.")
    def eat(self):
        print(f"{self.name_of_obj} eats")
    def sleep(self):
        print(f"{self.name_of_obj} sleeps")
class Cow(Animals):
    def sound(self):
        print(f"{self.name_of_obj} sounds 'mu-mu'")
    def produce(self):
        print(f"{self.name_of_obj} produces milk.")
class Dog(Animals):
    def sound(self):
        print(f"{self.name_of_obj} barks")
    def task(self):
        print(f"{self.name_of_obj} guards.")
class Sheep(Animals):
    def sound(self):
        print(f"{self.name_of_obj} sounds 'baaa' ")
    def task(self):
        print(f"{self.name_of_obj} gives meat")


## Bank application

import random
class Account:
    def __init__(self, acc_num, name, balance):
        self.acc_num = acc_num
        self.name = name
        self.balance = balance
class Bank:
    def __init__(self):
        self.accounts = {}
        # Dastur boshlanishi bilan faylni 'a' rejimida ochamiz.
        # Agar fayl bo'lmasa, 'a' uni yaratadi. Agar bo'lsa, tegmaydi.
        with open("accounts.csv", "a") as f:
            pass 
        self.load_from_file()

    def load_from_file(self):
        with open("accounts.csv", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    acc_num, name, bal = parts
                    self.accounts[acc_num] = Account(acc_num, name, float(bal))
    def save_to_file(self):
        with open("accounts.csv", "w") as f:
            for acc in self.accounts.values():
                # Obyekt ichidagi ma'lumotlarni vergul bilan ajratib yozamiz
                f.write(f"{acc.acc_num},{acc.name},{acc.balance}\n")
    def withdraw(self, acc_num, amount):
        if acc_num in self.accounts:
            if self.accounts[acc_num].balance >= amount:
                self.accounts[acc_num].balance -= amount
                self.save_to_file()
                print(f"Muvaffaqiyatli! Qoldiq: {self.accounts[acc_num].balance} USD")
            else:
                print("Xato: Balansda mablag' yetarli emas!")
        else:
            print("Xato: Hisob topilmadi!")

    def view_account(self, acc_num):
        if acc_num in self.accounts:
            acc = self.accounts[acc_num]
            print(f"\n--- Hisob ma'lumotlari ---")
            print(f"Raqam: {acc.acc_num}\nEga: {acc.name}\nBalans: {acc.balance} USD")
        else:
            print("Xato: Hisob topilmadi!")

    def create_account(self, name, initial_deposit):
        # Unikal 5 xonali raqam yaratish
        while True:
            acc_num = str(random.randint(10000, 99999))
            if acc_num not in self.accounts:
                break
        
        # Yangi obyekt yaratish va lug'atga qo'shish
        new_acc = Account(acc_num, name, initial_deposit)
        self.accounts[acc_num] = new_acc
        
        # O'zgarishni faylga saqlash
        self.save_to_file()
        print(f"\nHisob ochildi! Sizning raqamingiz: {acc_num}")

    def deposit(self, acc_num, amount):
        if acc_num in self.accounts:
            self.accounts[acc_num].balance += amount
            self.save_to_file()
            print(f"Muvaffaqiyatli! Yangi balans: {self.accounts[acc_num].balance} USD")
        else:
            print("Xato: Hisob topilmadi!")
bank = Bank()

while True:
    print("\n" + "="*20)
    print("  ONLINE BANKING")
    print("="*20)
    print("1. Hisob ochish")
    print("2. Hisobni ko'rish")
    print("3. Pul qo'shish (Deposit)")
    print("4. Pul yechish (Withdraw)")
    print("5. Chiqish")
    
    choice = input("\nAmalni tanlang: ")
    
    if choice == "1":
        name = input("Ismingizni kiriting: ")
        amount = float(input("Boshlang'ich summa: "))
        bank.create_account(name, amount)
    elif choice == "2":
        num = input("Hisob raqamingizni kiriting: ")
        bank.view_account(num)
    elif choice == "3":
        num = input("Hisob raqamingizni kiriting: ")
        amount = float(input("Summani kiriting: "))
        bank.deposit(num, amount)
    elif choice == "4":
        num = input("Hisob raqamingizni kiriting: ")
        amount = float(input("Summani kiriting: "))
        bank.withdraw(num, amount)
    elif choice == "5":
        print("Xayr, salomat bo'ling!")
        break
    else:
        print("Noto'g'ri buyruq!")
    