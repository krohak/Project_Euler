class Node(object):
    def __init__(self):
        self.marks=0
        self.nodes={}

    def add(self,contact,i):
        if(i==len(contact)):
            return 
        self.nodes[contact[i]]=Node()
        self.nodes[contact[i]].marks+=1
        i+=1
        self.nodes[contact[i-1]].add(contact,i)
            

node=Node()
n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if (op=="add"):
        node.add(contact,0)
    elif (op == "find"):
        node1=node
        no=1
        for i in range(len(contact)):
            if(not node1.nodes.get(contact[i])):
                print(0)
                no=1
                break
               
            node1=node1.nodes[contact[i]]
        if(no):
            continue
            
        print(node1.marks)
