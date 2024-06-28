# WAP to find the sum of first n numbers using while loop
# for n=7
n=7
sum=0
i=1
while i<=n:
    sum+=i
    i+=1

print("total sum=", sum)   



# WAP to find the factorial of first n numbers using for loop
n=5
fact=1

for i in range(1,n+1):
    fact*=i
print("factorial=",fact)   