# Student expense tracker 
Student = input("Enter your name : ")
Total=0
Item_total=0
Food_total=0 
while True:                         # CATEGORY LOOP

    category = input("Enter category: ")
    print("\033[1m", category, "\033[0m")

    item_total = 0

    while True:                     # ITEM LOOP

        item = input("Enter item: ")
        price = float(input("Enter price: "))

        item_total += price
        Total += price

        choice = input("Add another item? (yes/no): ")

        if choice.lower() == "no":
            break

    print("Total for", category, "=", item_total)

    Ask = input("Do you want to change category? (yes/no): ")

    if Ask.lower() == "no":
        break

print("Your total monthly expense =", Total)