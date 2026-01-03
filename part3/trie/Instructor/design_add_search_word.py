class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, root, word, level):
        if level == len(word):
            root.is_word = True
            root.word = word
            return

        if word[level] not in root.children:
            newNode = TrieNode()
            root.children[word[level]] = newNode
            self.insert(newNode, word, level+1)
        else:
            self.insert(root.children[word[level]], word, level+1)


    def search_(self, root, word, level):
        if level == len(word):
            return root.is_word

        character = word[level]
        if character == ".":
            for key in root.children:
                if self.search_(root.children[key], word, level+1):
                    return True

            return False
        else:
            if character in root.children:
                return self.search_(root.children[character], word, level+1)
            else:
                return False


    def addWord(self, word: str) -> None:
        self.insert(self.root, word,0)
        

    def search(self, word: str) -> bool:
        return self.search_(self.root, word,0)
