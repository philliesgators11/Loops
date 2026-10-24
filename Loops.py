def print_menu():
    print("\nTaco Palace Menu")
    print("1. Taco")
    print("2. Burrito")
    print("3. Nachos")
    print("4. Soft Drink")
    print("5. Quit")
def get_price(selection):
    if selection == 1:
        return 3.50
    elif selection == 2:
        return 5.00
    elif selection == 3:
        return 4.50
    elif selection == 4:
        return 2.45
def main():
    print("Welcome to Taco Palace, please view the menu below and enter the number that represents your selection.")
    orders = []
    total = 0.0
    while True:
        print_menu()
        selection = int(input("Enter your selection: "))
        if selection == 5:
            break
        elif selection >= 1 and selection <= 4:
            if selection == 1:
                item = "Taco"
            elif selection == 2:
                item = "Burrito"
            elif selection == 3:
                item = "Nachos"
            else:
                item = "Soft Drink"
            print("You have selected a", item)
            price = get_price(selection)
            total = total + price
            orders.append(item)
        else:
            print("Invalid selection. Please choose a number 1 to 5.")
    print("\nYou ordered:", ", ".join(orders))
    print("Your total is $" + format(total, ".2f"))
main()

