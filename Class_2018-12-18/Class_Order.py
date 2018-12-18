import datetime

class Item():

    def __init__(self, item_sku, item_name, item_price, taxable=True):
        """ Instantiate Item object"""
        self.item_sku = item_sku
        self.item_name = item_name
        self.item_price = item_price
        self.taxable = taxable

    def ItemDescription(self):
        """Create item description"""
        return {"item_sku": self.item_sku, "item_name":self.item_name, "item_price":self.item_price, "taxable":self.taxable}


class CustomerOrder(Item):

    def __init__(self, item_sku, item_name, item_price, taxable):
        """ Instantiate Order object"""
        super().__init__(item_sku, item_name, item_price, taxable)
        self.purchase_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.items_list = ["initial"]
        self.new_item_description = ""


    def ItemDescription(self):
        """Create item description"""

        self.new_item_description = [{"purchase_date": self.purchase_date,
                                "item_sku": self.item_sku,
                                "item_name": self.item_name,
                                "item_price": self.item_price,
                                "taxable": self.taxable}]
        return self.new_item_description

    def AddItem(self):
        """Create item description"""
        self.items_list +=CustomerOrder.ItemDescription(self)
        return self.items_list



test_order1 = CustomerOrder(123456, "apple", 1.20, False)
test_order2 = CustomerOrder(123457, "banana", 1.10, True)
test_order3 = CustomerOrder(123458, "carrot", 1.30, False)

print(test_order1.ItemDescription())
print(test_order2.ItemDescription())
print(test_order3.ItemDescription())

print(test_order1.AddItem())
print(test_order2.AddItem())
print(test_order3.AddItem())