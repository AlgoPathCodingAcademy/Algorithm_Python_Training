class Solution:

    def getNeighbors(self, current_row, current_column, board):
        neighbors = []
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        for drow,dcolumn in directions:
            new_row = current_row + drow
            new_column = current_column + dcolumn
            if (new_row >= 0 and new_row < len(board)) and \
                (new_column >=0 and new_column < len(board[0])):
                neighbors.append((new_row,new_column))

        return neighbors

    def dfs(self, start_row, start_column, board, visited, letter, level):

        current = letter[level]
        if current != board[start_row][start_column]:
            return False

        if level == len(letter)-1:
            return True

        visited[(start_row,start_column)] = True

        neighbors = self.getNeighbors(start_row, start_column, board)

        for row,column in neighbors:
            if (row,column) not in visited:
                #print("row,column",row,column)
                if self.dfs(row,column,board,visited,letter,level+1):
                    return True

        del visited[(start_row,start_column)]

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        c_list = []
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == word[0]:
                    c_list.append((row,column))

        #print("c_list",c_list)
        has_matched = False
        for c_word in c_list:
            visited = {}
            row,column = c_word
            if self.dfs(row,column,board,visited,word,0):
                has_matched = True
                break

        return has_matched
