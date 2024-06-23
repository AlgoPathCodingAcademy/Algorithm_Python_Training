#TODO
def is_valid_parentheses(s):
    #'(', ')', '{', '}', '[' and ']', 
    stack = []

#Test cases
print(is_valid_parentheses(["(","[",")","]"])) # False
print(is_valid_parentheses(["(",")","[","]","{","}"])) # True
print(is_valid_parentheses(["]"])) # False
print(is_valid_parentheses(["(","]",")"])) # False
