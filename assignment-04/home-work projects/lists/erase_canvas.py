import tkinter as tk

root = tk.Tk()
root.title("Blue Grid Canvas")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

square_size = 100

squares=[]
for row in range(5):
    for col in range(5):
        x1 = col * square_size
        y1 = row * square_size
        x2 = x1 + square_size
        y2 = y1 + square_size

        square = canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
        squares.append(square)

eraser_size = 50
eraser = canvas.create_rectangle(0, 0, eraser_size, eraser_size, fill="white", outline="gray")

# Function to move eraser with mouse
def drag_eraser(event):
    x = event.x
    y = event.y
    canvas.coords(eraser, x, y, x + eraser_size, y + eraser_size)

    # Get all canvas items touching the eraser
    overlapping = canvas.find_overlapping(x, y, x + eraser_size, y + eraser_size)

    for item in overlapping:
        if item in squares:
            canvas.itemconfig(item, fill="white")  # Erase the square

# Bind mouse drag to eraser movement
canvas.bind("<B1-Motion>", drag_eraser)


root.mainloop()
