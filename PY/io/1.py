import sys

sys.stdin = open('task12.txt', 'r')
sys.stdout = open('output1.txt', 'w')
t=int(input())

for i in range(t):
    n,m=input().split()
    n,m=int(n),int(m)