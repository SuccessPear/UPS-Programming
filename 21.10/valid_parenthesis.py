# every open parenthesis must have closed one
# + - must have at least one operand on the right or the close bracket on the left
# * / must have 2 operands (number or close on the left, open on the right)

def is_valid_statement(equation: str) -> bool:
    open_sign = ['(','[', '{']
    close_open_sign_map = {')': '(', ']': '[', '}': '{'}
    operators = ['+', '-', '*', '/']
    stack = []
    
    is_number_after_operand = True
    
    for i in range(len(equation)):
        if equation[i].isnumeric():
            is_number_after_operand = True
        if equation[i] in open_sign:
            stack.append(equation[i])
        elif equation[i] in close_open_sign_map:
            if len(stack) == 0:
                return False
            if stack[-1] != close_open_sign_map[equation[i]]:
                return False
            else:
                stack.pop(-1)
        elif equation[i] in operators:
            is_number_after_operand = False
            if i == len(equation):
                return False
            if equation[i] == '+' or equation[i] == '-':
                if equation[i+1] in close_open_sign_map:
                    return False
            elif equation[i] == '*' or equation[i] == "/" :
                if i == 0:
                    return False
                if equation[i-1] in open_sign:
                    return False
                if equation[i+1] in close_open_sign_map:
                    return False
    if is_number_after_operand == False:
        return False
    if len(stack):
        return False
    return True


equation = '9 * (9)('
print(is_valid_statement(equation))