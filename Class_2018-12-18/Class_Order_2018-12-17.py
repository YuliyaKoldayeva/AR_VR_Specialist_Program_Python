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
        """ Instantiate Order object"""
        self.new_item={}
        self.purchase_date = ""
        self.items_list = []
        self.sequential = 0

    def AddItem(self, item_sku, item_name, item_price, taxable, quantity):
        """Create item description"""
        self.new_item = Item(item_sku, item_name, item_price, taxable).ItemDescription()
        self.new_item['purchase_date']= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.sequential +=1
        self.new_item['sequential'] = self.sequential
        self.quantity =quantity
        self.new_item['quantity'] = self.quantity
        self.items_list.append(self.new_item)
        return self.items_list


    def DeleteItem(self, sku_to_delete):
        """Delete some item from the list by SKU """
        self.sku_to_delete = sku_to_delete
        self.delete_confirmation = "The item "+ str(self.sku_to_delete)+ " was not found"

        for element in self.items_list:
            if self.sku_to_delete == element['item_sku']:
                print("sku ", self.sku_to_delete)
                print("element ", element)
                self.items_list.remove(element)
                self.delete_confirmation = "The item "+ str(self.sku_to_delete)+ " was successfully removed"
                break

        return self.delete_confirmation

    def ShowOrder(self):
        print("There are {} items in this order".format(len(self.items_list)))
        return self.items_list


test_order1 = CustomerOrder()

print(test_order1.AddItem(123456, "apple", 1.20, False, 2))
print(test_order1.AddItem(123457, "banana", 1.10, True, 5))
print(test_order1.AddItem(123458, "carrot", 1.30, False, 10))
print(test_order1.DeleteItem(123457))
print(test_order1.DeleteItem(3457))
print(test_order1.ShowOrder())
