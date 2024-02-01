import itertools

digits = list(range(9, -1, -1))
operators = ['+', '-']
res = 200

resultList = set([])
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
        if eval(resultExpressionInStrFormat) == res and resultExpressionInStrFormat not in resultList:
            resultList.add(resultExpressionInStrFormat)
            print(resultExpressionInStrFormat)

# для res=200 результат: 
# 98+76-5+43-2-10
# 98-7+65+43+2-1+0
# 98-7+65+43+2-1-0
# 9-8+7-6-5-4-3+210
# 9-8-7-6-5+4+3+210
