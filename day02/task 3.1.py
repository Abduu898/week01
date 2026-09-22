n = 10
if n%2 ==0:
    print("even")
else:
    print("odd")



n = 123456789 * 987654321
total = 0
while n > 0:
    total = total + n % 10   # add the last digit
    n = n // 10              # remove the last digit

print(total)


n = 123456789 * 987654321
total = 0
while n > 0:
    total = total + n % 10   # add the last digit
    n = n // 10              # remove the last digit

print(total)


for x in (12.24,424242.8412):
    print(float(x))
