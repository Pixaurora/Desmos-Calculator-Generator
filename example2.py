from generators import add_generator
from converters import convert_python

add = add_generator(16)

print(convert_python(add))
