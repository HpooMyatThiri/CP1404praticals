'''
total_price = 0
get item_counts
for items in range for item_counts
    get item_price
    total_price += item_price
if total_price > 100
    total_price = total_price - total_price * 0.1
display "Total Price for" item_counts "item is $" total_price
'''

total_price = 0
item_counts = int(input("Number of items: "))
for items in range(item_counts):
    item_price = float(input("Item price: "))
    total_price += item_price
if total_price > 100:
    total_price = total_price - total_price * 0.1
print(f"Total Price for {item_counts} items is ${total_price:.2f}")

