class Item():

    def __init__(self, item_sku, item_name, item_price, taxable):
        """ Instantiate Item object"""
        self.item_sku = item_sku
        self.item_name = item_name
        self.item_price = item_price
        self.taxable = taxable

    def ItemDescription(self):
        """Create item description"""
        self.item_description ={"item_sku": self.item_sku, "item_name":self.item_name, "item_price":self.item_price, "taxable":self.taxable}
        return self.item_description