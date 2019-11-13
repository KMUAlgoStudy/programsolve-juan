brackets = []

def basicOpearate(n1, n2, op):
    if op=='+':
        return int(n1) + int(n2)
    if op=='-':
        return int(n1) - int(n2)
    if op=='*':
        return int(n1) * int(n2)
    if op=='/':
        return int(n1) / int(n2)
    if op=='**':
        return int(n1) ** int(n2)
    if op=='%':
        return int(n1) % int(n2)

def eval_(equation):
    global brackets
    open = []
    close = []
    previous = None
    current_count = 0
    depth = 0
    equation.replace(" ", "")
    for n, i in enumerate(equation):
        if i == '(':
            if previous == ')' and depth > 0:
                for n2 in range(n-depth, n):
                    close.append(n2)
                depth = 0
            else:
                current_count += 1
                if current_count > depth:
                    depth = current_count
            open.append(n)
            previous = '('
        if i == ')':
            current_count -= 1
            close.append(n)
            previous = ')'
    if len(open) < len(close):
        return "Need more open bracket"
    if len(open) > len(close):
        return "Need more close bracket"
    brackets = list(zip(open, close))
    return brackets


if __name__ == '__main__':
    print(eval_(input()))
