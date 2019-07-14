from generators import add_generator
from converters import convert_latex

bits = int(input("Input an integer: "))

add = add_generator(bits, name1='x', name2='y')

important = convert_latex(add)

file = open("output.txt", "w")

file.writelines([f'Bits: {bits}\n', important])

file.close()