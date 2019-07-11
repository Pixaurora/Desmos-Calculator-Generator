def convert_latex(function):
    return_list = []
    J = [gate.convert_latex(as_list=True) for gate in function.outputs]

    for i, j in enumerate(J):
        for k in j:
            return_list.append(f'{2**i}{k}')

    return '+'.join(return_list)
