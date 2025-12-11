def gcd(a,b):
    
    lcd = 0    
    while True:
        remainder = a%b
        
        if remainder == 0:
            return b

        a = b
        b = remainder

# The output should be 3
print(gcd(1701,3768))

def gcd_list(nums):
    g = nums[0]
    for i in range(1, len(nums)):
        g = gcd(g, nums[i])
    return g
