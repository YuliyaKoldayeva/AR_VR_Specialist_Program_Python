from Item import Item
from Order import Order

answer_string = ""
users_new_order = Order()
while answer_string != "FIN":
    answer_string = input("\nWhat do you want to do next?"+
                          "\n\tTo add a new item to your order type 'ADD'"+
                          "\n\tTo delete any item from your order type: 'DEL'"+
                          "\n\tTo complete your order type: 'FIN'"+
                          "\n\n\t\tPlease, type your choice HERE: >> ").upper()

    if answer_string == "ADD":
        print("\nPlease, give the following information: \n")

        while True:
            try:
                sku = int(input("Please, input the 8 digits of the item's SKU. >> "))
                while len(str(sku)) != 8:
                    sku = int(input("Please, check the item's SKU, it should contain 8 digits. >> "))
                break
            except ValueError:
                print("This field accepts only digits from 0 to 9 ")

        name = input("Please, input the item's name >> ").title()

        while True:
            try:
                price = float(input("Please, input the item's price >> "))
                break
            except ValueError:
                print("This field accepts only digits from 0 to 9 and a decimal point.")

        is_taxable = input("Is this item taxable? (Y/N) >> ").upper()

        while True:
            if is_taxable == "Y":
                taxable = True
                break
            elif is_taxable == "N":
                taxable = False
                break

            else:
                print("Your input is not valid, please, try again.")
                is_taxable = input("Is this item taxable? (Y/N) >> ").upper()


        new_item = Item(sku, name, price, taxable)
        users_new_order.add_item(new_item)

    elif answer_string == "DEL":

        print(users_new_order.print_order_summary())
        sku_to_delete = int(input("Please, enter the SKU of item you want to delete >> "))
        users_new_order.remove_item(sku_to_delete)
        print(users_new_order.print_order_summary())

    elif answer_string == "FIN":

        print(users_new_order.print_order_summary())

    else:
        print("It seams that you've chosen non-existent option. Please, try again.")
