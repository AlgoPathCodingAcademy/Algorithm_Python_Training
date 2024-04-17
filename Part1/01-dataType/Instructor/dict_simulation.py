list_size = 100
def simple_hash(key):
    return sum(ord(c) for c in key) % list_size

keys = ["beauty", "joy", "computing"]
meanings = [
    "a combination of qualities, such as shape, color, or form, that pleases the aesthetic senses, especially the sight",
    "a feeling of great pleasure and happiness",
    "process of using computer technology to manage and process information"
]

# Assuming we're simulating a values_list as the hash table
values_list = [None] * list_size

# TODO:Populate the values_list with meanings based on hashed key indices
def populate_hashTable(keys, meanings):
    #TODO: Add your code
    for i in range(len(keys)):
        values_list[simple_hash(keys[i])] = meanings[i]
        
    return values_list

# TODO:get the meaning based on the key
def get_meaning(key):
    #TODO: Add your code
    index = simple_hash(key)
    return values_list[index]

populate_hashTable(keys,meanings)
# Testing the get_value function with the provided keys
test_keys = ["beauty", "joy", "computing"]
for key in test_keys:
    print(f"{key}: {get_meaning(key)}")

