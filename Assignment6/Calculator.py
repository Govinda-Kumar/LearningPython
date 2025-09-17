from tkinter import *

window = Tk()

window.title("Simple Calculator")
window.geometry("350x400") 
window.configure(bg="lightblue")
window.resizable(False, False)


entry = Entry(window, width=16, font=("Arial", 24), bd=0, relief="flat", highlightthickness=0, insertwidth=4, bg="powder blue", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=8, pady=8)

def button_click(number):
    entry.insert(END, str(number))

def button_clear():
    entry.delete(0, END)

def button_delete():
    current = entry.get()
    if current:
        entry.delete(len(current)-1, END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, END)
        entry.insert(0, "Error")

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+',
    'DEL'
]

row_val = 1
col_val = 0

def make_btn(text, cmd):
    return Button(window, text=text, padx=20, pady=20, command=cmd, bd=0, relief="flat", highlightthickness=0, bg="white", activebackground="#e6e6e6")

for button in buttons:
    if button == 'C':
        btn = make_btn(button, button_clear)
    elif button == 'DEL':
        btn = make_btn(button, button_delete)
    elif button == '=':
        btn = make_btn(button, button_equal)
    else:
        btn = make_btn(button, lambda b=button: button_click(b))

    btn.grid(row=row_val, column=col_val, padx=4, pady=4, sticky="nsew")

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1


for i in range(4):
    window.grid_columnconfigure(i, weight=1)

window.bind('<BackSpace>', lambda e: button_delete())

window.mainloop()