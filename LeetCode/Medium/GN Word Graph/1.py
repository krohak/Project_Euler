from collections import defaultdict
from random import choice, randint

inputStrings = [
"apple",
"banana",
"cabbage",
]

begins = ["a","b","c"]
ends = ["a","e"]

# "a-z"
# "A-Z"
# graph = {
#     'a': set(['n'])
# }

def makeWord():
    graph = defaultdict(set)
    for string in inputStrings:
        for i in range(1,len(string)):
            graph[string[i-1]].add(string[i])
    
    start = choice(begins)
    end = choice(ends)

    vertex = start
    output = start
    # for cycle detecting, use a set
    while not vertex==end:
        vertex = choice(list(graph[vertex]))
        output+=vertex
    return output

print(makeWord())

def makeWordArray(constraint):

    graph = defaultdict(set)
    for string in inputStrings:
        for i in range(1,len(string)):
            graph[string[i-1]].add(string[i])
    
    start = choice(begins) #'a'
    end = choice(ends) #'a'
    vertex = start 
    output = start
    # iterations = 0
    visited = defaultdict(int)

    while visited[vertex]<constraint and vertex!=end:
        select = choice([ chr(i) for i in range (ord('a'), ord('z')+1) ])
        while select not in graph[vertex]:
            select = choice([ chr(i) for i in range (ord('a'), ord('z')+1) ])
        output+=select
        vertex=select
        visited[vertex]+=1
    return output


def makeWordBFSWrong():
    graph = defaultdict(set)
    for string in inputStrings:
        for i in range(1,len(string)):
            graph[string[i-1]].add(string[i])
    
    start = choice(begins)
    end = choice(ends)

    vertex =  None
    output = ""
    frontier, visited = [start], set()
    while frontier and not vertex == end:
        vertex = frontier.pop(0)
        visited.add(vertex)
        output+=vertex
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                frontier.append(neighbour)
                break

    return output


# string
# begins: a,b,c
# ends: a,e


# a->p,n,b,g
# abage
# bage
# capple
# a