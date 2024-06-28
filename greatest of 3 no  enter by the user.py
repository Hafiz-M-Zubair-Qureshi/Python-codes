a= int(input("enter first number="))
b= int(input("enter second number="))
c= int(input("enter third number="))
d= int(input("enter fourth number="))

if(a>=b and a>=c and a>=d):
    print("first number is largest=",a)
elif(b>=c and b>=d):
    print("second number is largest=",b)
elif(c>=d):
    print("third number is lergest=",c)
else:
    print("fourth number is lergest=",d)
