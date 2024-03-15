# Initializing an empty table
table = {}

# Inserting records with key-value pairs
table['Alice'] = 25
table['Bob'] = 30
table['Charlie'] = 22
table['David'] = 28

# The table now looks like this:
# {'Alice': 25, 'Bob': 30, 'Charlie': 22, 'David': 28}

# Checking if the table is empty
is_empty = len(table) == 0  # False, as the table has records

# Finding the value associated with a key
charlie_age = table['Charlie']  # 22

# Updating a record with a new value
table['David'] = 29
# The table is now: {'Alice': 25, 'Bob': 30, 'Charlie': 22, 'David': 29}

# Deleting a record based on a key
del table['Charlie']
# The table is now: {'Alice': 25, 'Bob': 30, 'David': 29}

# Checking if the table is full (assuming it has a maximum capacity)
# In this case, we assume it's not full.

# Enumerating (listing) all items in the table
for key, value in table.items():
    print(f'{key}: {value}')

# Output:
# Alice: 25
# Bob: 30
# David: 29
