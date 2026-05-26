
import tkinter as tk
import math

button_values = [
    ['AC', '+/-', '%', '÷', '∑'],
    ['7', '8', '9', 'x', 'π'],
    ['4', '5', '6', '-', '^'],
    ['1', '2', '3', '+', '//'],
    ['0', '.', '√', '=', '!']
]

right_symbols = ['∑', 'π', '^', '//', '!']
top_symbols = ['AC', '+/-', '%', '÷']

row_count = len(button_values)
column_count = len(button_values[0])

colour_soft_stone_gray =  '#EAE6E3'
colour_warm_blush_pink = '#ECCDC4'
colour_more_tan_than_pink = '#D5B19B'
colour_gray_blue = '#7F9593'
colour_lake = '#1F4045'
colour_black = '#000000'
colour_forest_green = '#2C3E50'

#window section
window = tk.Tk() # yeh ek  window create karta hai
window.title('Calculator')

# Make the window non-resizable 
window.resizable(False, False)

frame = tk.Frame(window, bg=colour_gray_blue)
label = tk.Label(frame, text='0', font=('Arial', 45), bg=colour_lake, 
                fg=colour_soft_stone_gray, anchor='e')
            
label.grid(row=0, column=0, columnspan=column_count, rowspan=1, padx=8, pady=8, sticky='nsew')

for row in range(row_count):
    for col in range(column_count): 
        value = button_values[row][col]
        button = tk.Button(frame, text=value, font=('Arial', 15),
                           width=5, height=2, bg=colour_soft_stone_gray, fg=colour_lake,
                           command=lambda value=value: button_clicked(value))
        button.grid(row=row+1, column=col, padx=5, pady=5, sticky='nsew')
        if value in right_symbols:
            button.config(bg=colour_warm_blush_pink, fg=colour_forest_green)
        if value in top_symbols:
            button.config(bg=colour_warm_blush_pink, fg=colour_forest_green)
        # else:
        #     button.config(fg=colour_black)

def convert_exp(expression):

    symbol_map = {
        'x': '*',
        '÷': '/',
        '√': 'sqrt',
        '∑': 'sum',
        'π': 'pi',
        '^': '**',
        '//': '//',
        '!': 'factorial'
    }

    for calculator_symbol, python_symbol in symbol_map.items():
        expression = expression.replace(calculator_symbol, python_symbol)

    return expression

def button_clicked(value):
    current_text = label['text']

    if value in right_symbols:
        pass
    elif value in top_symbols:
        pass
        if value == 'AC':
            label.config(text='0')
            return
        elif value == '+/-':
            text = current_text
            if text.startswith('-'):
                text = text[1:]
            else:
                text = '-' + text
            label.config(text=text)
    elif value == '%':
        text = current_text
        if text.endswith('%'):
            text = text[:-1]
        label.config(text=text)

    if current_text == '0':
        label.config(text=value)
        return
    
    if value == '=':
        current_text = convert_exp(current_text)
        result = eval(current_text)
        label.config(text=str(result))
        return
    
    else:
        label.config(text=current_text + value)


frame.pack(padx=10, pady=10)

 # window ki postion screen center pai shift karta hai
window.update() # window ko upadte karta hai
window_height = window.winfo_height()
window_width = window.winfo_width()
screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()

window_x = int(screen_width / 2 - window_width / 2)
window_y = int(screen_height / 2 - window_height / 2)

# window geometry = (w)*(h)+(x)+(y)
window.geometry(f'{window_width}x{window_height}+{window_x}+{window_y}')

window.mainloop()