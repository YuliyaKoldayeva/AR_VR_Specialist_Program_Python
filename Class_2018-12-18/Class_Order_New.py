import datetime

class Item():

    def __init__(self):
        """ Instantiate Item object"""
        self.item_description={}

    def ItemDescription(self, item_sku, item_name, item_price, taxable=True):
        self.item_description = {"item_sku":item_sku,
                                 "item_name":item_name,
                                 "item_price":item_price,
                                 "taxable":taxable}
        return self.item_description


class CustomerOrder():

    def __init__(self):
        """ Instantiate Order object"""
        self.new_item={}
        self.purchase_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.items_list = ["initial"]

    def AddItem(self, item_sku, item_name, item_price, taxable):
        """Create item description"""
        new_item = Item()
        self.new_item = new_item.ItemDescription(item_sku, item_name, item_price, taxable)
        updated_order= (self.items_list).append(self.new_item)
        return (updated_order)

test_order1 = CustomerOrder()

print(test_order1.AddItem(123456, "apple", 1.20, False))
print(test_order1.AddItem(123457, "banana", 1.10, True))
print(test_order1.AddItem(123458, "carrot", 1.30, False))

