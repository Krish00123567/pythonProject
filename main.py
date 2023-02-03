def main():
    # Initializing menu with prices
    menu = {"Palak Paneer": 200, "Sada Dhosa": 900, "Cheese Dhosa": 900, "Lion Dhosa": 500}

    # Initializing total bill to 0
    total_bill = 0

    # Running a loop until the user wants to exit
    while True:
        # Printing the menu items
        print("JJ Dhosa Menu:")
        for item, price in menu.items():
            print(f"{item}: Rs. {price}")

        # Taking input for item and quantity
        item = input("Enter the item name: ")
        quantity = int(input("Enter the quantity: "))

        # Checking if the item is present in the menu
        if item in menu:
            # Adding the price of the item to the total bill
            total_bill += menu[item] * quantity
            print(f"{quantity} {item} added to the bill")
        else:
            print("Item not found in the menu")

        # Asking the user if they want to add more items
        add_more = input("Do you want to add more items? (yes/no) ")
        if add_more.lower() == "no":
            break

    # Printing the final bill
    print(f"Total Bill: Rs. {total_bill}")

if __name__ == '__main__':
    main()
