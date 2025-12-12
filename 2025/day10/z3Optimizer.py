import z3

def solveFastestPath(buttons, b):
        ### Process one line
    s = z3.Optimize()
    X = [z3.Int('x%s' % i) for i in range(len(buttons))]

    for i in range(len(b)):
        constraint = ""
        for j, one_combo in enumerate(buttons):

            if type(one_combo) == int:
                if i == one_combo:
                    constraint += X[j]
                continue

            if i in one_combo:
                constraint += X[j]

        s.add(constraint == b[i])

    for i in range(len(buttons)):
        s.add(X[i] >= 0)

    s.minimize(sum(X))
    s.check()
    numButtonPresses = sum([int(s.model()[a].as_long()) for a in s.model()])
    
    return numButtonPresses