#!/usr/bin/python
# -*- coding: utf-8 -*-



def make_link(G,edge1,edge2):

    if edge1 not in G:
        G[edge1]={}
    G[edge1][edge2]=1
    if edge2 not in G:
        G[edge2]={}
    G[edge2][edge1] =1


def Generate_graph(intput_data):

    lines = intput_data
    G=dict()
    for edges in lines:
        li1,li2 =edges.split(" ")
        make_link(G,int(li1), int(li2))
    return G





def coloring(G,v):
    queue=[]
    Colors=dict()
    Colors[v]=0
    queue=[v]
    visited=set([v])
    while queue:
        ans = queue.pop(0)

        for neighbor in G[ans]:
            if neighbor not in visited:
                ans2 =Colors.get(ans,0)

                i=0
                Colors[neighbor] = ans2+1
                queue.append(neighbor)
                visited.add(neighbor)



    return Colors




def solve_it(input_data):
    # Modify this code to run your optimization algorithm
    Colors =dict()
    # parse the input

    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    graph =Generate_graph(lines[1:-1])
    ans = coloring(graph,0)
    nos = len(set(ans.values()))
    ans2 =  "{} {} \n".format(nos,1)
    al2=[]
    for i in range(node_count):
        al2.append(str(ans[i]))
    ans2+=" ".join(al2)
    return ans2
    # build a trivial solution
    # every node has its own color



import sys

if __name__ == '__main__':

    filename =sys.argv[1].strip()
    input_data_file = open(filename, 'r')
    input_data = ''.join(input_data_file.readlines())
    input_data_file.close()
    print solve_it(input_data)
else:
    print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver2.py ./data/gc_4_1)'

