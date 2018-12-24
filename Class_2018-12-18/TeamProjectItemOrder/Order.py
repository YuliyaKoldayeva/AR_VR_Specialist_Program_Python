# #from .Item import Item

class Item:
    __item_name_field_length = 25
    __price_field_length = 10

    def __init__(self, sku:int, name: str, price:float, taxable:bool):
        """Instantiating the items"""
        self.__sku = sku
        self.__name = name
        self.__price = price
        self.__taxable = taxable

    @staticmethod
    def get_price_field_length(self):
        return Item.__price_field_length

    @staticmethod
    def get_item_name_field_length(self):
        return Item.__item_name_field_length

    def print_item(self):
        """Printing the description of the item"""
        self.__taxable_field_fill = "T" * self.__taxable + " " * (1 - self.__taxable)
        self.__price_field_fill = "." * (Item.__price_field_length - len(str(self.__price)))
        self.__item_description = ("| {} | {} {} | $ {}{:0,.2f} |  {}  |".format(self.__sku,
                                                                               self.__name,
                                                                               ("." * (
                                                                               Item.__item_name_field_length - len(
                                                                                   self.__name))),
                                                                               self.__price_field_fill,
                                                                               self.__price,
                                                                               self.__taxable_field_fill))
        return self.__item_description

    def item_base_price(self):
        """Return gets the price and makes it available to user"""
        return self.__price

    def item_gst_amount(self):
        """Returns tax amount"""
        if self.__taxable:
            self.__gst_amount = self.__price * .05
        else:
            self.__gst_amount = 0
        return self.__gst_amount

    def item_pst_amount(self):
        """Returns tax amount"""
        if self.__taxable:
            self.__pst_amount = self.__price * .09975
        else:
            self.__pst_amount = 0
        return self.__pst_amount

    def get_item_total(self):
        self.__item_total = Item.item_base_price(self) + Item.item_pst_amount(self) + Item.item_pst_amount(self)
        return self.__item_total

    def get_item_sku(self):
        return self.__sku


class Order:
    __description_length = 63
    last_order_number_used = 0

    @staticmethod
    def get_last_order_number_used():
        return Order.last_order_number_used

    def __init__(self):
        """This instantiate new order"""
        print("\nThank you for shopping with us! \n")
        self.__items_list = []
        self.__order_number = Order.last_order_number_used + 1
        Order.last_order_number_used = self.__order_number

    def get_order_number(self):
        """This gives the order number"""
        return self.__order_number

    def add_item(self, item: Item):
        """This add new item to the order list"""
        self.__items_list.append(item)

    def remove_item(self, sku_to_delete: int):
        """This deletes an item by sku, returns True on successful delete."""

        for current_item in self.__items_list:

            if current_item.get_item_sku() == sku_to_delete:
                self.__items_list.remove(current_item)
                print("Item was removed")
                return True

        print("Item was not found")
        return False

    def get_price_subtotals(self):
        self.__subtotal_price = 0
        for current_item in self.__items_list:
            self.__subtotal_price += current_item.item_base_price()
        return self.__subtotal_price

    def get_pst_subtotals(self):
        self.__subtotal_pst = 0
        for current_item in self.__items_list:
            self.__subtotal_pst += current_item.item_pst_amount()
        return self.__subtotal_pst

    def get_gst_subtotals(self):
        self.__subtotal_gst = 0
        for current_item in self.__items_list:
            self.__subtotal_gst += current_item.item_gst_amount()
        return self.__subtotal_gst

    def get_total_to_pay(self):

        self.__total_to_pay = Order.get_price_subtotals(self) + Order.get_pst_subtotals(self) + Order.get_gst_subtotals(
            self)
        return self.__total_to_pay

    def final_info_printing(self, title_string, amount_to_display):

        self.__string_to_print = f"{title_string} {'.' * (40 - len(title_string))} $ {amount_to_display:0,.2f}"
        return self.__string_to_print

    def print_order_summary(self):

        fill_space_name = int(Item.get_item_name_field_length(self)) - len("ITEM NAME")
        fill_space_price = int(Item.get_price_field_length(self)) - len("PRICE")

        print("\n", " " * 40, "ORDER NUMBER : ", self.__order_number, "\n")
        print("| SKU      | ITEM NAME {} | PRICE   {} | TAX |".format(" " * fill_space_name,
                                                                        " " * fill_space_price))
        print("=" * Order.__description_length)

        for current_item in self.__items_list:
            print(current_item.print_item())
            print("-" * Order.__description_length)

        print("\n")
        print(Order.final_info_printing(self, "Subtotal", Order.get_price_subtotals(self)))
        print(Order.final_info_printing(self, "Tax GST", Order.get_gst_subtotals(self)))
        print(Order.final_info_printing(self, "Tax PST", Order.get_pst_subtotals(self)))
        print(Order.final_info_printing(self, "TOTAL", Order.get_total_to_pay(self)))
        print("\nYour order contains the total of {} items".format(len(self.__items_list)))
        print("\nThank you for your order")



user_answer = True
users_new_order = Order()
while user_answer == True:
    answer_string = input("Do you want to add something to your order? (Y/N) >> ").upper()
    if answer_string == "Y":
        sku = int(input("Please, enter 8-digits of item's SKU. >> "))
        while len(str(sku)) != 8:
            sku = int(input("Please, check the item's SKU, it should contain 8-digits. >> "))
        name = input("Please, enter the item's name >> ").title()
        price = float(input("Please, enter the item's price >> "))
        is_taxable = input("Is this item taxable? (Y/N) >> ").upper()
        if is_taxable == "Y":
            taxable = True

        else:
            taxable = False

        new_item = Item(sku, name, price, taxable)
        users_new_order.add_item(new_item)


    else:

        print("\nPlease, check your order before paying.\n")
        print(users_new_order.print_order_summary())

        want_to_change_answer =input("Do you want to delete some item from your order (Y/N) >> ").upper()
        if want_to_change_answer == "Y":
            sku_to_delete =int(input("Please, enter the SKU of item you want to delete >> "))
            users_new_order.remove_item(sku_to_delete)
            print(users_new_order.print_order_summary())



# a1 = Item(12345678, "first item", 2000.00, True)  # instantiating the first item
# a2 = Item(23456789, "second item", 300.00, False)  # instantiating the second item
# a3 = Item(34567891, "third item", 10.00, True)  # instantiating the third item
#
#
# print(a1.print_item())
# print(a2.print_item())
# print(a1.item_base_price())
# print(a1.item_gst_amount())
#
# new_order = Order()
#
# new_order.add_item(a1)  # adding the first item
# new_order.add_item(a2)  # adding the second item
# new_order.add_item(a3)  # adding the third item)
# print(new_order.print_order_summary())
# new_order.remove_item(12345678)
# print(new_order.print_order_summary())
