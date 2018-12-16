"""
Create an Item Class
sku , name, price of the item.
T/F values for taxable
"""
import datetime

class Item():
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
        return self.__itemprice

    def SetItemTaxable(self, taxable=True):
        self.__taxable = taxable

    def GetItemTaxable(self):
        return self.__taxable

    def ItemDescription(self):
        return [self.__item_sku, self.__item_name, self.__item_price, self.__taxable]




class Order():

    def __init__(self, purchase_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
        self.purchase_date = purchase_date
        self.item_dict = {}
        self.item_info = ""


    def BuyItem(self, item_description):
        self.item_dict[self.purchase_date] = item_description
        return self.item_dict



"""
    def SetCancelItem(self, purchase_date):
        self.__item_list = self.__item_list.remove(purchase_date)

    def GetCancelItem(self, purchase_date):
        self.__item_list


    item1 = Item('apple', 7.8)
    item2 = Item('pear', 5)

    user1 = User('John')

    user1.BuyItem(item1, 5)
    print("user1 cart0 have: %s" % user1.GetCart(0).ShowCart())

    user1.BuyItem(item2, 6)
    print("user1 cart0 have: %s" % user1.GetCart(0).ShowCart())


    user1.AddCart()
    user1.BuyItem(item1, 5, 1)
    print("user1 cart1 have: %s" % user1.GetCart(1).ShowCart())

"""

item_test1 = Item(1323, "apple", 134, False).ItemDescription()
item_test2 = Item(133, "Mac", 134, True).ItemDescription()
print(item_test1, item_test2)

order_test = Order()

order_test.BuyItem(item_test1)
order_test.BuyItem(item_test2)

print(order_test)