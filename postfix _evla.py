def postfix_eval(postfix):
    stack = []
    for i in postfix:
        if i.isalnum():
            stack.append(i)
        elif i in ('*','/','+','-','^'):
            a = int(stack.pop(-2))
            b = int(stack.pop(-1))
            if i == '+':
                stack.append(a+b)
            elif i == '-':
                stack.append(a-b)
            elif i == '*':
                stack.append(a*b)
            elif i == '/':
                stack.append(a/b)
            elif i == '^':
                stack.append(a^b)
    return stack.pop()

print(postfix_eval("`3 4 2 + *"))