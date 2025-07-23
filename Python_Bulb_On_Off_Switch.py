import tkinter as tk

def turn_on():
    canvas.itemconfig(bulb_glass, fill='yellow')
    for glow in glow_layers:
        canvas.itemconfig(glow, state='normal')
    status_label.config(text="Bulb is ON", fg="yellow")

def turn_off():
    canvas.itemconfig(bulb_glass, fill='white')
    for glow in glow_layers:
        canvas.itemconfig(glow, state='hidden')
    status_label.config(text="Bulb is OFF", fg="white")

root = tk.Tk()
root.title("Bulb Glow ON/OFF")
root.configure(bg="black")

canvas = tk.Canvas(root, width=220,
       height=320, bg='black', highlightthickness=0)
canvas.pack(pady=10)

glow_colors = ['#ffff66', '#ffeb3b', '#ffe033', '#ffd700']
glow_coords = [(10, 0, 190, 220), (20, 10, 180, 210), 
               (30, 20, 170, 200), (40, 30, 160, 190)]
glow_layers = []

for color, coords in zip(glow_colors[::-1], glow_coords[::-1]):
    glow = canvas.create_oval(coords, fill=color, 
                        outline='', state='hidden')
    glow_layers.append(glow)

bulb_glass = canvas.create_oval(50, 40, 150, 180, 
                 fill='white', outline='gold', width=4)
canvas.create_polygon(80, 180, 120, 
                     180, 110, 220, 90, 220, fill='light gray', outline='gold', width=3)
canvas.create_rectangle(75, 220, 125, 
                    260, fill='dim gray', outline='gold', width=3)

for y in [230, 240, 250]:
    canvas.create_line(75, y, 125, y,
                        fill='black', width=2)

status_label = tk.Label(root, text="Bulb is OFF",
          fg="white", bg="black", font=("Arial", 14))
status_label.pack()

btn_frame = tk.Frame(root, bg="black")
btn_frame.pack()

tk.Button(btn_frame, text="ON", command=turn_on, 
          width=10, bg='green', fg='white', font=("Arial", 10, "bold")
          ).grid(row=0, column=0, padx=15, pady=10)
tk.Button(btn_frame, text="OFF", command=turn_off, 
          width=10, bg='red', fg='white', font=("Arial", 10, "bold")
          ).grid(row=0, column=1, padx=15, pady=10)

root.mainloop()
