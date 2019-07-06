from math import floor
from math import log

class Bit:
    """An arbitrary Bit to input to a Logic Gate. This is useful for making it so the value can be changed when
    computed.
    """

    __slots__ = ('value', 'name', 'position', 'outputs', 'kind')

    def __init__(self, name:str, position:int):
        self.value = None  # Can be either True or False by default.
        self.kind = "bit"
        self.name = name
        self.position = position # Used to check the index of the bit. Mostly used when transforming it.
        self.outputs = []

    def change_value(self, new_value: bool):
        self.value = new_value

    def get_value(self) -> bool:
        return self.value

    def __mul__(self, other: int):
        return self.value * other

    def add_output(self, new_output):
        self.outputs.append(new_output)

    def compute(self):
        return self.value


class Input:
    """An input to a function. Is made up of bits.
    """

    def __init__(self, bits: int, name:str):
        self.bits = bits
        self.name = name
        self.bit_list = [Bit(name, i) for i in range(bits)]

    def __getitem__(self, index: int) -> Bit:
        return self.bit_list[index]

    def set_number(self, new_number: int):
        if floor(log(new_number, 2)) >= self.bits:
            raise ValueError("This number has too many bits!")

        for i, bit in enumerate(self.bit_list):
            bit.change_value(floor(new_number / 2 ** i) % 2)

    def get_number(self) -> int:
        return sum([bit * 2 ** i for i, bit in enumerate(self.bit_list)])

    number = property(get_number, set_number)
