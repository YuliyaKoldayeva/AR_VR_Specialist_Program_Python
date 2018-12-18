"""
Create an Item Class
sku , name, price of the item.
T/F values for taxable
"""
import datetime


class Item(object):

    def __init__(self, item_sku, item_name, item_price, taxable=True):
        self.__item_sku = item_sku
        self.__item_name = item_name
        self.__item_price = item_price
        self.__taxable = taxable

    def SetItemSku(self, new_item_sku):
        self.__item_sku = new_item_sku

    def GetItemSku(self):
        return self.__item_sku

    def SetItemName(self, new_item_name):
        self.__item_name = new_item_name

    def GetItemName(self):
        return self.__item_name

    def SetItemPrice(self, new_item_price):
        self.__item_price = new_item_price

    def GetItemPrice(self):
        return self.__item_price

    def SetItemTaxable(self, taxable=True):
        self.__taxable = taxable

    def GetItemTaxable(self):
        return self.__taxable

    def ItemDescription(self):
        return [self.__item_sku, self.__item_name, self.__item_price, self.__taxable]


class Order(Item):
    def __init__(self, purchase_date, item_quantity, item_sku, item_name, item_price, taxable=True):
        super().__init__(item_sku, item_name, item_price, taxable=True)
        self.purchase_date = purchase_date
        self.quantity = item_quantity
        self.sku = item_sku
        self.name = item_name
        self.price = item_price
        self.taxable = taxable
        self.item_dict = {}

    def OrderItemDescription(self):
        return {self.purchase_date:[self.quantity, self.sku, self.name, self.price, self.taxable]}

    def SetQuantity(self, new_quantity):
        self.quantity = new_quantity
        
    def GetQuantity(self):
        return self.quantity

    def BuyItem(self):
        self.item_dict[self.purchase_date] = Order.OrderItemDescription()
        return self.item_dict


"""
    def SetCancelItem(self, purchase_date):
        self.__item_list = self.__item_list.remove(purchase_date)

    def GetCancelItem(self, purchase_date):
        self.__item_list

"""

item_test1 = Item(1323, "apple", 134, False).ItemDescription()
item_test2 = Item(133, "Mac", 134, True).ItemDescription()
print(item_test1, item_test2)

order_test = Order(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 2, 1323, "apple", 134, False)

print(order_test.OrderItemDescription())
print(order_test.GetQuantity())
#print(order_test.BuyItem(1323, 1, "apple", 134, False))
#print(order_test.BuyItem(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 2, 1323, "apple", 134, False))

#print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))