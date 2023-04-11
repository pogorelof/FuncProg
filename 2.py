import tkinter as tk

root = tk.Tk()

root.title("M Logo")

canvas = tk.Canvas(root, width=200, height=200, bg="white")

canvas.create_oval(20, 20, 180, 180, fill="red", outline="red")
canvas.create_oval(50, 50, 150, 150, fill="white", outline="white")
canvas.create_text(100, 100, text="M", font=("Helvetica", 50, "bold"), fill="red")

canvas.pack()

root.mainloop()
