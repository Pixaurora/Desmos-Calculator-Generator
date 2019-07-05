def AND(gate):
    return gate[0].compute() & gate[1].compute()

def OR(gate):
    return gate[0].compute() | gate[1].compute()

def XOR(gate):
    return gate[0].compute() ^ gate[1].compute()

def NOT(gate):
    return not gate[0].compute()

COMPUTATIONAL_KEYS = {
    "AND" : AND,
    "OR" : OR,
    "XOR" : XOR,
    "NOT" : NOT
}
