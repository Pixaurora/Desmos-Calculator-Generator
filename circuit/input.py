class Input:
    """An arbitrary Input to a Logic Gate. This is useful for making it so the value can be changed when computed.
    """

    __slots__ = ('max_inputs', 'inputs', 'outputs', 'kind')

    def __init__(self, name: str):
        self.name = name
        self.value = None # Can be either True or False by default.
        self.outputs = []

    def change_value(self, new_value: bool):
        self.value = new_value

    def get_value(self) -> bool:
        return self.value

    def add_output(self, new_output):
        self.outputs.append(new_output)