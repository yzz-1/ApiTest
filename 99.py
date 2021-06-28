for i in range(1,10):
    for j in range(1, i+1):
        print(str(j) + '*' + str(i) + '=' + str(i*j), end=' ')
    print('')


k = [1, 7, 3, 1, 10]

for i in range(1, len(k)):
    for j in range(0, len(k)-1):
        if k[j] > k[j+1]:
            k[j], k[j+1] = k[j+1], k[j]
        else:
            pass
print(k)


def Collatz():
    num = input('请输入一个整数')
    while int(num) != 1:
        if int(num) % 2 == 0:
            i = int(num) // 2
            print(int(num) // 2)
        elif int(num) % 2 == 1:
            i = 3 * int(num) + 1
            print(3 * int(num) + 1)
        num = i

if __name__ == '__main__':
    Collatz()