from tkinter import *

expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" Error ")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="white")
    gui.title("Calculator")

    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation,
                             font=("Helvetica", 20), justify="right")
    expression_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

    button_texts = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        'C', '0', '=', '+'
    ]

    row_val = 1
    col_val = 0
    for text in button_texts:
        if text == '=':
            button = Button(gui, text=text, bg='#f39c12', fg='white', font=(
                "Helvetica", 18), command=equalpress)
        elif text == 'C':
            button = Button(gui, text=text, bg='#e74c3c',
                            fg='white', font=("Helvetica", 18), command=clear)
        else:
            button = Button(gui, text=text, bg='#3498db', fg='white', font=(
                "Helvetica", 18), command=lambda t=text: press(t))

        button.grid(row=row_val, column=col_val,
                    ipadx=15, ipady=15, padx=1, pady=1)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

    gui.mainloop()
