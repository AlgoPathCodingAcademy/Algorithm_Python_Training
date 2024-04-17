#input format
#NNCode 1023: Hash Function for User Profile Lookup
'''
4
user123 Profile1
alice42 Profile2
john_doe Profile3
jane99 Profile4
3
jane99
alice42
user123
'''
def get_hash_value(string):    
    hash_value = 0
    for i in string:
        hash_value += ord(i)
    
    return hash_value % 100

profile_list = [None] * 100

frequency = int(input())
for i in range(frequency):
    input_list = input().split()
    #profile_list[get_hash_value(input_list[0])] = input_list[1]
    profile_list.insert(get_hash_value(input_list[0]),input_list[1])


frequency = int(input())
for n in range(frequency):
    userinput = input()
    totalhash = get_hash_value(userinput)

    print(totalhash)
    print(profile_list[totalhash])
