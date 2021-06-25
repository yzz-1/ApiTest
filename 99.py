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