class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None
        
# unused
def getNeighbors(node):
    values = []
    keys = []
    for key in node.children:
        values.append(node.children[key])
        keys.append(key)
        
    return keys,values

def insert(root, word, level):
    # Base Case
    if level == len(word):
        root.is_word = True
        root.word = word
        return
    
    keys = root.children.keys()
    
    if word[level] not in keys:
        # create new root node
        newNode = TrieNode()
        # update the current node to include the new root
        root.children[word[level]] =newNode
        
        insert(newNode,word,level+1)
    else:
        # continue to insert
        insert(root.children[word[level]],word,level+1)
        
def search(root, word, level):
    if level == len(word):
        return root.is_word
    
    keys = root.children.keys()
    if word[level] not in keys:
        return False
    else:
        return search(root.children[word[level]], word, level + 1)
    
    
def startsWith(root, prefix, level):
    if level == len(prefix):
        return True
    
    keys = root.children.keys()
    if prefix[level] not in keys:
        return False
    else:
        return startsWith(root.children[prefix[level]], prefix, level + 1)

def printTrie(node):
    if not node:
        return
    # current node
    keys = node.children.keys()
    values = node.children.values()
    print("edges",keys)
    print("is_word",node.is_word)
    print("word",node.word)
    for value in values:
        printTrie(value)

word = "b"
root = TrieNode()
insert(root,word,0)
#printTrie(root)
insert(root,"bc",0)
printTrie(root)


print(search(root,"bd",0))
