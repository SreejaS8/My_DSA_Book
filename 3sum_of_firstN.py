def sum_of_firstN(n):
    s = 0
    for i in range(n+1): s += i
    return s

n = int(input("Enter a number: "))
print(sum_of_firstN(n))