'''students name: Dekavallas Dimitrios
   I.D. number: 8130034
   submission date: 05/10/2015
   department: DMST'''

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-c","--c",action="store_true", help="activate the 'numbers of nodes' function")
parser.add_argument("-r","--radious", type=int, help="Radious value")
parser.add_argument("num_nodes", type=int, help="numbers of nodes to be extracted")
parser.add_argument("input_file", help="file path that contain the graph")
args = parser.parse_args()

'''read file and graph implementation by adjacency list '''
grahpFile = open(args.input_file)
poplist = []
s = 0
for line in grahpFile.readlines():
        numbers_str = line.split()#removing the space between the number of nodes in the file
        x,y = numbers_str
        x = int(x)
        y = int(y)             
        poplist.append(x)
        poplist.append(y)
grahpFile.close()
poplist.reverse()
AdjacencyList= {}
for i in poplist:
    AdjacencyList[i]=-1
while poplist:
    x = poplist.pop()
    y = poplist.pop()
        
    if AdjacencyList[x]!= -1:         
            AdjacencyList[x].extend([y])           
    else:
            tem = []
            tem.append(y)
            AdjacencyList[x]=tem
            
    if AdjacencyList[y]!=-1:
            AdjacencyList[y].extend([x])        
    else:
            tem1 = []
            tem1.append(x)
            AdjacencyList[y]=tem1

def breadth_first_search (AL,start):
        '''breadth-first search '''
        visited = []
        for i in range (0, len(AL)+1):
                if i==0:
                        visited.append (-1)
                else:
                        visited.append (0)
        visited [start] = 1
        from collections import deque
        que = deque()#use of deque in order to use .popleft() function 
        que.append(start)
        to=[]
        while que:
            c = que.popleft()
            to.clear()
            to.extend(AL[c])
            while to:
                v=to.pop()
                if visited [v] == 0:
                    visited [v] = 1
                    que.append(v)
        
        return visited
   
def find_max_node (AdjacencyList):
        '''search for the node with the biggest no. of neighbours'''
        maxim = -1
        pos = -1
        for i in AdjacencyList:
                if len(AdjacencyList[i])>maxim:
                        maxim = len(AdjacencyList[i])
                        pos = i
        s = 'Removing node: ' + repr(pos) + ' with metric: ' + repr(len(AdjacencyList[pos])) + ''
        if len(s)>80:
                print(s[:s.rfind(' ',0,80)])
                se=s[s.rfind(' ',0,80):len(s)]
                print('  ',se)
        else:
                print(s)
        return pos

def list_combination (listA,listB):
        '''an alternation of XOR,
           in order to keep a record of what -connected- parts of the graph we have visited.'''
        list3=[]
        for i in range(0,len(listB)):
             
             if i!=0:   
                 if listA[i]==1 or listB[i]==1:
                         list3.insert(i, 1)
                 else:
                        list3.insert(i, 0)
             else:
                        list3.insert(i, -1)
        return list3

def print_subgraph(list_visited):
        '''print modification'''
        pr=[]
        for i in range(0,len(list_visited)):
                if list_visited[i]==1:
                        pr.append(i)
        s = 'Size: ' + repr(len(pr)) + ' members: ' + repr(pr) + ''
        if len(s)>80:
                print(s[:s.rfind(' ',0,80)])
                se=s[s.rfind(' ',0,80):len(s)]
                #print(se)
                print('  ',se)
        else:
                print(s)
                
def C_I(AdjacencyList,r):
        CI={}
        for i in range(1,len(AdjacencyList)):
                #find shortest path for each node to the others
                s=i
                pred=[]
                dist=[]
                pq = {}
                
                for v in range(0,len(AdjacencyList)+1):
                        pred.insert(v, None)
                        if v!=s:
                                dist.insert(v, 1000)
                        else:
                                dist.insert(v, 0)        
                pq[s] = dist[s]
                al_u=[]
                while pq:
                        #find min
                        min_u=1002
                        for i in pq.keys():
                                if min_u > pq[i]:
                                                u = i
                                                min_u=pq[i] 
                        #remove the item with the smallest value
                        del pq[u]
                        al_u.clear()
                        al_u.extend(AdjacencyList[u])
                        while al_u:
                                v=al_u.pop()
                                if dist[v] > dist[u] + 1:
                                        dist[v] =  dist[u] + 1
                                        pred[v] =  u
                                        if v in pq:
                                                pq[v]=dist[v]
                                        else:
                                                pq[v]= dist[v]
                #finding the node with the biggest influence for the given -r
                sum_BALL=0
                if not r:
                        r=2
                for i in range(0,len(dist)):
                        if dist[i]==r:
                               sum_BALL = sum_BALL+ (len(AdjacencyList[i])-1)                                        
                CI[s]=(len(AdjacencyList[s])-1)*sum_BALL
        #find node with biggest influence
        for i in range(1,len(AdjacencyList)):
                if i==1:
                        max_CI=CI[i]
                        pos_max_CI=i
                elif max_CI < CI[i]:
                        max_CI=CI[i]
                        pos_max_CI=i
        s = 'Removing node: ' + repr(pos_max_CI) + ' with metric: ' + repr(max_CI) + ''
        if len(s)>80:
                print(s[:s.rfind(' ',0,80)])
                se=s[s.rfind(' ',0,80):len(s)]
                print('  ',se)
        else:
                print(s)
        return pos_max_CI

def No_of_nodes (AdjacencyList,c,r,num_nodes):
        '''implement chosen method of finding the node to be extracted.
           Extract this node and explores the execution of the program'''
        k=[]
        k.extend(list(AdjacencyList.keys()))
        s = 'Size: ' + str(len(AdjacencyList)) + ' members: ' + repr(k) + ''
        if len(s)>80:
                print(s[:s.rfind(' ',0,80)])
                se=s[s.rfind(' ',0,80):len(s)]
                print('  ',se)
        else:
                print(s)
        for i in range (0,num_nodes):
                if c:
                        max_no= find_max_node(AdjacencyList)
                else:
                        max_no= C_I(AdjacencyList,r)
                while AdjacencyList[max_no]:
                                        neib=AdjacencyList[max_no].pop()
                                        AdjacencyList[neib].remove(max_no)
                te1=[]
                te1.extend(breadth_first_search (AdjacencyList,1))
                print_subgraph(te1)
                tempo=[]
                te2=[]
                while te1.count(0)!=0:
                        te2.clear()
                        te2.extend(breadth_first_search (AdjacencyList,te1.index(0)))
                        print_subgraph(te2)
                        tempo.extend(list_combination (te1,te2))
                        te1.clear()
                        te1.extend(tempo)
                        tempo.clear()

No_of_nodes (AdjacencyList,args.c,args.radious,args.num_nodes)

