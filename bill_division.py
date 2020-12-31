def bonAppetit(bill, k, b):
    count = 0
    for i in range(len(bill)):
        if i != k:
            count += bill[i]
    b_actual = count // 2
    if b_actual != b:
        print(b - b_actual)
    else:
        print('Bon Appetit')


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
