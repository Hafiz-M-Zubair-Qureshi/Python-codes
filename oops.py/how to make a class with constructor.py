# class Student:
#     college_name="Punjab college"
#     def __init__(self,name,marks):
#             self.name=name
#             self.marks=marks
#             print("Adding new student in Database...")
# s1=Student("Ali",97)
# print(s1.name,s1.marks)

# s2=Student("Noman",87)
# print(s2.name,s2.marks)
# print(Student.college_name)




# class Student:
#     college_name="Punjab college"
#     def __init__(self,name,marks):
#             self.name=name
#             self.marks=marks
#     def welcome(self):
#           print("welcome student",self.name)
#     def get_marks(self):
#           return self.marks
    
# s1=Student("Ali",97)
# s1.welcome
# print(s1.get_marks)


# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def get_avg(self):
#         sum=0
#         for i in self.marks:
#             sum +=i
#         print("Hi",self.name,"Your avg score is:",sum/3)

# s1=Student("Ali",[99,98,97])
# s1.get_avg()



# static method
# class Student:
#     @staticmethod      # decorator
#     def college():
#         print("ABC college")
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def get_avg(self):
#         sum=0
#         for i in self.marks:
#             sum +=i
#         print("Hi",self.name,"Your avg score is:",sum/3)

# s1=Student("Ali",[99,98,97])
# s1.get_avg()



# abstraction
# class Car:
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False

#     def start(self):
#         self.clutch=True
#         self.acc=True
#         print("car started...")

# car1=Car()
# car1.start()        





# create account class with 2 attributes 'balance and account no. Credit method for debit,credit and printing the balance
# class Account:
#     def __init__(self,bal,acc):
#         self.balance=bal
#         self.account_no=acc

#     def debit(self,amount):
#         self.balance -=amount
#         print("Rs",amount,"was detected")
#         print("total balance=",self.get_balance())

#     def credit(self,amount):
#         self.balance +=amount
#         print("Rs",amount,"was credited")
#         print("total balance = ",self.get_balance())

#     def get_balance(self):
#         return self.balance
    

# acc1=Account(10000,12345)
# acc1.debit(1000)
# acc1.credit(500)







