from collections import deque

def isNeighbour(first, second):

    count = 0
    for i in range(len(first)):

        if first[i]!=second[i]:
            count+=1
    
    return (True if count == 1 else False)


def BFS(beginWord, endWord, wordList):

    frontier = deque()
    explored = set()

    frontier.append((beginWord,0))

    while frontier:
        node = frontier.popleft()
        
        if node[0] not in explored:
            explored.add(node[0])
            if node[0] == endWord:
                return node[1]+1

            for neighbour in wordList:
                if isNeighbour(node[0], neighbour) and neighbour not in explored:
                    frontier.append((neighbour, node[1]+1))

    return 0



class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        return BFS(beginWord, endWord, wordList)
        


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]


sol = BFS(beginWord, endWord, wordList)
print(sol)