help_love_messages = [
    {"receiver": "cmen@help.com", "msg": "Anch", "sender": "sanie@help.com"},
    {"receiver": "brad@help.com", "msg": "Intrk", "sender": "wing@help.com"},
    {"receiver": "dwin@help.com", "msg": "Gtion today", "sender": "jemy@help.com"},
    {"receiver": "cmen@help.com", "msg": "Yoof", "sender": "hmy@help.com"},
    {"receiver": "hmy@help.com", "msg": "thoepol", "sender": "dwin@help.com"},
    {"receiver": "hmy@help.com", "msg": "foomb, nbd", "sender": "jemy@help.com"},
    {"receiver": "qui@help.com", "msg": "Yot!", "sender": "hmy@help.com"},
    {"receiver": "hmy@help.com", "msg": "thol", "sender": "cmen@help.com"},
    {"receiver": "cmpy@help.com", "msg": "I love spam!", "sender": "patchy@help.com"},
    {"receiver": "cmpy@help.com", "msg": "I love spam!", "sender": "patchy@help.com"},
    {"receiver": "cmpy@help.com", "msg": "I love spam!", "sender": "patchy@help.com"},
    {"receiver": "cmpy@help.com", "msg": "I love spam!", "sender": "patchy@help.com"},
    {"receiver": "cmpy@help.com", "msg": "I love spam!", "sender": "patchy@help.com"},
    {"receiver": "cmpy@help.com", "msg": "I love spam!", "sender": "patchy@help.com"},
]

# print(help_love_messages, end="\n\n")

from collections import defaultdict
import heapq

receiverDict = defaultdict(int)
messageSet = set()

for message in help_love_messages:
    if frozenset(message.values()) not in messageSet:
        receiverDict[message['receiver']]+=1
        messageSet.add(frozenset(message.values()))

receiverHeap = [(-freq,receiver) for receiver, freq in receiverDict.items()]
heapq.heapify(receiverHeap)

k = 10

# answer = [ heapq.heappop(receiverHeap) if receiverHeap else None for _ in range(k) ]
# print(answer)

class LeaderBoard():
    
    def __init__(self, help_love_messages, emailType):
        self.help_love_messages = help_love_messages
        self.emailType = emailType
    
    def getTopK(self, k):
        emailDict = defaultdict(int)
        messageSet = set()

        for message in help_love_messages:
            if frozenset(message.values()) not in messageSet:
                emailDict[message[self.emailType]]+=1
                messageSet.add(frozenset(message.values()))
        
        # transforming the dictionary to a max heap (negative values)
        emailHeap = [(freq,receiver) for receiver, freq in emailDict.items()]
        heapq.heapify(emailHeap)

        return heapq.nlargest(k, emailHeap) #[ heapq.heappop(emailHeap) if emailHeap else None for _ in range(k) ]

# import TestClass from pytest
       
# class LenderBoardTest(TestClass):
#     def 

ldrboard = LeaderBoard(help_love_messages, 'receiver')
print(ldrboard.getTopK(10))

ldrboard = LeaderBoard(help_love_messages, 'sender')
print(ldrboard.getTopK(10))

# heapq.nlargest(n, iterable, key=None)
# Return a list with the n largest elements from the dataset defined by iterable. key, if provided, specifies a function of one argument that is used to extract a comparison key from each element in iterable (for example, key=str.lower). Equivalent to: sorted(iterable, key=key, reverse=True)[:n].
# print(heapq.heappop([]))