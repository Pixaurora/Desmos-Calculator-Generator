from .component import Component


class LogicGate(Component):
    """An arbitrary Logic Gate.

    By default, no conversion or computation is implemented, but is instead
    implemented by the other children classes.

    Attributes
    ----------
        inputs: List[Component]
            A list of all the inputs to the Logic Gate. By default, any type is
            allowed however.
        kind: str
            The kind of gate. This is usually handled by the internal classes
            only.
    """

    __slots__ = ('inputs', 'kind')

    def __init__(self, kind: str, required_inputs: int, *inputs):
        """Creates the Logic Gate.

        Arguments
        ---------
        kind: str
        required_inputs: int
            The amount of inputs allowed to be inputted.
        *inputs: List[Union[LogicGate, Bit]]
        """
        self.kind = kind
        if len(inputs) == required_inputs:
            self.inputs = inputs
        else:
            raise KeyError("Too few or too many inputs entered.")

    def __getitem__(self, index: int):
        """Used to replicate list-like syntax with LogicGate[index]

        Arguments
        ---------
        index: int
        """
        return self.inputs[index]

    def compute(self):
        """Computes the gate's value."""
        raise NotImplementedError("This internal class isn't meant to be used.")

    def __str__(self):
        """Convert the Logic Gate to a string in the syntax of Python.

        IE LogicGate(*inputs) and also convert those inputs to a string and so
        on...
        """
        return f'{self.kind}({", ".join([str(i) for i in self.inputs])})'

    def convert_latex(self, as_list=False):
        """Convert the Logic Gate to a string in the syntax of LaTeX.

        This one is much more complicated as the math that it gets converted to
        may vary.
        """
        raise NotImplementedError("This internal class isn't meant to be used.")


class And(LogicGate):
    """An AND Logic Gate."""

    def __init__(self, *inputs):
        super().__init__("And", 2, *inputs)

    def compute(self):
        return self[0].compute() & self[1].compute()

    def convert_latex(self, as_list=False):
        I = self[0].convert_latex(as_list=True)
        J = self[1].convert_latex(as_list=True)

        return_list = []

        for i in I:
            for j in J:
                return_list.append(f'{i}{j}')

        return return_list if as_list else '+'.join(return_list)


class Or(LogicGate):
    """An OR Logic Gate."""

    def __init__(self, *inputs):
        super().__init__("Or", 2, *inputs)

    def compute(self):
        return self[0].compute() | self[1].compute()

    def convert_latex(self, as_list=False):
        """Converts  the gate to LaTeX code, for use in Desmos."""

        left = '{'
        right = '}'
        return_statement = f'\\operatorname{left}sign{right}\\left({self[0].convert_latex()}+{self[1].convert_latex()}\\right)'

        return [return_statement] if as_list else return_statement


class Xor(LogicGate):
    """An XOR Logic Gate."""

    def __init__(self, *inputs):
        super().__init__("Xor", 2, *inputs)

    def compute(self):
        return self[0].compute() ^ self[1].compute()

    def convert_latex(self, as_list=False):
        """Converts  the gate to LaTeX code, for use in Desmos."""

        return_statement = f'\\left|{self[0].convert_latex()}-{"-".join(self[1].convert_latex(as_list=True))}\\right|'

        return [return_statement] if as_list else return_statement


class Not(LogicGate):
    """An NOT Logic Gate."""

    def __init__(self, input):
        super().__init__("Not", 1, input)

    def compute(self):
        return not self[0].compute()

    def convert_latex(self, as_list=False):
        """Converts  the gate to LaTeX code, for use in Desmos."""
        return_statement = f'1-{self[0].convert_latex()}'

        return [return_statement] if as_list else return_statement
