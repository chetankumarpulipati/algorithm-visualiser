import tkinter as tk
from algorithms.searching_algorithms import searching_algorithm
from algorithms.sorting_algorithms import sorting_algorithm
from algorithms.pathfinding_algorithms import pathfinding_algorithm
from algorithms.graph_algorithms import graph_algorithms
def start():
    def show_menu(event):
        menu.post(event.x_root, event.y_root)

    root = tk.Tk()
    root.title("Algorithm Visualizer")
    root.geometry("400x400")
    root.resizable(False, False)

    menu = tk.Menu(root, tearoff=0)
    menu.add_command(label="Searching Algorithms", command=lambda: searching_algorithm())
    menu.add_command(label="Sorting Algorithms", command=lambda: sorting_algorithm())
    menu.add_command(label="Pathfinding Algorithms", command=lambda: pathfinding_algorithm())
    menu.add_command(label="Graph Algorithms", command=lambda: graph_algorithms())

    button = tk.Button(root, text="Choose Algorithm")
    button.pack(pady=20)
    button.bind("<Button-1>", show_menu)

    root.mainloop()

if __name__ == '__main__':
    start()