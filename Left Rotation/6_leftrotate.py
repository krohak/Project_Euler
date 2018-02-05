def array_left_rotation(a, n, k):
    for i in range(n):
        a.append(a[i])
    return a[k:k+n]

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')



'''
from copy import deepcopy

def array_left_rotation(a, n, k):
    a2=deepcopy(a)
    for i in range(n):
        a2[(i-k+n)%(n)]=a[i]
    return a2


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
'''
