def sol(n, m, nlist):
    answer = 0
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nlist[j]
            if total % m == 0:
                answer += 1

    return answer

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    lis = [int(i) for i in input().split()]
    print(sol(n, m, lis))
