# ax + by + cz = d ---> [a, b, c, d]

system = [[0, 2, 3, 4],
          [7, 1, 4, 1],
          [1, 4, 8, 6]]

# Multiplies each coefficient in the equation by a number
def multiplyEquation(equation, multiple):
    return [i*multiple for i in equation]

# Adds two equations together (collects like terms)
def addEquations(equation1, equation2):
    return [i + j for (i, j) in zip(equation1, equation2)]

# Eliminates one variable from a system of linear equations to reduce the problem
def eliminateVariable(equations):
    first_equation = equations[0]
    new_equations = []
    for equation in range(1, len(equations)):
        factor = (equations[equation][0] / first_equation[0]) * -1
        new_equations.append(addEquations(multiplyEquation(first_equation, factor), equations[equation])[1::])
    return new_equations

# Ensures that the first element of the first equation in the system is non-zero
def sortEquations(equations):
    # Quite a crude way to ensure the first element is not zero, but it works well enough
    if equations[0][0] == 0:
        for eq in range(len(equations)):
            if equations[eq][0] != 0:
                equations[eq], equations[0] = equations[0], equations[eq]
                break
    return equations

# Uses Gaussian Elimination to solve the system of linear equations (recursion)
def GaussianElimination(equations):
    if len(equations[0]) == 2:
        return [equations[0][1] / equations[0][0]]
    else:
        solutions = []
        for solution in GaussianElimination(eliminateVariable(equations)):
            solutions.append(solution)
        for equation in equations:
            total = 0
            for i in range(len(solutions)):
                total += equation[i+1]*solutions[i]
            solutions.insert(0, (equation[-1] - total) / equation[0])
            break
        return solutions

# Checks if the solutions satisfy all of the equations
def CheckSolutions(system, solutions):
    for equation in system:
        total = 0
        for term in range(len(solutions)):
            total += equation[term]*solutions[term]
        if total != equation[-1]:
            return False
    return True


system = sortEquations(system)
solutions = GaussianElimination(system)
print(solutions)
CheckSolutions(system, solutions) # True if the solution works for all equations (false if there is no solution)
