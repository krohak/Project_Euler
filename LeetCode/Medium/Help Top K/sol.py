from collections import Counter
import heapq

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

removedSpam = set(map(lambda x: tuple(x.values()), help_love_messages))
emailCounts = Counter( map(lambda x: x[0], removedSpam) )
emailHeap = [ (c,email) for email,c in emailCounts.items() ]
heapq.heapify(emailHeap)
print(heapq.nlargest(3, emailHeap))