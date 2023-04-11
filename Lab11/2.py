import tkinter as tk

# Create a window
root = tk.Tk()

# Set the window title
root.title("Vladimir Logo")

# Create a canvas widget
canvas = tk.Canvas(root, width=450, height=200, bg="white")

# Draw the logo
canvas.create_text(150, 70, text="V", font=("Arial", 80, "bold"), fill="#4f7cac")
canvas.create_text(230, 95, text="ladimir", font=("Helvetica", 30), fill="#c0392b")
canvas.create_text(220, 140, text="Голосуйте за будущее!", font=("Helvetica", 30), fill="#c0392b")
# Pack the canvas widget
canvas.pack()

# Run the main event loop
root.mainloop()
