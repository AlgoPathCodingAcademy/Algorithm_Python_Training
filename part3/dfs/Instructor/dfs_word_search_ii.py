class Solution:
    def getNeighbors(self, current, visited):
        neighbors = []
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        row, column = current
        for drow, dcolumn in directions:
            current_row = row + drow
            current_column = column + dcolumn
            if current_row >=0 and current_row < len(self.board) and \
                current_column >=0 and current_column < len(self.board[0]):
                if (current_row,current_column) not in visited:
                    neighbors.append((current_row,current_column))

        return neighbors

    def dfs(self, path, level, visited, word):
        start = path[-1]
        row,column = path[-1]
        if word[level] != self.board[row][column]:
            return False

        if level == len(word) - 1:
            return True

        neighbors = self.getNeighbors(start,visited)
        isFound = False
        for neighbor_row, neighbor_column in neighbors:
            visited[(neighbor_row,neighbor_column)] = True
            isFound = self.dfs(path + [(neighbor_row,neighbor_column)],level + 1, visited, word)
            del visited[(neighbor_row,neighbor_column)]
            if isFound:
                return True

        return False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        result = []

        for word in words:
            for row in range(len(board)):
                for column in range(len(board[0])):
                    if board[row][column] == word[0]:
                        path = [(row,column)]
                        visited = {}
                        visited[(row,column)] = True
                        if self.dfs(path,0,visited,word):
                            result.append(word)

        final_result = set(result)
        return list(final_result)
