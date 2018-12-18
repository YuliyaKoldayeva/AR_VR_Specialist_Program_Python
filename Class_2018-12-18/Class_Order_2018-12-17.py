import datetime

class Item:

    def __init__(self, item_sku, item_name, item_price, taxable):
        """ Instantiate Item object"""
        self.item_sku = item_sku
        self.item_name = item_name
        self.item_price = item_price
        self.taxable = taxable

    def ItemDescription(self):
        """Create item description"""
        return {"item_sku": self.item_sku, "item_name":self.item_name, "item_price":self.item_price, "taxable":self.taxable}

class CustomerOrder:
    def __init__(self):
        """ Instantiate Item object"""
        self.new_item={}
        self.purchase_date = ""
        self.items_list = []

    def AddItem(self, item_sku, item_name, item_price, taxable):
        """Create item description"""
        self.new_item = Item(item_sku, item_name, item_price, taxable).ItemDescription()
        self.new_item['purchase_date']= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.items_list.append(self.new_item)
        return self.items_list

test_order1 = CustomerOrder()

print(test_order1.AddItem(123456, "apple", 1.20, False))
print(test_order1.AddItem(123457, "banana", 1.10, True))
print(test_order1.AddItem(123458, "carrot", 1.30, False))
