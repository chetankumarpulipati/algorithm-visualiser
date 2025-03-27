import tkinter as tk
from tkinter import messagebox, simpledialog

def linear_search(arr, target, canvas, rects):
    for i, value in enumerate(arr):
        canvas.itemconfig(rects[i], fill="yellow")
        canvas.update()
        if value == target:
            canvas.itemconfig(rects[i], fill="green")
            return i
        canvas.itemconfig(rects[i], fill="red")
    return -1

def binary_search(arr, target, canvas, rects):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        canvas.itemconfig(rects[mid], fill="yellow")
        canvas.update()
        if arr[mid] == target:
            canvas.itemconfig(rects[mid], fill="green")
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        canvas.itemconfig(rects[mid], fill="red")
    return -1

def visualize_search(algorithm, arr, target):
    root = tk.Tk()
    root.title("Search Visualization")
    canvas = tk.Canvas(root, width=600, height=400)
    canvas.pack()

    rects = []
    bar_width = 600 / len(arr)
    for i, value in enumerate(arr):
        rect = canvas.create_rectangle(i * bar_width, 400, (i + 1) * bar_width, 400 - value * 4, fill="blue")
        canvas.create_text(i * bar_width + bar_width / 2, 400 - value * 4 - 10, text=str(i), fill="black")
        rects.append(rect)

    result = algorithm(arr, target, canvas, rects)
    if result != -1:
        # messagebox.showinfo("Result", f"Element found at index {result}")
        print()
    else:
        messagebox.showinfo("Result", "Element not found")
    root.mainloop()

def searching_algorithm():
    algorithms = {
        "Linear Search": linear_search,
        "Binary Search": binary_search
    }

    root = tk.Tk()
    root.withdraw()  # Hide the root window

    choice = simpledialog.askstring("Input", "Choose algorithm (Linear Search/Binary Search):")
    if choice in algorithms:
        arr = [int(x) for x in simpledialog.askstring("Input", "Enter array elements separated by space:").split()]
        target = int(simpledialog.askstring("Input", "Enter the target element:"))
        visualize_search(algorithms[choice], arr, target)
    else:
        messagebox.showerror("Error", "Invalid algorithm choice")