# WAF to print the length of list
cities=["multan","ISL", "LHR", "FSD","Karachi","PES"]
heroes=["Ali","Zubair","Hamza","Abdullah"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)



# WAF to print the element of list in a single line
heroes=["Ali","Zubair","Hamza","Abdullah"]

def print_len(list):
    for item in list:
        print(item,end=" ")
print_len(heroes)



# WAF to find the factorail of n(n is the parameters)
def calc_fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(calc_fact(5))  # Output: 120



# convert USD to PKR
def convertor(usd_val):
    pkr_val=usd_val*280
    print(usd_val,"USD=",pkr_val,"PKR")
convertor(2)





# input number from user and check whether it is even or odd
def zubair():
    n=int(input("enter your number"))
    if (n%2==0):
        print("even")
    else:
        print("odd")
zubair()