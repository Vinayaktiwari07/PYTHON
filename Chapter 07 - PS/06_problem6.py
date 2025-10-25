n = int(input("Enter a number: "))
fact = 1

i = 1
for i in range(1, n+1):
    fact *= i
    # i +=1
   

print(f"The factorial of {n} is {fact}")