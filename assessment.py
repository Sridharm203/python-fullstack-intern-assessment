# Q1 Student Attendance

attendance = ['P', 'A', 'P', 'P', 'A']

present_count = 0

for i in attendance:
    if i == 'P':
        present_count = present_count + 1

print("Total Present Students =", present_count)


# Q2 Login System

password = input("Enter Password: ")

if password == "admin123":
    print("Access Granted")
else:
    print("Access Denied")


# Q3 Electricity Bill

units = int(input("Enter Units: "))

if units <= 100:
    bill = units * 1
elif units <= 200:
    bill = (100 * 1) + ((units - 100) * 2)
else:
    bill = (100 * 1) + (100 * 2) + ((units - 200) * 3)

print("Total Bill =", bill)


# Q4 Name Formatter

name = input("Enter Full Name: ")

words = name.split()

for word in words:
    print(word.capitalize(), end=" ")

print()


# Q5 Mobile Recharge

amount = int(input("Enter Recharge Amount: "))

if amount == 199:
    print("Validity = 28 Days")
elif amount == 399:
    print("Validity = 56 Days")
else:
    print("Invalid Recharge Amount")


# Q6 E-commerce Cart

price1 = 100
qty1 = 2

price2 = 250
qty2 = 1

total = (price1 * qty1) + (price2 * qty2)

print("Total Bill =", total)


# Q7 Salary Calculator

salary = float(input("Enter Basic Salary: "))

hra = salary * 20 / 100
da = salary * 10 / 100

final_salary = salary + hra + da

print("HRA =", hra)
print("DA =", da)
print("Final Salary =", final_salary)


# Q8 OTP Verification

otp = 1234

for attempt in range(3):
    user_otp = int(input("Enter OTP: "))

    if user_otp == otp:
        print("OTP Verified Successfully")
        break
    else:
        print("Wrong OTP")

if user_otp != otp:
    print("Verification Failed")


# Q9 Banking System

balance = 1000

print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")

choice = int(input("Enter Choice: "))

if choice == 1:
    amount = int(input("Enter Deposit Amount: "))
    balance = balance + amount
    print("Updated Balance =", balance)

elif choice == 2:
    amount = int(input("Enter Withdraw Amount: "))

    if amount <= balance:
        balance = balance - amount
        print("Updated Balance =", balance)
    else:
        print("Insufficient Balance")

elif choice == 3:
    print("Current Balance =", balance)

else:
    print("Invalid Choice")


# Q10 Food Ordering System

pizza_price = 200
burger_price = 100
sandwich_price = 80

total = 0

for i in range(3):
    item = input("Enter Item Name: ")
    quantity = int(input("Enter Quantity: "))

    if item == "Pizza":
        total = total + (pizza_price * quantity)

    elif item == "Burger":
        total = total + (burger_price * quantity)

    elif item == "Sandwich":
        total = total + (sandwich_price * quantity)

    else:
        print("Item Not Available")

gst = total * 5 / 100
final_amount = total + gst

print("Total Amount =", total)
print("GST =", gst)
print("Final Amount =", final_amount)