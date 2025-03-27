import tkinter as tk
from tkinter import messagebox, simpledialog
from collections import deque
import heapq

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            queue.extend(graph[vertex] - visited)
    return order

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    order = [start]
    for next in graph[start] - visited:
        order.extend(dfs(graph, next, visited))
    return order

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(graph, start, goal):
    queue = []
    heapq.heappush(queue, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while queue:
        current = heapq.heappop(queue)[1]

        if current == goal:
            break

        for next in graph[current]:
            new_cost = cost_so_far[current] + graph[current][next]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                heapq.heappush(queue, (priority, next))
                came_from[next] = current

    return came_from, cost_so_far

def draw_graph(canvas, graph, positions):
    for node, edges in graph.items():
        x, y = positions[node]
        canvas.create_oval(x-10, y-10, x+10, y+10, fill="white")
        canvas.create_text(x, y, text=node)
        for edge in edges:
            ex, ey = positions[edge]
            canvas.create_line(x, y, ex, ey)

def draw_path(canvas, path, positions):
    for i in range(len(path) - 1):
        x1, y1 = positions[path[i]]
        x2, y2 = positions[path[i+1]]
        canvas.create_line(x1, y1, x2, y2, fill="red", width=2)

def visualize_algorithm(algorithm, graph, start, goal=None):
    root = tk.Tk()
    root.title("Graph Algorithm Visualization")
    canvas = tk.Canvas(root, width=600, height=400)
    canvas.pack()

    positions = {node: (i*100 + 50, 200) for i, node in enumerate(graph)}

    draw_graph(canvas, graph, positions)

    if algorithm == bfs:
        result = algorithm(graph, start)
        messagebox.showinfo("Result", f"BFS Order: {result}")
    elif algorithm == dfs:
        result = algorithm(graph, start)
        messagebox.showinfo("Result", f"DFS Order: {result}")
    elif algorithm == a_star:
        if goal is None:
            messagebox.showerror("Error", "Goal node is required for A* Algorithm")
            return
        came_from, cost_so_far = algorithm(graph, start, goal)
        path = []
        current = goal
        while current:
            path.append(current)
            current = came_from[current]
        path.reverse()
        draw_path(canvas, path, positions)
        messagebox.showinfo("Result", f"A* Path: {path}")

    root.mainloop()

def pathfinding_algorithm():
    algorithms = {
        "BFS": bfs,
        "DFS": dfs,
        "A* Algorithm": a_star
    }

    root = tk.Tk()
    root.withdraw()  # Hide the root window

    choice = simpledialog.askstring("Input", "Choose algorithm (BFS/DFS/A* Algorithm):")
    if choice in algorithms:
        start = simpledialog.askstring("Input", "Enter start node:")
        if choice == "A* Algorithm":
            goal = simpledialog.askstring("Input", "Enter goal node:")
        else:
            goal = None
        graph_input = simpledialog.askstring("Input", "Enter graph as adjacency list (e.g., {'A': {'B', 'C'}, 'B': {'A', 'D'}, ...}):")
        graph = eval(graph_input)
        visualize_algorithm(algorithms[choice], graph, start, goal)
    else:
        messagebox.showerror("Error", "Invalid algorithm choice")