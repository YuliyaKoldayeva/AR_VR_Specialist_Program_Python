import datetime

class Customer:
    def __init__(self, customer_name, customer_id):
        """Instantiating customer object"""
        self.customer_name = customer_name
        self.customer_id = customer_id

    def CustomerInfo(self):
        """Assemble customer info"""
        self.customer_info = {"customer_name": self.customer_name, "self.customer_id":self.customer_id}
        return self.customer_info

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
        self.purchase_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.items_list = []
        self.sequential = 0
        self.who_is_customer_info = {"Unknown", 0000000}

    def AddCustomerInfo(self, customer_name, customer_id):
        """Create item description"""
        self.who_is_customer_info = Customer(customer_name, customer_id).CustomerInfo()
        return self.who_is_customer_info

    def AddItem(self, item_sku, item_name, item_price, taxable, quantity):
        """Create item description"""
        self.new_item = Item(item_sku, item_name, item_price, taxable).ItemDescription()
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

    def PrintOrder(self):
        totals = CustomerOrder.TotalPrice(self)
        print("This order was made by {} on date: {}".format(self.who_is_customer_info["customer_name"],
                                                             self.purchase_date))

        print("The total price before taxes is " + str(self.total_raw_price))
        print("The total amount of taxes " + str(self.total_taxes))
        print("The total price with taxes is " + str(self.total_price))
        print("There are {} items in this order (listed below):".format(len(self.items_list)))
        for element in self.items_list:
            print(" {} !   {}   !   {}  !  {}   !  {}".format(element['item_sku'],
                  element['item_name'],
                  element['item_price'],
                  "T"*(element['taxable']==True),
                  element['quantity']))
        return "Thank you for your order"


    def TotalPrice(self):
        self.total_price = 0
        self.total_raw_price = 0
        self.total_taxes = 0

        for element in self.items_list:
            self.total_raw_price += element["item_price"] * element["quantity"]
            if element["taxable"]==True:
                self.total_taxes += element["item_price"]*0.15*element["quantity"]
        self.total_price = self.total_raw_price + self.total_taxes

        return "All amounts were calculated"


test_order1 = CustomerOrder()

print(test_order1.AddCustomerInfo("Someone", 987654)) # test to add customer info
print(test_order1.AddItem(123456, "apple", 1.20, False, 2)) # test to add 1st item to the order
print(test_order1.AddItem(123457, "banana", 1.10, True, 5)) # test to add 2nd item to the order
print(test_order1.AddItem(123458, "carrot", 1.30, True, 10)) # test to add 3rd item to the order
print(test_order1.DeleteItem(123457)) # test to delete 2nd item from the order
print(test_order1.DeleteItem(3457)) # test to delete non existent item from the order
print(test_order1.TotalPrice()) # test for total price
print(test_order1.PrintOrder()) # test to simply show the items in the order


