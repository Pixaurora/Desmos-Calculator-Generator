from generators import add_generator
from converters import convert_latex

add = add_generator(6, name1='x', name2='y')

important = convert_latex(add)

file = open("output.txt", "w")

file.write(important)

file.close()