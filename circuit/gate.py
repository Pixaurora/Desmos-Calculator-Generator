class Gate:
    """An arbitrary Logic Gate. This parent class is never used directly, but instead is used by all the other gates
    here. This is a strictly internal class.
    """

    __slots__ = ('required_inputs', 'inputs', 'kind')

    def __init__(self, kind: str, required_inputs: int, *inputs):
        self.kind = kind
        if len(inputs) == required_inputs:
            self.inputs = inputs
        else:
            raise KeyError("Too few or too many inputs entered.")

    def __getitem__(self, index):
        return self.inputs[index]


class AND(Gate):
    def __init__(self, *inputs):
        super().__init__("AND", 2, *inputs)

    def compute(self):
        return self[0].compute() & self[1].compute()

    def convert_python(self, as_list=False):
        I = self[0].convert_python(as_list=True)
        J = self[1].convert_python(as_list=True)

        return_list = []
 
        for i in I:
            for j in J:
                return_list.append(f'{i}*{j}')

        return return_list if as_list else '+'.join(return_list)

    def convert_latex(self, as_list=False):
        I = self[0].convert_latex(as_list=True)
        J = self[1].convert_latex(as_list=True)

        return_list = []

        for i in I:
            for j in J:
                return_list.append(f'{i}{j}')

        return return_list if as_list else '+'.join(return_list)



class XOR(Gate):
    def __init__(self, *inputs):
        super().__init__("XOR", 2, *inputs)

    def compute(self):
        return self[0].compute() ^ self[1].compute()

    def convert_python(self, as_list=False):
        return_statement = f'abs({self[0].convert_python()}-{self[1].convert_python()})'

        return [return_statement] if as_list else return_statement

    def convert_latex(self, as_list=False):
        return_statement = f'\\left|{self[0].convert_latex()}-{"-".join(self[1].convert_latex(as_list=True))}\\right|'

        return [return_statement] if as_list else return_statement

class OR(Gate):
    def __init__(self, *inputs):
        super().__init__("OR", 2, *inputs)

    def compute(self):
        return self[0].compute() | self[1].compute()

    def convert_python(self, as_list=False):
        return_list = [self[0].convert_python(), self[1].convert_python()]

        return return_list if as_list else '+'.join(return_list)

    def convert_latex(self, as_list=False):
        return_list = [self[0].convert_latex(), self[1].convert_latex()]

        return return_list if as_list else '+'.join(return_list)


class NOT(Gate):
    def __init__(self, input):
        super().__init__("NOT", 1, input)

    def compute(self):
        return not self[0].compute()

    def convert_python(self, as_list=False):
        return_statement = f'1-{self[0].convert_python()}'

        return [return_statement] if as_list else return_statement

    def convert_latex(self, as_list=False):
        return_statement = f'1-{self[0].convert_latex()}'

        return [return_statement] if as_list else return_statement
