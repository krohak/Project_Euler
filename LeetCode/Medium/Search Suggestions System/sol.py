from collections import defaultdict

class Node():
    def __init__(self, val=None):
        self.val = val
        self.edges = defaultdict(Node)

    def addEdge(self, e):
        self.edges[e].val = e
    
    def __repr__(self):
        return '{} - {}'.format(self.val, list(self.edges.values()))


class Solution(object):
    def suggestedProducts(self, products, searchWord):
        suggested = []
        trie = self.makeTrie(products)
        pointer = trie
        for i, c in enumerate(searchWord):
            if c not in pointer.edges:
                suggested.extend([ [] for _ in range(i, len(searchWord)) ])
                return suggested
            pointer = pointer.edges[c]
            self.subtreeSuggestions = []
            self.getSuggestedInSubtree(pointer, '')
            suggested.append([ '{}{}'.format(searchWord[:i+1], suffix) for suffix in self.subtreeSuggestions ])
        return suggested

    def getSuggestedInSubtree(self, pointer, prefix):
        if -1 in pointer.edges: 
            self.subtreeSuggestions.append(prefix)
            if len(self.subtreeSuggestions)>2: return
        for o in range(ord('a'), ord('z')):
            if chr(o) in pointer.edges:
                self.getSuggestedInSubtree(pointer.edges[chr(o)], '{}{}'.format(prefix, chr(o)))
                if len(self.subtreeSuggestions)>2: return

    def makeTrie(self, products):
        trie = Node()
        for product in products:
            pointer = trie
            for c in product:
                if not c in pointer.edges:
                    pointer.addEdge(c)
                pointer = pointer.edges[c]
            pointer.addEdge(-1)
        return trie

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
# products = ["havana"] 
# searchWord = "havana"
print(Solution().suggestedProducts(products, searchWord))