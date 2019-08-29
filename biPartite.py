#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:04:12 2019

@author: acer
"""
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def draw_graph(graph, e_color):
    plt.figure(figsize=(4, 4))
    plt.axis('off')

    nx.draw_networkx_nodes(graph, layout, node_color='steelblue', node_size=700)
    nx.draw_networkx_edges(graph, layout, edge_color=e_color, width = 3)
    nx.draw_networkx_labels(graph, layout, font_color='white')
    
    plt.tight_layout()
    plt.show()
    
def create_graph():
    B = nx.Graph()
    B.add_nodes_from(m, bipartite=0)
    B.add_nodes_from(n, bipartite=1)
    return B
    
G = np.array([[1,1,0,0],
              [1,0,0,0],
              [0,1,0,1],
              [0,1,0,0],
              [0,0,1,1]])
    
m = [1, 2, 3, 4, 5]
n = ['a', 'b', 'c', 'd']
layout = {1: [0, 8], 2: [0, 6], 3: [0, 4], 4: [0, 2], 5:[0, 0],
         'a': [1, 7], 'b': [1, 5], 'c': [1, 3], 'd':[1, 1],}

B = create_graph()

# Add edges only between nodes of opposite node sets
for i,row in enumerate(G):
    for j,edge in enumerate(row):
        if(G[i,j] == 1):
            B.add_edge(m[i], n[j])
    
draw_graph(B, 'grey')

#Initialize
M = create_graph()
allocated = []
for i,row in enumerate(G):
    for j,edge in enumerate(row):
        if(G[i,j] == 1 and n[j] not in allocated):
            M.add_edge(m[i], n[j])
            allocated.append(m[i])
            allocated.append(n[j])
            break

print('Initial Matching...')
draw_graph(M, 'blue')

#Detrmine Alternate Path
def alt_path(start_node):
    print('start node:', start_node)
    try:
        node_index = m.index(start_node)
        for j,edge in enumerate(G[node_index]):
            if(edge == 1 and (start_node, n[j]) not in M1.edges()):
                M1.add_edge(start_node, n[j])
                #print('Choosen edge:', start_node, n[j])
                start_node = n[j]
                alt_path(start_node)
                return None
    except:
        node_index = n.index(start_node)
        for j,edge in enumerate(G.T[node_index]):
            if(edge == 1 and (m[j], start_node) not in M1.edges()):
                M1.add_edge(m[j],start_node)
                #print('Choosen edge:', m[j] ,start_node)
                start_node = m[j]
                alt_path(start_node)
                return None

M1 = create_graph()
free_node = list(set(n)-set(allocated))
bol = alt_path(free_node[0])
print('Alternate Path...')
draw_graph(M1, 'red')

# Redraw Matching Graph
edges = (set(M.edges()).union(M1.edges()) - 
        set(M.edges()).intersection(M1.edges()))

M2 = create_graph()

# Add edges only between nodes of opposite node sets
for edge in list(edges):
    M2.add_edge(edge[0],edge[1])

print('FInal MAximal MAtching')    
draw_graph(M2, 'green')