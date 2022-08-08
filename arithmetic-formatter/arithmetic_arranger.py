def requirements_check(problems): # takes list of ['123', '+', '123']

    status = None
    
    if len(problems) > 5:
        status = 'Error: Too many problems.'
    
    for problem in problems:
        if (problem[1] != '+' and problem[1] != '-'):
            status = "Error: Operator must be '+' or '-'."
        elif (problem[0].isdigit() == False or problem[2].isdigit() == False):
            status = 'Error: Numbers must only contain digits.'
        elif max(map(len, problem)) > 4:
            status = 'Error: Numbers cannot be more than four digits.'
    
    return status


def operate_expression(expression):
    # return expression in format [operand, operator + operand, dashes, result], all formated

    operated_expression = []
    length = max(map(len, expression)) + 2
    
    operated_expression.append(expression[0].rjust(length))
    operated_expression.append(expression[1] + ' ' + expression[2].rjust(length - 2))
    operated_expression.append('-' * length)

    if expression[1] == '+':
        result = int(expression[0]) + int(expression[2])
    else:
        result = int(expression[0]) - int(expression[2])
    
    operated_expression.append(str(result).rjust(length))

    return operated_expression


def concatenate(*args):

    line = '    '.join(args)
    
    return line


def arithmetic_arranger(problems, answers=False):
    
    operated_expressions = []
    # formatted_matrix = []
    problems = list(map(str.split, problems))
    
    status = requirements_check(problems)
    if status is not None:
        return status

    for problem in problems:
        operated_expressions.append(operate_expression(problem))

    matrix = list(map(concatenate, *operated_expressions))
    matrix[0] += '\n'
    matrix[1] += '\n'
    arranged_problems = matrix[0] + matrix[1] + matrix[2]
    
    if answers:
        arranged_problems = arranged_problems + '\n' + matrix[3]
    
    return arranged_problems
