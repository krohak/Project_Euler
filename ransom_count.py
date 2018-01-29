from collections import Counter


def ransom_note(magazine, ransom):

    mag_count = Counter(magazine.split())
    ran_count = Counter(ransom.split())

    for word in ran_count:
        if mag_count[word]<ran_count[word]:
            return False

    return True

m, n = map(int, input().strip().split(' '))
magazine = input()
ransom = input()
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")

'''
from collections import Counter


def ransom_note(magazine, ransom):

    a = Counter(str(magazine).split())
    b = Counter(str(ransom).split())

    #print(a,b)


    for word in set.intersection(set(b),set(a)):
        if a[word]<b[word]:
            return False

    return True

m, n = map(int, input().strip().split(' '))
magazine = input()
ransom = input()
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
'''
