# Arithmetic Formatter
import numpy as np

def answer(sepp):
    if sepp[1]=='+':
        ans = int(sepp[0]) + int(sepp[2])
    else:
        ans = int(sepp[0]) - int(sepp[2])
    return ans

def maximum(sepp):
    max = np.zeros(len(sepp),dtype=int)
    for i in range(len(sepp)):
        if len(sepp[i][0]) >= len(sepp[i][2]):
            max[i] = len(sepp[i][0])
        else:
            max[i] = len(sepp[i][2])
    return max

def splitter(problem):
    sepp = []
    for i in problem:
        sepp.append(i.split())
    return sepp

def arithmetic_arranger(problem, arg):
    errors = 0
    operandError = 0
    digitsError = 0
    if len(problem) > 5:
        errors += 1
        print('Error: Too many problems.')

    for i in problem:
        problem_split = i.split()
        if operandError==0 and problem_split[1]!='-' and problem_split[1]!='+':
            operandError += 1
            errors += 1
            print('Error: Operator must be + or -.')
        elif digitsError==0 and (problem_split[0].isnumeric()==False or problem_split[2].isnumeric()==False):
            digitsError += 1
            errors += 1
            print('Error: Numbers must only contain digits.')
        elif digitsError==0 and (len(problem_split[0])>4 or len(problem_split[2])>4):
            errors += 1
            print('Error: Numbers cannot be more than four digits.')

    if errors==0:
        sepp = splitter(problem)
        max = maximum(sepp)
        spacing = '    '
        for i in range(len(sepp)):
            dist = max[i] + 2 - len(sepp[i][0])
            print(f'{sepp[i][0].rjust(len(sepp[i][0])+dist)}{spacing}',end='')

        print(f'\n',end='')
        for i in range(len(sepp)):
            dist = max[i] + 1 - len(sepp[i][2])
            print(f'{sepp[i][1]}{sepp[i][2].rjust(len(sepp[i][2])+dist)}{spacing}',end='')

        print(f'\n',end='')
        for i in range(len(sepp)):
            dash = '-'
            for j in range(max[i] + 1):
                dash += '-'
            print(f'{dash}{spacing}',end='')

        if arg==True:
            print(f'\n',end='')
            for i in range(len(sepp)):
                ans = str(answer(sepp[i]))
                dist = max[i] + 2 - len(ans)
                print(f'{ans.rjust(len(ans)+dist)}{spacing}',end='')


