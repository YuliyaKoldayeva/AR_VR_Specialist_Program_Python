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
        print("\nStarting a new order.\nThank you for visiting our on-line store!")
        self.__items_list = []
        self.__purchase_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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
            self.__subtotal_price += current_item.get_item_base_price()
        return self.__subtotal_price

    def get_qst_subtotals(self):
        """Returns QST tax amount for all items"""
        self.__subtotal_qst = 0
        for current_item in self.__items_list:
            self.__subtotal_qst += current_item.calculate_qst()
        return self.__subtotal_qst

    def get_gst_subtotals(self):
        """Returns GST tax amount for all items"""
        self.__subtotal_gst = 0
        for current_item in self.__items_list:
            self.__subtotal_gst += current_item.calculate_gst()
        return self.__subtotal_gst

    def get_total_to_pay(self):
        """Returns price with both taxes included for all  items"""
        self.__total_to_pay = Order.get_price_subtotals(self) + \
                              Order.get_qst_subtotals(self) + \
                              Order.get_gst_subtotals(self)
        return self.__total_to_pay

    def final_info_formatting(self, title_string, amount_to_display):
        """Returns the formated string to be printed to inform the final amounts of taxes, before & after taxes"""
        self.__string_to_print = f"{title_string} " \
                                 f"{'.' * (40 - len(title_string))} " \
                                 f"$ {'.' * (11 - len('{:0,.2f}'.format(amount_to_display)))}" \
                                 f"{amount_to_display:0,.2f}"
        return self.__string_to_print

    def right_alignment(self, string_to_align):
        return " " * (Order.__description_length - len(str(string_to_align)))+str(string_to_align)


    def print_order_summary(self):
        """Generate order summary"""
        print("\nHere is your order summary:")
        __fill_space_name = " " * (int(Item.get_item_name_field_length(self)) - len("ITEM NAME"))
        __fill_space_price = " " * (int(Item.get_price_field_length(self)) - len("PRICE"))
        __fill_space_order_number = "0"* int(8 - len(str(self.__order_number)))
        __purchase_date_string = "{}{}".format("Purchase date: ", self.__purchase_date)
        __purchase_order_string = "{}{}{}".format("ORDER NUMBER: ", __fill_space_order_number, self.__order_number)

        print(Order.right_alignment(self,__purchase_date_string))
        print(Order.right_alignment(self,__purchase_order_string))

        print("=" * Order.__description_length) # print separator
        print("| SKU      | ITEM NAME {} | PRICE  {} | TAX |".format(__fill_space_name,
                                                                        __fill_space_price))
        print("=" * Order.__description_length)  # print separator

        for current_item in self.__items_list:
            print(current_item.print_item())

        print("="*Order.__description_length) # print separator
        print(Order.final_info_formatting(self, "Subtotal", Order.get_price_subtotals(self)))
        print(Order.final_info_formatting(self, "Tax GST", Order.get_gst_subtotals(self)))
        print(Order.final_info_formatting(self, "Tax QST", Order.get_qst_subtotals(self)))
        print(Order.final_info_formatting(self, "TOTAL", Order.get_total_to_pay(self)))

        return "\nYour order contains {} items".format(len(self.__items_list))
