import tkinter as tk

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

#window section
window = tk.Tk() # yeh ek  window create karta hai
window.title('Calculator')

# Make the window non-resizable
window.resizable(False, False)

frame = tk.Frame(window, bg=colour_gray_blue)
label = tk.Label(frame, text='0', font=('Arial', 45), bg=colour_lake, 
                fg=colour_lake, anchor='e')
            
label.grid(row=0, column=0, columnspan=column_count, rowspan=1, padx=8, pady=8, sticky='nsew')

for row in range(row_count):
    for col in range(column_count): 
        value = button_values[row][col]
        button = tk.Button(frame, text=value, font=('Arial', 15),
                           width=5, height=2, bg=colour_soft_stone_gray, fg=colour_lake,
                           command=lambda value=value: button_clicked(value))
        button.grid(row=row+1, column=col, padx=5, pady=5,)

def button_clicked(value):
    pass

frame.pack()
window.mainloop()




