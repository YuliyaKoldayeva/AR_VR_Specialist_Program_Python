class Item:
    __item_name_field_length = 25
    __price_field_length = 11

    def __init__(self, sku: int, name: str, price: float, taxable: bool):
        """Instantiating the items"""
        self.__sku = sku
        self.__name = name
        self.__price = price
        self.__taxable = taxable

    @staticmethod
    def get_price_field_length(self):
        """Static method to refer the length of the price field"""
        return Item.__price_field_length

    @staticmethod
    def get_item_name_field_length(self):
        """Static method to refer the length of the item name field"""
        return Item.__item_name_field_length

    def get_item_sku(self):
        """This function returns a SKU."""
        return self.__sku

    def is_taxable(self):
        """This function returns a Boolean value of True or False depending if the taxable attribute is True or False."""
        return self.__taxable

    def get_item_base_price(self):
        """Returns the price and makes it available to user"""
        return self.__price

    def calculate_gst(self):
        """Returns GST tax amount"""
        if self.__taxable:
            return self.__price * .05
        else:
            return 0

    def calculate_qst(self):
        """Returns QST tax amount"""
        if self.__taxable:
            return self.__price * .09975
        else:
            return 0

    def get_item_total(self):
        """Returns the TOTAL amount to pay, Taxes included"""
        return Item.get_item_base_price(self) + Item.calculate_qst(self) + Item.calculate_gst(self)

    def print_item(self):
        """Returns the formatted description of the item"""
        __name_field_fill = "." * (Item.__item_name_field_length - len(self.__name))
        __price_field_fill = "." * (Item.__price_field_length - len('{:0,.2f}'.format(self.__price)))
        __taxable_field_fill = "T" * self.__taxable + " " * (1 - self.__taxable)

        self.__item_description = ("| {} | {} {} | $ {}{:0,.2f} |  {}  |".format(self.__sku,
                                                                                 self.__name,
                                                                                 __name_field_fill,
                                                                                 __price_field_fill,
                                                                                 self.__price,
                                                                                 __taxable_field_fill))
        return self.__item_description
