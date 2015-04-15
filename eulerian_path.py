__author__ = 'Girish'


def createGraph(li):
    graph = dict()
    for i,j in li:
        if i not in graph.keys():
            graph[i]=[]
        if j not in graph.keys():
            graph[j]=[]
        graph[i].append(j)
        graph[j].append(i)

    return graph


def bfs(graph,start,path,endlen,nodes):
    if(len(graph.keys())==len(path) and len(nodes)==0 ):
        return path,True
    elif(len(graph.keys())==len(path)):
        return -1,False
    for i in graph[start]:
        if i not in path:
            templi = list(nodes)
            try:
                templi.remove((start,i))
            except:
                templi.remove((i,start))
            ans,bol=  bfs(graph,i,path+[i],endlen,templi)
            if bol ==True:
                return ans

    return -1,False



def work(li,length,nodes,done=set()):

    for i in li.keys():
        if len(li[i])%2!=0:
            x,bol =bfs(li,i,[i],length,nodes)
            if bol :
                print(x)
                break







TEST  = [(1,2),(2,3),(3,4),(4,5),(5,6),(2,5),(6,1)]


print(work(*createGraph(TEST)))