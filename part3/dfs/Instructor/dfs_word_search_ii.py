def convertToPoint(word,maze):
    points = []
    for row in range(len(maze)):
        for column in range(len(maze[0])):
            if maze[row][column] == word:
                points.append((row,column))

    return points

def dfs_search(path,maze,visited,level,word):
    current_row,current_column = path[-1]
    directions = [(-1,0),(1,0),(0,1),(0,-1)]
    if word[level] == maze[current_row][current_column]:
        if len(word)-1 == level:
            return True

        for drow,dcolumn in directions:
            new_row = current_row + drow
            new_column = current_column + dcolumn
            if (new_row >=0 and new_row < len(maze)) and \
                (new_column >=0 and new_column < len(maze[0])):
                if (new_row,new_column) not in visited:
                    visited[(new_row,new_column)] = True
                    result = dfs_search(path + [(new_row,new_column)],maze,visited,level+1,word)
                    del visited[(new_row,new_column)]
                    if result:
                        return result
    else:
        return False
    


def word_search_i_i(board, words):
    # write your code here
    output = []
    for word in words:
        start_point = convertToPoint(word[0],board)
        for point in start_point:
            visited = {}
            visited[point] = True
            if dfs_search([point],board,visited,0,word):
                output.append(word)
                break

    return output

board = ["doaf","agai","dcan"]
words = ["dog","dad","dgdg","can","again"]
print(word_search_i_i(board,words))
board = ["a"]
words = ["b"]
print(word_search_i_i(board,words))
