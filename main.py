import itertools

digits = list(range(9, -1, -1))
operators = ['+', '-']
res = 200

for op_combination in itertools.product(operators, repeat=len(digits) - 1):
    expression = [str(digits[i]) + op for i, op in enumerate(op_combination)]
    expression.append(str(digits[-1]))

    iterations = itertools.product(range(0, 2), repeat=9)
    for i in iterations:
        localExpression = expression.copy()
        posList = [index for index, j in enumerate(i) if j == 1]
        for index, pos in enumerate(posList):
            localExpression[pos] = localExpression[pos][0]

        resultExpressionInStrFormat = ''.join(localExpression)
        if eval(resultExpressionInStrFormat) == res:
            print(resultExpressionInStrFormat)
            exit(0)

# для res=200 результат - 98+76-5+43-2-10
