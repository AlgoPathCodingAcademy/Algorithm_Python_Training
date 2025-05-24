numbers = "23"
hashTable = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"}

result = []

def dfs_work(path,level):
    if level == len(numbers):
        result.append(path)
        return
    letters = hashTable[numbers[level]]
    for letter in letters:
        dfs_work(path+letter,level + 1 )
        
dfs_work("",0)

print(result)
