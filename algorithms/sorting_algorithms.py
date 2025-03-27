import tkinter as tk
from tkinter import messagebox, simpledialog

def bubble_sort(arr, canvas, rects):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            canvas.itemconfig(rects[j], fill="yellow")
            canvas.itemconfig(rects[j+1], fill="yellow")
            canvas.update()
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                canvas.coords(rects[j], j * 20, 400, (j + 1) * 20, 400 - arr[j] * 4)
                canvas.coords(rects[j+1], (j + 1) * 20, 400, (j + 2) * 20, 400 - arr[j+1] * 4)
            canvas.itemconfig(rects[j], fill="blue")
            canvas.itemconfig(rects[j+1], fill="blue")
    return arr

def quick_sort(arr, low, high, canvas, rects):
    if low < high:
        pi = partition(arr, low, high, canvas, rects)
        quick_sort(arr, low, pi-1, canvas, rects)
        quick_sort(arr, pi+1, high, canvas, rects)

def partition(arr, low, high, canvas, rects):
    i = low - 1
    pivot = arr[high]
    canvas.itemconfig(rects[high], fill="yellow")
    for j in range(low, high):
        canvas.itemconfig(rects[j], fill="yellow")
        canvas.update()
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            canvas.coords(rects[i], i * 20, 400, (i + 1) * 20, 400 - arr[i] * 4)
            canvas.coords(rects[j], j * 20, 400, (j + 1) * 20, 400 - arr[j] * 4)
        canvas.itemconfig(rects[j], fill="blue")
    arr[i+1], arr[high] = arr[high], arr[i+1]
    canvas.coords(rects[i+1], (i + 1) * 20, 400, (i + 2) * 20, 400 - arr[i+1] * 4)
    canvas.coords(rects[high], high * 20, 400, (high + 1) * 20, 400 - arr[high] * 4)
    canvas.itemconfig(rects[high], fill="blue")
    return i + 1

def selection_sort(arr, canvas, rects):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            canvas.itemconfig(rects[j], fill="yellow")
            canvas.update()
            if arr[j] < arr[min_idx]:
                min_idx = j
            canvas.itemconfig(rects[j], fill="blue")
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        canvas.coords(rects[i], i * 20, 400, (i + 1) * 20, 400 - arr[i] * 4)
        canvas.coords(rects[min_idx], min_idx * 20, 400, (min_idx + 1) * 20, 400 - arr[min_idx] * 4)
    return arr

def insertion_sort(arr, canvas, rects):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            canvas.itemconfig(rects[j], fill="yellow")
            canvas.update()
            arr[j + 1] = arr[j]
            canvas.coords(rects[j + 1], (j + 1) * 20, 400, (j + 2) * 20, 400 - arr[j + 1] * 4)
            canvas.itemconfig(rects[j], fill="blue")
            j -= 1
        arr[j + 1] = key
        canvas.coords(rects[j + 1], (j + 1) * 20, 400, (j + 2) * 20, 400 - arr[j + 1] * 4)
    return arr

def merge_sort(arr, l, r, canvas, rects):
    if l < r:
        m = (l + r) // 2
        merge_sort(arr, l, m, canvas, rects)
        merge_sort(arr, m + 1, r, canvas, rects)
        merge(arr, l, m, r, canvas, rects)

def merge(arr, l, m, r, canvas, rects):
    n1 = m - l + 1
    n2 = r - m
    L = arr[l:l + n1]
    R = arr[m + 1:m + 1 + n2]
    i = j = 0
    k = l
    while i < n1 and j < n2:
        canvas.itemconfig(rects[k], fill="yellow")
        canvas.update()
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        canvas.coords(rects[k], k * 20, 400, (k + 1) * 20, 400 - arr[k] * 4)
        canvas.itemconfig(rects[k], fill="blue")
        k += 1
    while i < n1:
        arr[k] = L[i]
        canvas.coords(rects[k], k * 20, 400, (k + 1) * 20, 400 - arr[k] * 4)
        canvas.itemconfig(rects[k], fill="blue")
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        canvas.coords(rects[k], k * 20, 400, (k + 1) * 20, 400 - arr[k] * 4)
        canvas.itemconfig(rects[k], fill="blue")
        j += 1
        k += 1

def heap_sort(arr, canvas, rects):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, canvas, rects)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        canvas.coords(rects[i], i * 20, 400, (i + 1) * 20, 400 - arr[i] * 4)
        canvas.coords(rects[0], 0 * 20, 400, 1 * 20, 400 - arr[0] * 4)
        heapify(arr, i, 0, canvas, rects)

def heapify(arr, n, i, canvas, rects):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        canvas.coords(rects[i], i * 20, 400, (i + 1) * 20, 400 - arr[i] * 4)
        canvas.coords(rects[largest], largest * 20, 400, (largest + 1) * 20, 400 - arr[largest] * 4)
        heapify(arr, n, largest, canvas, rects)

def visualize_sort(algorithm, arr):
    root = tk.Tk()
    root.title("Sort Visualization")
    canvas = tk.Canvas(root, width=600, height=400)
    canvas.pack()

    rects = []
    bar_width = 600 / len(arr)
    for i, value in enumerate(arr):
        rect = canvas.create_rectangle(i * bar_width, 400, (i + 1) * bar_width, 400 - value * 4, fill="blue")
        canvas.create_text(i * bar_width + bar_width / 2, 400 - value * 4 - 10, text=str(value), fill="black")
        rects.append(rect)

    if algorithm in [quick_sort, merge_sort]:
        algorithm(arr, 0, len(arr) - 1, canvas, rects)
    else:
        algorithm(arr, canvas, rects)
    messagebox.showinfo("Result", "Sorting Complete")
    root.mainloop()

def sorting_algorithm():
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Quick Sort": quick_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Heap Sort": heap_sort
    }

    root = tk.Tk()
    root.withdraw()

    choice = simpledialog.askstring("Input", "Choose algorithm (Bubble Sort/Quick Sort/Selection Sort/Insertion Sort/Merge Sort/Heap Sort):")
    if choice in algorithms:
        arr = [int(x) for x in simpledialog.askstring("Input", "Enter array elements separated by space:").split()]
        visualize_sort(algorithms[choice], arr)
    else:
        messagebox.showerror("Error", "Invalid algorithm choice")