dict_ = {"2":"abc","3":"def"}
letters = "23"

def getNeighbors(dict_, level, letters):
    return dict_[letters[level]]
    
def dfs(dict_, path, level, letters):
    if level == len(letters):
        print("path",path)
        return
    
    neighbors = getNeighbors(dict_, level, letters)
    for neighbor in neighbors:
        dfs(dict_, path + neighbor, level+1, letters)
        
dfs(dict_, "", 0,letters)
