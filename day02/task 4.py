total=0
sign=1
d=1
for i in range(1000000):  
    total=total+sign/d
    sign=-sign
    d =d+2

pi=4*total
print(round(pi, 6))