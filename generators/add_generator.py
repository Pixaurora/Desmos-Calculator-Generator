from circuit import AND
from circuit import Input
from circuit import OR
from circuit import XOR

def add_generator(bits):
    a = Input(bits)
    b = Input(bits)

    c = []
    o = []

    for i in range(bits):
        if i == 0:
            c.append(AND(a[i], b[i]))
            o.append(XOR(a[i], b[i]))
        else:
            c.append(OR(AND(a[i], b[i]),AND(XOR(a[i], b[i]), c[i-1])))
            o.append(XOR(XOR(a[i], b[i]), c[i-1]))

    def add(x, y):
        a.number = x
        b.number = y

        return sum([output.compute()*2**i for i, output in enumerate(o+[c[-1]])])

    return add
