
import sys
from collections import deque


def conversion_to_postfix(infix_expression):
    postfix_expr = []
    p1 = '^'
    p2 = ['*', '/']
    p3 = ['+', '-']
    expr = ''.join((' {} '.format(el) if el in '()^*/+-' else el for el in infix_expression))
    expr = expr.split(' ')
    expr = [x for x in expr if x.strip()]
    stack_expr = deque()
    for x in expr:
        if x.isdigit() or x.isalpha():
            postfix_expr.append(x)
        elif len(stack_expr) == 0 and (x in p1 or x in p2 or x in p3 or x == '('):
            stack_expr.append(x)
        elif stack_expr[-1] == '(' and (x in p1 or x in p2 or x in p3):
            stack_expr.append(x)
        elif x in '(':
            stack_expr.append(x)
        elif x in ')':
            while stack_expr:
                if stack_expr[-1] == '(':
                    stack_expr.pop()
                    break
                else:
                    postfix_expr.append(stack_expr.pop())
            # Incoming Higher precedence and top element is lower precedence
        elif x in p2 and stack_expr[-1] in p3:
            stack_expr.append(x)
            #  equal precedence for * and /
        elif x in p1 and stack_expr[-1] in p2:
            stack_expr.append(x)
        elif x in p2 and (stack_expr[-1] in p2 or stack_expr[-1] in p1):
            while stack_expr:
                if stack_expr[-1] in p3 or stack_expr[-1] == '(':
                    break
                else:
                    postfix_expr.append(stack_expr.pop())
            stack_expr.append(x)
            # Incoming Lower precedence and top element higher precedence . Equal precedence for + and -
        elif x in p3 and (stack_expr[-1] in p1 or stack_expr[-1] in p2 or stack_expr[-1] in p3):
            while stack_expr:
                if stack_expr[-1] == '(':
                    break
                else:
                    postfix_expr.append(stack_expr.pop())
            stack_expr.append(x)
    while stack_expr:
        postfix_expr.append(stack_expr.pop())
    return postfix_expr


def assignment_variables(input_expr):
    check = input_expr.replace(" ", "").split("=")
    assert check[0].isalpha(), 'Invalid identifier'
    if check[0].isalpha() and check[1].isdigit():
        if check[0] not in variables_dict:
            variables_dict.update({check[0]: check[1]})
        else:
            variables_dict[check[0]] = check[1]
    elif check[0].isalpha() and check[1].isalpha():
        assert check[1].isalpha(), 'Invalid assignment'
        if check[1] not in variables_dict:
            print("Unknown variable")
        else:
            variables_dict[check[0]] = variables_dict.get(check[1])
    else:
        print("Invalid assignment")


#  Processing postfix expression
def expression_calculate(input_expression):
    postfix_expr = conversion_to_postfix(input_expression)
    stack_calc = deque()
    for x in postfix_expr:
        if x.isdigit():
            stack_calc.append(x)
        elif x.isalpha():
            val = int(reading_variable(x))
            assert val is not None, "Unknown Variable"
            stack_calc.append(val)
        elif x in ('*', '+', '-', '/', '^') and stack_calc:
            v2 = int(stack_calc.pop())  # top element
            v1 = int(stack_calc.pop())
            if x in ('*', '+', '-', '/'):  # Power convert to **
                calc = str(v1) + x + str(v2)
                stack_calc.append(eval(calc))
            else:
                stack_calc.append(v1 ** v2)
    print(stack_calc[-1])


# reading variables from dictionary
def reading_variable(variable):
    return variables_dict.get(variable)


variables_dict = {}
while True:
    try:
        i = input()
        if i == '':
            continue
        elif i.startswith('/'):
            assert i == '/exit' or i == '/help', "Unknown command"
            if i == '/exit':
                print('Bye!')
                sys.exit()
            else:
                print('The program evaluate expressions')
        elif i.isdigit() or i.strip('-').isdigit():
            print(i)
            continue
        elif '=' in i:
            assignment_variables(i)
        elif '*' in i or '+' in i or '-' in i or '/' in i or '^' in i or '(' in i or ')' in i:
            for_eval = i
            for_eval = for_eval.replace('^', '**')
            # Expression validation
            eval("".join(x if not x.isalpha() else variables_dict.get(x) for x in for_eval))
            # Expression Reduction
            count = i.count('-')
            while count != 0:
                if count % 2 == 0:
                    i = i.replace('-' * count, '+')
                else:
                    i = i.replace('-' * count, '-')
                count -= 1
            count = i.count('+')
            while count != 0:
                i = i.replace('+' * count, '+')
                count -= 1
            count = i.count('/')
            if count > 1:
                while count != 1:
                    assert i.find('/' * count) < 0, 'Invalid Expression'
                    count -= 1
            expression_calculate(i)
        elif '=' not in i:
            assert i.strip(' ').isalpha(), 'Invalid Identifier'
            value = reading_variable(i)
            assert value is not None, "Unknown Variable"
            print(value)
    except AssertionError as msg:
        print(msg)
    except SyntaxError:
        print('Invalid Expression')
    except NameError:
        print('Unknown Variable')
    except TypeError:
        print('Unknown Variable')
