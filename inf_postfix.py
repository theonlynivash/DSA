'''BEGIN
  Initialize empty stack
  Initialize empty output list

  SCAN expression from LEFT to RIGHT, one token at a time:

  CASE 1: Token is an OPERAND (number or variable)
          → Append directly to output

  CASE 2: Token is '('
          → Push onto stack

  CASE 3: Token is ')'
          → WHILE top of stack is not '('
                Pop from stack → Append to output
          → Pop and DISCARD the '(' itself

  CASE 4: Token is an OPERATOR ( +, -, *, /, ^ )
          → WHILE stack is not empty
               AND top of stack is not '('
               AND precedence(top of stack) >= precedence(current token)
                    Pop from stack → Append to output
          → Push current operator onto stack

  END OF EXPRESSION:
          → WHILE stack is not empty
                Pop from stack → Append to output

  Output list is the final Postfix expression
END'''
def precendence(operand):
    if operand == "^":
        return 2
    elif operand == '*' or '/':
        return 1
    elif operand == '+' or '-':
        return 0
    
def infix_to_postfix(exp):
    postfix = []
    stack = []
    for i in exp:
        if i.isalnum():
            postfix.append(i)
        elif i == "(":
            stack.append('(')
        elif i == ")":
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        elif i in ("+","-","/","*","^"):
            while len(stack) != 0 and stack[-1]!="(" and precendence(stack[-1]) >= precendence(i):
                postfix.append(stack.pop())
            stack.append(i) 
    while len(stack) != 0:
        postfix.append(stack.pop())
    return postfix

print(infix_to_postfix("A*(B+C)/D-E^F+G"))