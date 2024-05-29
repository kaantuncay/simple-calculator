import tkinter as tk

def clear():
    entry.delete(0, tk.END)

def button_click(value):
    current = entry.get()
    clear()
    entry.insert(0, current + value)

def calculate():
    try:
        result = round(eval(entry.get()), 6)
        clear()
        entry.insert(0, str(result))
    except:
        clear()
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")

# Entry widget for displaying the input and output
entry = tk.Entry(root, width=15, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Button configuration
button_config = {
    'font': ('Arial', 18),
    'bg': 'lightblue',
    'fg': 'black',
    'width': 4,
    'height': 2,
    'relief': 'solid',
    'borderwidth': 1
}

# Button creation
buttons = [
    ('C', 1, 0, lambda: clear()),
    ('()', 1, 1, lambda: button_click('()')),
    ('%', 1, 2, lambda: button_click('%')),
    ('/', 1, 3, lambda: button_click('/')),
    ('7', 2, 0, lambda: button_click('7')),
    ('8', 2, 1, lambda: button_click('8')),
    ('9', 2, 2, lambda: button_click('9')),
    ('*', 2, 3, lambda: button_click('*')),
    ('4', 3, 0, lambda: button_click('4')),
    ('5', 3, 1, lambda: button_click('5')),
    ('6', 3, 2, lambda: button_click('6')),
    ('-', 3, 3, lambda: button_click('-')),
    ('1', 4, 0, lambda: button_click('1')),
    ('2', 4, 1, lambda: button_click('2')),
    ('3', 4, 2, lambda: button_click('3')),
    ('+', 4, 3, lambda: button_click('+')),
    ('+/-', 5, 0, lambda: button_click('-')),
    ('0', 5, 1, lambda: button_click('0')),
    ('.', 5, 2, lambda: button_click('.')),
    ('=', 5, 3, lambda: calculate())
]

# Add buttons to the grid
for (text, row, col, cmd) in buttons:
    tk.Button(root, text=text, command=cmd, **button_config).grid(row=row, column=col)

root.mainloop()
