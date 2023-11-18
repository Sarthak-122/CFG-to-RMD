import tkinter as tk

def convert_to_rightmost_derivation():
    grammar = {
        'S': ['AB', 'BC'],
        'A': ['a'],
        'B': ['b'],
        'C': ['c']
    }
    input_string = input_entry.get()
    derivation = convert_to_rightmost_derivation_recursive(grammar, input_string)
    output_label.config(text=' -> '.join(derivation))

def convert_to_rightmost_derivation_recursive(grammar, input_string):
    def find_production(non_terminal):
        for production in grammar[non_terminal]:
            if production[0].isupper():
                inner_production = find_production(production[0])
                if inner_production:
                    return inner_production + production[1:]
            else:
                return production

    stack = [input_string]
    derivation = []
    while stack:
        current_symbol = stack.pop()
        if current_symbol.isupper():
            production = find_production(current_symbol)
            if production:
                stack.extend(production[::-1])
                derivation.append(' -> '.join(production))
        else:
            derivation.append(current_symbol)

    return derivation[::-1]


root = tk.Tk()
root.title('CFG to Rightmost Derivation Converter')

input_label = tk.Label(root, text='Enter input string:')
input_label.pack()

input_entry = tk.Entry(root, width=30)
input_entry.pack()

convert_button = tk.Button(root, text='Convert', command=convert_to_rightmost_derivation)
convert_button.pack()

output_label = tk.Label(root, text='')
output_label.pack()

root.mainloop()
