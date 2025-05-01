def odd_eve(n):
    if (n == 0): return "Zero"
    elif (n%2 == 0): return "Even"
    else: return "Odd"
    
n = int(input("Enter a number: "))
print(odd_eve(n))