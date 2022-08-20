# Project : Order a Pizza

# import os module
import os


def order(name, address, **toppings):
    print("Receipt:\n*****************************")
    print(f"Customer name:\t Mr.{name}")
    print(f"Address:\t {address}")

    price = 18.00
    for key, value in toppings.items():
        price = price + 2.00

    print("Total Price:\t", price)
    print("****************************\n")


# Main()
customer_name = input("Enter your name: ")
customer_address = input("Enter your address: ")

# Clear Screen
os.system('cls')

# Call the Function
order(name=customer_name, address=customer_address, cheese=True, ham=True)
