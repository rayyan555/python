
Grocery = {
    "Cornflakes": {"quantity": 15, "price": 100},
    "Muesli": {"quantity": 14, "price": 150},
    "Oats": {"quantity": 10, "price": 80},
    "Wheat Flakes": {"quantity": 5, "price": 75},
    "Granola": {"quantity": 8, "price": 125}
}

print("Grocery dictionary before updating:\n", Grocery)

choice = int(input("Enter your choice:\n1. Add additional quantity of cereals\n2. Update the price of the grocery\n3. Add new item\n"))

if choice == 1:
    item_name = input("Enter the grocery item name: ")
    quantity_added = int(input("Enter the quantity of the item to be added: "))
    Grocery[item_name]["quantity"] += quantity_added
elif choice == 2:
    item_name = input("Enter the grocery item name: ")
    new_price = float(input("Enter the new price of the item: "))
    Grocery[item_name]["price"] = new_price
elif choice == 3:
    item_name = input("Enter the new grocery item name: ")
    quantity = int(input("Enter the quantity of the new item: "))
    price = float(input("Enter the price of the new item: "))
    Grocery[item_name] = {"quantity": quantity, "price": price}
else:
    print("Invalid choice!")

print("\nItem details after updating:\n", Grocery)
