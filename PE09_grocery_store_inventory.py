"""grocery_store_inventory.py

This assignment is to gain knowledge on hash tables using a linked list.
A grocery store inventory manager will be implemented for this exercise.
The program stores inventory items in hash tables.
Your task is to define hash table in linked list in a separate file such as "hash_grocery_store_inventory.py,"
where it contains FileNameClass class(es) with essential methods for data manipulation.
Note that "grocery_store_inventory.py" with the "main" method has already been provided.
As part of the assignment, compare the actual runtime of hash tables operation as N increases and analyze 
its performance in a short paragraph.

"""
# file name: hash_grocery_store_inventory.py
# class name: HashGroceryStoreInventoryClass
from hash_grocery_store_inventory import HashGroceryStoreInventoryClass

import time
import random
from random_word import RandomWords # NOTE: pip install random-word

x = random.random()
# Random price from $0.99 to $100.00


# You can use the following 2 lists for your testing purpose
item_list = ["apple", "banana", "milk", "bread", "butter", "cheese", "carrot", "pork", "beef",
                 "mushroom", "fish", "apple", "salt", "pepper", "olive oil", "eggs", "flour"]
item_price = ["$1.10", "$2.20", "$3.30", "$4.40", "$5.50", "$6.60", "$7.70", "$8.80", "$9.90",
                 "$10.10", "$11.11", "$2.20", "$12.12", "$13.13", "$14.14", "$15.15", "$16.16"]
search_item = "apple"

# You can use the following 2 lists for your analysis
# Note that it is difficult to validate its time complexity with the list defined above
# as the size of list is too small.
# ---- uncomment the following lines to populate more items for your analysis ----
item_price = [] # random prices to simulate the price for each grocery item
item_list  = [] # random words to simulate the grocery items
N = 500 # Test and report the results on {10, 50, 100, 250, and 500} 
r = RandomWords()
for i in range(0, N):
    # any random float between 50.50 to 500.50
    # don't use round() if you need number as it is
    x = round(random.uniform(0.99, 100.00), 2)
    item_price.append("$"+ str(x))
    item_list.append(r.get_random_word())
search_item = item_list[N//2] # pick one in the middle for a search item
# --------------------------------------------------------------------------------
def main():

        print("\n\n------ Hash table ------")
        htgsi = HashGroceryStoreInventoryClass(len(item_list))
        hash_table_insert_start_time = time.perf_counter()
        for i in range(len(item_list)):
                htgsi.insert_item(item_list[i], item_price[i])
        hash_table_insert_end_time = time.perf_counter()

        htgsi.print_items()
        
        hash_table_find_start_time = time.perf_counter()
        item = search_item
        print("price for %s : %s" % (item, htgsi.find_item(item)))
        item = "abc" # unknown item
        print("price for %s : %s" % (item, htgsi.find_item(item)))
        hash_table_find_end_time = time.perf_counter()
        
        #time summary:
        htInsertOp = hash_table_insert_end_time - hash_table_insert_start_time
        htLookupOp = hash_table_find_end_time - hash_table_find_start_time
        print("-insert: %f\n-lookup: %f\n" %(htInsertOp, htLookupOp))

if __name__ == "__main__":
        main()