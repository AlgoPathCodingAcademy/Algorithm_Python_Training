def is_valid_parentheses(s):
    #'(', ')', '{', '}', '[' and ']', 
    stack = []

    #input_list = ["(","[",")","]"]
    #input_list = ["(",")","[","]","{","}"]

    for item in s:
        if item == "(" or item == "[" or item == "{":
            stack.append(item)
        elif item == ")" or item == "}" or item == "]":
            if len(stack) == 0:
                return False
                
            if item == ")":
                if stack[len(stack) - 1] == "(":
                    stack.pop()
                else:
                    return False
                
            elif item == "}":
                if stack[len(stack) - 1] == "{":
                    stack.pop()
                else:
                    return False
                    
            elif item == "]":
                if stack[len(stack) - 1] == "[":
                    stack.pop()
                else:
                    return False
                    
    if len(stack) == 0:
        return True
    else:
        return False

#Test cases
print(is_valid_parentheses(["(","[",")","]"])) # False
print(is_valid_parentheses(["(",")","[","]","{","}"])) # True
print(is_valid_parentheses(["]"])) # False
print(is_valid_parentheses(["(","]",")"])) # False
