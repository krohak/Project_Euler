from collections import Counter

a = input().strip()
b = input().strip()

# set x,y
x = Counter(a)
y = Counter(b)


# set remainders
rem1 = (x-y)
rem2 = (y-x)


rem3 = rem1+rem2

sum1=sum(rem3.values())

print(sum1)

'''
from collections import defaultdict

def number_needed(a, b):
    l=defaultdict()
    r=defaultdict()

    for word in a:
        try:
            l[word]+=1
        except:
            l[word]=1

    for word in b:
        try:
            r[word]+=1
        except:
            r[word]=1

    #print(l,r)
    sect=set.intersection(set(l),set(r))
    #print(sect)

    res=0
    for el in sect:
        #print(el,r[el],l[el])
        res+=min(r[el],l[el])

    #print(len(a),len(b),res)
    return (len(a)+len(b)-2*res)

a = input().strip()
b = input().strip()

print(number_needed(a, b))


'''

'''

from collections import *
a = Counter(raw_input())
b = Counter(raw_input())
c = a - b
d = b - a
e = c + d
print len(list(e.elements()))

'''
