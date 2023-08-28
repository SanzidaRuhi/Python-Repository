#implementation of bfs
tree={
    'A':['B','C'],
    'B':['D','E'],
    'C':['G','H'],
    'D':['F'],
    'E':[],
    'F':[],
    'G':[],
    'H':['I'],
    'I':[]
}
visited_list=[]#empty list for visited nodes
queue_list=[]#empty list for queue
def bfs(visited_list, tree, node):#function for bfs
    visited_list.append(node)
    queue_list.append(node)
    while queue_list:#creating loop to visit each node
        m=queue_list.pop(0)
        print(m)
        #print(m,end='\n')
        for adjacent in tree[m]:
            if adjacent not in visited_list:
                visited_list.append(adjacent)
                queue_list.append(adjacent)
print("following is the breadth first search")
bfs(visited_list, tree, 'A')#function calling


#implementation of dfs
tree={
    'A':['B','C'],
    'B':['D','E'],
    'C':['G','H'],
    'D':['F'],
    'E':[],
    'F':[],
    'G':[],
    'H':['I'],
    'I':[]
}
visited_list=[]#empty list for visited nodes
queue_list=[]#empty list for queue
def dfs(visited_list, tree, node):#function for dfs
    visited_list.append(node)
    queue_list.append(node)
    while queue_list:#creating loop to visit each node
        m=queue_list.pop(0)
        print(m)
        for adjacent in tree[node]:
            if adjacent not in visited_list:
                dfs(visited_list, tree, adjacent)
print("following is the depth first search")
dfs(visited_list, tree, 'A')#function calling
'''if node not in visited_list:
        print(node)
        visited_list.append(node)
        for adjacent in tree[node]:
            if adjacent not in visited_list:
                dfs(visited_list, tree, adjacent)'''