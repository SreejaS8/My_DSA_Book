def positive_negative(n):
    if (n>0): return "Positive"
    elif (n == 0): return "Given number is Zero"
    else: return "Negative"

n = int(input("Enter a number: "))
print(positive_negative(n))
