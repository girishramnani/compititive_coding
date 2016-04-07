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

    for i in graph.keys():
        if len(graph[i])%2!=0:
            return False,len(graph.keys())
    return True,len(graph.keys())


TEST3=[(0, 1), (1, 5), (1, 7), (4, 5),
(4, 8), (1, 6), (3, 7), (5, 9),
(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]

def dfs(graph,i,path,done,le):

    if (len(done)==len(graph)):
        return path,True
    if(len(path)==le):
        return -1,False
    for j in graph:
        if j[0] ==i:
            if j not in done:
                path.append(j[1])
                t= dfs(graph,j[1],path,done+[j],le)
                if t[1]==False:
                    continue
                elif t[1]==True:
                    return t
        elif j[1] ==i:
            if j not in done:
                path.append(j[0])
                t= dfs(graph,j[0],path,done+[j],le)
                if t[1]==False:
                    continue
                elif t[1]==True:
                    return t
    return path,False


def test(graph):
    ans = createGraph(graph)
    if ans[0]:
        print(dfs(graph,graph[0][0],[],[],ans[1])[0])
    else:
        return False


test2 =[(1,2),(2,3),(3,4),(4,1)]
test(TEST3)



