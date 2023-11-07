# YOUR CODE STARTS HERE
from data import warehouse1, warehouse2
import re

# Get the user name
name = input("Please insert yout name: ").capitalize()

# Greet the user
print(f"Heloo, {name}")

# Show the menu and ask to pick a choice
print("menu: \n1. List items by warehouse. \n2. Search an item and place an order. \n3. Quit.\n")
choice = input("Please choice from menu: ")

# If they pick 1
if choice == "1":
    for item in warehouse1:
        print(item)
    for item in warehouse2:
        print(item)
# Else, if they pick 2
elif choice =="2":
    item_name = input("Enter the item name you want to search for: ")
    item_in_warehouse1 = [item for item in warehouse1 if re.match(fr".*{re.escape(item_name)}.*", item, re.IGNORECASE)]
    item_in_warehouse2 = [item for item in warehouse2 if re.match(fr".*{re.escape(item_name)}.*", item, re.IGNORECASE)]
    amount_of_items_in_warehouse1 = len(item_in_warehouse1)
    amount_of_items_in_warehouse2= len(item_in_warehouse2)
    total_amount_of_items = amount_of_items_in_warehouse1 + amount_of_items_in_warehouse2
    print(f"The total amount of {item_name} in warehouse1: ", len(item_in_warehouse1))
    print(f"The total amount of {item_name} in warehouse2: ", len(item_in_warehouse2))
    
    locations = []
    if amount_of_items_in_warehouse1 > 0:
       locations.append("Warehouse 1")
    if amount_of_items_in_warehouse2 > 0:
        locations.append("Warehouse 2")
    if locations:
        print(f"{item_name} is in ", locations)
    else:
        print(f"{item_name} is not in stock ")
    highest_count = max(amount_of_items_in_warehouse1, amount_of_items_in_warehouse2)
    highest_count_warehouse = "Warehouse 1" if highest_count == amount_of_items_in_warehouse1 else "Warehouse 2" if highest_count == amount_of_items_in_warehouse2 else None
    if highest_count_warehouse:
        print(f"The warehouse with the highest amount of {item_name} is {highest_count_warehouse} with {highest_count} items.")
    order_choice = input("Do you want to place an order for this item? (yes/no): ").lower()
    if order_choice == "yes":
        user_amount = int(input("How many do you want: "))
        if user_amount <= total_amount_of_items:
            print(f"Your order:  {user_amount} of {item_name} has been placed.")
        elif user_amount > total_amount_of_items:
            print("Your order is higher than the total available")
            re_choice = input("Do you want to order the maximum available, instead?  (yes/no): ").lower()
            if re_choice == "yes":
                print(f"Your order:  {user_amount} of {item_name} has been placed.")
            else:
                pass
    else:
        pass


# Else, if they pick 3
elif choice =="3":
    pass

# Else
else:
    print("The operation entered is not valid.")
    
# Thank the user for the visit
print(f"{name} ,thank you for the visit.")
