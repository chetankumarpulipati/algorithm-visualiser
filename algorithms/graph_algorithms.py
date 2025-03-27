import tkinter as tk
import sys
from tkinter import messagebox, simpledialog

def topological_sort_util(v, visited, stack, graph):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            topological_sort_util(i, visited, stack, graph)
    stack.insert(0, v)

def topological_sort(graph):
    visited = [False] * len(graph)
    stack = []
    for i in range(len(graph)):
        if not visited[i]:
            topological_sort_util(i, visited, stack, graph)
    return stack

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        return result

def min_key(key, mst_set, V):
    min_val = sys.maxsize
    min_index = -1
    for v in range(V):
        if key[v] < min_val and not mst_set[v]:
            min_val = key[v]
            min_index = v
    return min_index

def prim(graph, V):
    key = [sys.maxsize] * V
    parent = [None] * V
    key[0] = 0
    mst_set = [False] * V
    parent[0] = -1
    for _ in range(V):
        u = min_key(key, mst_set, V)
        mst_set[u] = True
        for v in range(V):
            if graph[u][v] and not mst_set[v] and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u
    return parent

def visualize_graph_algorithm(algorithm, graph, vertices):
    root = tk.Tk()
    root.title("Graph Algorithm Visualization")
    canvas = tk.Canvas(root, width=600, height=400)
    canvas.pack()

    if algorithm == topological_sort:
        result = algorithm(graph)
        messagebox.showinfo("Result", f"Topological Sort: {result}")
    elif algorithm == Graph.kruskal:
        g = Graph(vertices)
        for edge in graph:
            g.add_edge(*edge)
        result = g.kruskal()
        messagebox.showinfo("Result", f"Kruskal's MST: {result}")
    elif algorithm == prim:
        result = algorithm(graph, vertices)
        messagebox.showinfo("Result", f"Prim's MST: {result}")

    root.mainloop()

def graph_algorithms():
    algorithms = {
        "Topological Sort": topological_sort,
        "Kruskal's Algorithm": Graph.kruskal,
        "Prim's Algorithm": prim
    }

    root = tk.Tk()
    root.withdraw()  # Hide the root window

    choice = simpledialog.askstring("Input", "Choose algorithm (Topological Sort/Kruskal's Algorithm/Prim's Algorithm):")
    if choice in algorithms:
        vertices = int(simpledialog.askstring("Input", "Enter number of vertices:"))
        edges = simpledialog.askstring("Input", "Enter edges (u v w) separated by commas:").split(',')
        graph = [tuple(map(int, edge.split())) for edge in edges]
        visualize_graph_algorithm(algorithms[choice], graph, vertices)
    else:
        messagebox.showerror("Error", "Invalid algorithm choice")