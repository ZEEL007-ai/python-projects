menu = {
    'pizza': 110,
    'pasta': 100,
    'chole-bhature': 100,
    'meggie': 100
}

gender = input("Are You Boy OR Girl? : ")
if gender.lower() == 'boy':
    print("WELCOME SIR !")
else:
    print("WELCOME MA'AM !")

total_payment = 0

print("\nMenu:")
print("1) pizza           : 110\n2) pasta           : 100\n3) chole-bhature   : 100\n4) meggie          : 100")

# First item input
item = input("Please Enter item You Want To Order : ").lower()

if item in menu:
    qty = int(input(f"How many {item} you want? : "))
    total_payment += menu[item] * qty
else:
    print(f'{item} Not Available. Please order something else.')

# Repeat order loop
while True:
    another_item = input("Order anything else? (yes/no) : ").lower()
    if another_item == 'yes':
        item = input("Enter item you want to order: ").lower()
        if item in menu:
            qty = int(input(f"How many {item} you want? : "))
            total_payment += menu[item] * qty
        else:
            print(f'{item} Not Available.')
    elif another_item == 'no':
        print("OKAY..!!, THANK YOU :)")
        break
    else:
        print("INVALID CHOICE")

print(f'\nTOTAL BILL TO PAY IS : ₹{total_payment}')
