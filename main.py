a = [int(input()) for i in range(10)] #пусть в списке 10 чисел, которые вводятся
print(a)
l = 0
for i in range(len(a) - 1):
    if a[i] >= 0 and a[i + 1] >= 0 or a[i] < 0 and a[i + 1] < 0 and l == 0:
        print(a[i], a[i + 1])
        l += 1
        break
if l == 0:
    print()




