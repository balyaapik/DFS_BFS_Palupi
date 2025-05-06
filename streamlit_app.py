import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import time

# Define the adjacency list
graph = {
    0: {3, 1},
    1: {0, 2, 4, 6, 7},
    2: {1, 3, 8, 9},
    3: {0, 2},
    4: {1, 5, 6, 9},
    5: {4},
    6: {1, 4, 7},
    7: {1, 4, 6},
    8: {2},
    9: {2}
}

# Visualization function
def draw_graph(visited_nodes, current_structure, traversal_type):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G, seed=42)
    node_colors = ['lightgreen' if node in visited_nodes else 'lightgray' for node in G.nodes()]

    fig, ax = plt.subplots(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=800, ax=ax)
    ax.set_title(f"{traversal_type} Traversal - Visited Nodes: {visited_nodes}")
    st.pyplot(fig)

    st.write(f"Current {'Queue' if traversal_type == 'BFS' else 'Stack'}: {list(current_structure)}")

# BFS implementation
def bfs(start_node):
    visited = set()
    queue = deque([start_node])
    visited_order = []

    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.add(current)
            visited_order.append(current)
            draw_graph(visited_order, queue, "BFS")
            time.sleep(1)
            queue.extend(sorted(graph[current] - visited))

# DFS implementation
def dfs(start_node):
    visited = set()
    stack = [start_node]
    visited_order = []

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            visited_order.append(current)
            draw_graph(visited_order, stack, "DFS")
            time.sleep(1)
            stack.extend(sorted(graph[current] - visited, reverse=True))

# Streamlit app interface
st.title("BFS and DFS Visualization")

traversal = st.radio("Choose Traversal Method", ["BFS", "DFS"])
start_node = st.selectbox("Select Starting Node", sorted(graph.keys()))

if st.button("Run Traversal"):
    if traversal == "BFS":
        bfs(start_node)
    else:
        dfs(start_node)
