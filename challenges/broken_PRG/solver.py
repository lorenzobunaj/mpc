

'''
def retrieve_r(U, seeds, l):
    k = 10

    leaks = []
    leaks.append(U[0] ^ PRG(seeds[0], 0) ^ k)
    for i in range(1, l):
        leaks.append(U[i] ^ PRG(seeds[i], i) ^ ((i + 1) * k))

    #leaks[0] ^ leaks[1] = k[0][1 - s[0]] ^ k[1][1 - s[1]]
    #leaks[1] ^ leaks[2] = k[1][1 - s[1]] ^ k[2][1 - s[2]]
    #...
    #leaks[n-1] ^ leaks[n] = k[n-1][1 - s[n-1]] ^ k[n][1 - s[n]]

    unknown_seeds = [Int(f'k[{i}]') for i in range(l)]

    solver = Solver()

    for i in range(l-1):
        solver.add(Xor(leaks[i], leaks[i+1]) == Xor(unknown_seeds[i], unknown_seeds[i+1]))

    if solver.check() == sat:
        model = solver.model()
        solution = [model[unknown_seeds[i]].as_long() for i in range(8)]
        for i in range(8):
            print(f"{solution[i]}", end=" ")
    else:
        print("No solution found.")
'''