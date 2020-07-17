for x in range(int(input())):
    s1 = set(input())
    s2 = set(input())
    if s1.intersection(s2):
        print('YES')
    else:
        print('NO')

    