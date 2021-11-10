def grade(op):
    if op == '(':
        return 0
    elif op in "+-":
        return 10
    elif op in '*/':
        return 20
    else:
        return -1


def in_to_post(in_express):
    stack_operator = []
    post_express = ''
    stack_operator.append('(')
    for c in in_express:
        if c in '0123456789':
            post_express += c
        elif c == '(':
            stack_operator.append('(')
        elif c == ')':
            while stack_operator[-1] != '(':
                post_express += stack_operator.pop(-1)
            stack_operator.pop(-1)
        elif c in '+-*/':
            while grade(c) <= grade(stack_operator[-1]):
                post_express += stack_operator.pop(-1)
            stack_operator.append(c)
    while stack_operator[-1] != '(':
        post_express += stack_operator.pop(-1)
    stack_operator.pop(-1)
    del stack_operator
    return post_express


def calculate_post(post_express):
    stack_operand = []
    for c in post_express:
        if c in '0123456789':
            stack_operand.append(c)
        else:
            operand_right = stack_operand.pop()
            operand_left = stack_operand.pop()
            stack_operand.append(eval("{}{}{}".format(operand_left, c, operand_right)))
    return stack_operand.pop()


if __name__ == '__main__':
    in_ex = '(5+7)/2-((8-5）*2+（1+2)*3)/3'
    post_ex = in_to_post(in_ex)
    print('中缀表达式:"{}"'.format(in_ex))
    print('后缀表达式:"{}"'.format(post_ex))
    result = calculate_post(post_ex)
    print(result)

