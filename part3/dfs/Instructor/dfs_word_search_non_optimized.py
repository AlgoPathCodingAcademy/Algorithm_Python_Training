def dfs_search(maze, path, visited, word):
    row,column = path[-1]
    
    directions = [(-1,0),(1,0),(0,1),(0,-1)]
    if len(word) == len(path):
        search_word = ""
        for point in path:
            point_row,point_column = point
            search_word = search_word + maze[point_row][point_column]

        if search_word == word:
            return True
        else:
            return False

    for drow,dcolumn in directions:
        new_row = row + drow
        new_column = column + dcolumn
        if (new_row >= 0 and new_row < len(maze)) and \
            (new_column >= 0 and new_column < len(maze[0])):
            if (new_row,new_column) not in visited:
                 visited[(new_row,new_column)] = True
                 isFound = dfs_search(maze,path+[(new_row,new_column)],visited, word)
                 del visited[(new_row,new_column)]
                 if isFound:
                     return True

    return False

def exist(board, word):
    # write your code here
    src_list = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                src_list.append((i,j))

    isFound = False
    for item in src_list:
        visited = {}
        start = item
        visited[start] = True
        path = [start]
        if dfs_search(board,path,visited,word):
            isFound = True
            break

    return isFound
    
print(exist(["ABCE","SFCS","ADEE"],"ABCCED")) # Should print true
print(exist(["z"],"z")) # Should print true
print(exist(["b","a","b","b","a"],"baa")) # Should print false
