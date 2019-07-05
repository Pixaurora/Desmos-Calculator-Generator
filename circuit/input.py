class Input:
    """An arbitrary Logic Gate. This parent class is never used directly, but instead is used by all the other gates
    here. This is a strictly internal class.
    """

    __slots__ = ('max_inputs', 'inputs', 'outputs', 'kind')

    def __init__(self, kind: str, max_inputs: int, *inputs):
        self.kind = kind
        self.inputs = []
        self.outputs = []

        for i in inputs:
            i.add_output(self)

    def add_output(self, new_output):
        self.outputs.append(new_output)