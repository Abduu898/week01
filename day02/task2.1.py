total=0
current=0
i=1
while i <= 9:
    current = current * 10 + 1
    total=total+current
    i = i + 1

print(total)
print(pow(total,2))
print(pow(total,3))
print(pow(total,5))
