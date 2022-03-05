# def p(n):
#     if n == 0:
#         return
#     else:
#         p(n-1)
#         print(n)
# p(5)

pars = {")":"(", "]":"["}

def par_checker(string):
    stack = []

    for s in string:
        if s == "([":
            stack.append(s)
        elif s == ")]":
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            else:
                return False
    return len(stack) == 0

par_checker(str((5+6)*(7+8)/(4+3)))