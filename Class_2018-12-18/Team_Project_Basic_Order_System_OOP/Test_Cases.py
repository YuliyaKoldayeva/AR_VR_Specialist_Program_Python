from Item import Item
from Order import Order

a1 = Item(12345678, "first item", 2.00, True)# instantiating the first item
a2 = Item(23456789, "second item", 3.00, False)# instantiating the second item
a3 = Item(34567891, "third item", 10.00, True)# instantiating the third item

print("print item 1 ", a1.print_item())
print("print item 2 ", a2.print_item())
print("print item 3 ", a3.print_item())
print("\nbase price 1 = ", a1.item_base_price())
print("GST 1 = ", a1.item_gst_amount())
print("PST 1 = ", a1.item_pst_amount())
print("\nbase price 2 = ", a2.item_base_price())
print("GST 2 = ", a2.item_gst_amount())
print("PST 2 = ", a2.item_pst_amount())
print("\nTotal 1 = ", a1.get_item_total())
print("\nTotal 2 = ", a2.get_item_total())
print("\nTotal 3 = ", a3.get_item_total())

new_order1 = Order()
new_order2 = Order()
new_order3 = Order()

new_order1.add_item(a1)  # adding the first item to the first order
new_order2.add_item(a1)  # adding the first item to the second order
new_order2.add_item(a2)  # adding the second item to the second order
new_order3.add_item(a3)  # adding the third item to the third order
print("\nOrder 1 summary printed: ", new_order1.print_order_summary())
new_order2.remove_item(12345678) # removing the first item from the second order
print("\nOrder 2 summary printed: ", new_order2.print_order_summary())
print("\nOrder 3 summary printed: ", new_order3.print_order_summary())

for order in range(100):
    new_order = Order()

new_order.add_item(a1)  # adding the first item to the new order
new_order.add_item(a2)  # adding the second item to the new order
new_order.add_item(a3)  # adding the third item to the new order
print("\nOrder summary printed: ", new_order.print_order_summary())