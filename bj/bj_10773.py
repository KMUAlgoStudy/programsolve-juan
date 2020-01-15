if __name__ == '__main__':
    k = int(input())
    list = []
    for i in range(k):
        n = int(input())
        if n == 0:
            l = len(list)
            if not l == 0:
                list.pop(l-1)
        else:
            list.append(n)
    print(sum(list))