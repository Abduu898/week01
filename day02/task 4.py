total=0
sign=1
d=1
for i in range(1000000):  
    total=total+sign/d
    sign=-sign
    d =d+2

pi=4*total
print(round(pi, 6))


def pi_calculate(n):
    if n == 0:
        return 0
    odd = 2 * n - 1
    return odd * odd / (6 + pi_calculate(n - 1))

pi = 3 + pi_calculate(1000)
print(round(pi, 6))