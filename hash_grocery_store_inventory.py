class HashGroceryStoreInventoryClass:

    # Node class for linked list
    class Node:
        def __init__(self, item, price):
            self.item = item
            self.price = price
            self.next = None # Pointer to next node

    # Initialize hash table
    def __init__(self, table_size):
        self.table_size = table_size 
        self.table = [None] * table_size # Empty list of size of table to store linked lists

    # Hash function for strings as keys
    def hash_func(self, key):
        # Hash variable for ASCII values
        hash_sum = 0

        # Iterate though each character in key
        for char in key:
            # Convert to ASCII value and add to sum
            hash_sum += ord(char)

        # Return using modulo to ensure index fits
        return hash_sum % self.table_size
    
    # Insert item
    def insert_item(self, item, price):
        # Get item hash index
        index = self.hash_func(item)

        # Check if slot is empty. 
        if self.table[index] is None:
            # Create new node and store item at index
            self.table[index] = self.Node(item, price)

            # Exit function
            return
        
        # Index to start loop at
        current = self.table[index]

        # Iterate through linked list
        while current:
            # Update item price if item exists
            if current.item == item:
                current.price = price

                # Exit function
                return
            
            # If last node, exit loop
            if current.next is None:
                break
            
            # Go to next node
            current = current.next

        # Add new node at end of linked list
        current.next = self.Node(item, price)


    # Output all items in hash table
    def print_items(self):
        # Iterate through table
        for slot in self.table:
            print("[", end = " ") # Opening bracket
            current = slot # Start from first node in list

            # Loop while node exists
            while current:
                # Print item name and price
                print(f"{current.item}, {current.price}", end = " ")
                # Go to next node
                current = current.next

            print("]") # Closing bracket

    # Output price of specified item
    def find_item(self, key):
        # Get hash index for search key
        index = self.hash_func(key)
        # Start from first node in linked list
        current = self.table[index]

        # Loop while node exists
        while current:
            # If current items equals key, output item price
            if current.item == key:
                return current.price
            
            # Move to next node
            current = current.next

        # Return None if item not found
        return None 