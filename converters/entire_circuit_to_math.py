import itertools

from circuit import AND
from circuit import XOR

class python_converters:
    @classmethod
    def fix_or(cls, element):
        return [cls.fix_and(element), cls.fix_xor(element)]

    @classmethod
    def fix_and(cls, element):
        return list(itertools.chain([f'{i}*{j}' for j in cls.fix(element[1])] for i in cls.fix(element[0])))

    @classmethod
    def fix_xor(cls, element):
        return [
            [cls.fix(i) for i in element.inputs]
        ]

    @classmethod
    def fix_input(cls, element):
        return ['{name}//2**{p}%2'.format(name=element.name, p=element.position)]

    @classmethod
    def fix(cls, element):
        translate = {
            "OR": cls.fix_or,
            "AND": cls.fix_and,
            "XOR": cls.fix_xor,
            "bit": cls.fix_input
        }

        return translate[element.kind](element)

def convert_python(f):
    output = []
    for i, element in enumerate(f.outputs):
        tmp = python_converters.fix(element)
        for j in itertools.chain(tmp):
            output.append("{factor}*{normal}+".format(factor=2**i, normal=j))

    return output[0:-1]

