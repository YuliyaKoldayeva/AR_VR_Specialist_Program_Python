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


# Testing the instantiation of item from the class Item

test_item1 = Item(123456, "apple", 1.20, False)

print(test_item1.ItemDescription())