from Item import Item
import datetime

class Order:
    __description_length = 63
    __last_order_number_used = 0

    @staticmethod
    def get_last_order_number_used():
        """Static method to refer order number"""
        return Order.__last_order_number_used

    def __init__(self):
        """This instantiate a new order"""
        print("\nThank you for visiting our on-line store!")
        self.__items_list = []
        self.__order_number = Order.__last_order_number_used + 1
        Order.__last_order_number_used = self.__order_number

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
        """Returns price before tax amount for all  items"""
        self.__subtotal_price = 0
        for current_item in self.__items_list:
            self.__subtotal_price += current_item.item_base_price()
        return self.__subtotal_price

    def get_pst_subtotals(self):
        """Returns PST tax amount for all items"""
        self.__subtotal_pst = 0
        for current_item in self.__items_list:
            self.__subtotal_pst += current_item.item_pst_amount()
        return self.__subtotal_pst

    def get_gst_subtotals(self):
        """Returns GST tax amount for all items"""
        self.__subtotal_gst = 0
        for current_item in self.__items_list:
            self.__subtotal_gst += current_item.item_gst_amount()
        return self.__subtotal_gst

    def get_total_to_pay(self):
        """Returns price with both taxes included for all  items"""
        self.__total_to_pay = Order.get_price_subtotals(self) + Order.get_pst_subtotals(self) + Order.get_gst_subtotals(
            self)
        return self.__total_to_pay


    def final_info_printing(self, title_string, amount_to_display):
        """Returns the string to be printed to inform """
        self.__string_to_print = f"{title_string} {'.' * (40 - len(title_string))} $ {'.' * (11 - len('{:0,.2f}'.format(amount_to_display)))}{amount_to_display:0,.2f}"
        return self.__string_to_print

    def print_order_summary(self):
        """Generate order summary"""
        print("Here is your order summary:")
        fill_space_name = " " * (int(Item.get_item_name_field_length(self)) - len("ITEM NAME"))
        fill_space_price = " " * (int(Item.get_price_field_length(self)) - len("PRICE"))
        fill_space_order_number = "0"* int(8 - len(str(self.__order_number)))

        print("Purchase date: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("\n{} ORDER NUMBER: {}{}".format((" " * 40), fill_space_order_number,self.__order_number))
        print("\n| SKU      | ITEM NAME {} | PRICE   {} | TAX |".format(fill_space_name,
                                                                      fill_space_price))
        print("=" * Order.__description_length)

        for current_item in self.__items_list:
            print(current_item.print_item())

        print("="*Order.__description_length)
        print(Order.final_info_printing(self, "Subtotal", Order.get_price_subtotals(self)))
        print(Order.final_info_printing(self, "Tax GST", Order.get_gst_subtotals(self)))
        print(Order.final_info_printing(self, "Tax PST", Order.get_pst_subtotals(self)))
        print("")
        print(Order.final_info_printing(self, "TOTAL", Order.get_total_to_pay(self)))
        print("\nYour order contains the total of {} items".format(len(self.__items_list)))

        return print("\nThank you for your order")



# Test area

# a1 = Item(12345678, "first item", 2.00, True)# instantiating the first item
# a2 = Item(23456789, "second item", 3.00, False)# instantiating the second item
# a3 = Item(34567891, "third item", 10.00, True)# instantiating the third item
#
# new_order1 = Order()
# new_order2 = Order()
# new_order3 = Order()
#
# new_order1.add_item(a1)  # adding the first item
# new_order2.add_item(a1)  # adding the first item
# new_order2.add_item(a2)  # adding the second item
# new_order3.add_item(a3)  # adding the third item)
# print(new_order1.print_order_summary())
# new_order2.remove_item(12345678)
# print(new_order2.print_order_summary())
