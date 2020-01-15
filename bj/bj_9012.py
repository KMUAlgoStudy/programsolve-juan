def isCorrectBrackets(string):
    open_count = 0
    prev = None
    if not string[0] == "(" and not string[-1] == ")":
        return "NO"
    for i in string:
        if i == "(":
            if i == prev:
                open_count += 1
            prev = "("
        if i == ")":
            if i == prev:
                open_count -= 1
            prev = ")"
        if open_count < 0:
            return "NO"

    if open_count == 0:
        return "YES"
    return "NO"

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        brackets = input()
        print(isCorrectBrackets(brackets))