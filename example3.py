from components import Adder

bits = int(input("Input an integer to represent how many bits : "))

adder = Adder(bits)

file = open("output.txt", "w")

file.writelines([f'Bits: {bits}\n', adder.convert_latex()])
file.close()
print("Successfully written.")
