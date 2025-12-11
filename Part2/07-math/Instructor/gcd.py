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
