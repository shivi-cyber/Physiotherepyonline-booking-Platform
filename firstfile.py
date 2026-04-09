# # marks = float(input("enter ur marks: "))
# # if(marks >= 90):
# #     print("your grade is A+")
# # elif(marks < 90 and marks>= 80): 
# #     print("your grade is A")
# # elif(marks < 80 and marks>= 70): 
# #     print("your grade is B+")
# # elif(marks < 70 and marks>= 60): 
# #     print("your grade is B")
# # elif(marks < 60 and marks>= 50): 
# #     print("your grade is C")
# # elif(marks < 50 and marks>= 40): 
# #     print("your grade is D")
# # elif(marks < 40 ): 
# #     print("you are fail")
# # else:
# #     print("enter again")
   
# """num = float(input("enter a number: "))
# if(num%2 == 0):
#     print("this is even")
# elif(num%2 != 0):
#     print("this is odd")"""

# num1 = float(input("enter a number1: "))
# num2 = float(input("enter a number2: "))
# num3 = float(input("enter a number3: "))
# num4 = float(input("enter a number4: "))
# if(num1 > num2 and num2 > num3 and num3 > num4):
#     print("greatest number is", num1)
# elif(num2 > num3 and num3 > num4):
#     print("greatest number is", num2)
# elif(num3 > num4):
#     print("greatest number is", num3)
# else:
#     print("greatest number is", num4)


# num7 = int(input("enter a number:"))
# if(num7%7 == 0):
#     print("it is a multiple")
# elif(num7/7 != 0):
#     print("not a multiple")
# else:
#     print("enter again")
# 4


# listp = [1,2,4,3,2,1]
# listm = listp.copy()
# listp.reverse()
# if(listm == listp):
#     print("this is palindrome")
# elif(listm != listp):
#     print("this is not plandrome")
    
# else:
#     print("check again")

# tup = ("c","D","A","A","B","B","A")
# print(tup.count("A"))

# list = ["C","D","A","A","B","B","A"]
# list.sort()
# print(list)


# dictt = { "cat" : "a small animal",
#          "table": ["a piece of furniture", "list of facts"]
#          }
# print(dictt)

# dictt = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++","C"}
# print(len(dictt))
# print(type(dictt))

# dict = {}
# mark1 = int(input("enter ur phy marks: "))
# mark2 = int(input("enter ur che marks: "))
# mark3 = int(input("enter ur math marks: "))
# dict.update({"phy" : mark1})
# dict.update({"che" : mark2})
# dict.update({"math" : mark3})
# print(dict)


# set1 = {
#      ("float",9.0),("int", 9)
#  }
# print(set1)

# i = 1
# while i <= 10:
    
#     print(i*i)
#     i += 1
# print("loop ended")

# tup = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# x = 49
# idx = 0
# while idx < len(tup): 
#     if(tup[idx] == x ):
#         print("found at ", idx)
#     idx += 1
    
# print(type(tup))
    
    
# l = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# idx = 0
# for num in l:
#     if(num == 36):
#         print("found at", idx)
#     idx += 1

# n = 4
# fac = 1

# for i in range(1, n+1):
#     fac = i*fac
    
# print(fac)
    
    

# i = int(input("Enter a number: "))
# sum = 0
# it = 1
# while it <= i:
#     sum += i
#     it += 1
    
# print( sum )

#funtions
# listl = ["k", "r", "t"]
# def fun(list):
#     print("elements are:", list)
    
# fun(listl)
    
# def print_list(list):
#     for item in list:
#         print(item, end=" ")

# listl = ["rt","ty", "ew"]
# print_list(listl)

# n = 5

# def fun_fac(a):
#     fac= 1
#     for val in range(1,a+1):
#         fac *= val
#     print(fac)
        
# fun_fac(5)


# def fum_ch(n):
   
#     v = n*83
#     print("INR: ",v)
    
# fum_ch(45)

#recursion
# def sum(n):
#     if( n == 1):
#         return 1
#     else:
#         return n+sum(n-1)
    
# print(sum(10))

# listl = ["u", "m", "p", "e", "r"]
# def pr(list,idx):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     pr(list,idx+1)
    
# pr(listl,0)
    
    
#i/o file
# # with open("sample.txt","w") as f:
# #     f.write("this is java file\nstudying java\nlearning i/o")
 
# with open("sample.txt", "r") as f:
#     data = f.read()
        
# ndata = data.replace("java", "python")
# print(ndata)

# # with open("sample.txt", "w") as f:
# #     f.write(ndata)

# with open("sample.txt", "r") as f:
#     data = f.read()
#     if(data.find("python") != -1):
#         print("found")
        
#     else:
#         print("not found")

# class Student:
    
    
#     def __int__(self, name, marks, subject):
#         self.name = name
#         self.marks = marks
#         self.subject = subject
#         print("adding new data")
        
# s1 = Student("nishu", 45, "evs")
# print(s1.marks, s1.name, s1.subject)
# class Student:
     
#      def __init__(self, fullname):
#          self.name = fullname
#          print("adding new")
         
        
     
# s1 = Student("shivani")
# print(s1.name)

# class Student:
    # def __init__(self, name,marks1,marks2, marks3):
    #     self.name = name
    #     self.marks1 = marks1
    #     self.marks2 = marks2
    #     self.marks3 = marks3
        
    # def avj(self):
    #     self.avg = ((self.marks1+self.marks2+self.marks3)/3)
    #     print("Average marks of",self.name," is ", self.avg)
        
 
# s1 = Student("sherro" ,34, 45, 66) 
# print(s1.avj())    


class Account:
    def __init__(self, balance, accNo):
        self.balance = balance
        self.accNo = accNo
    def deb(self,debAmount):
        self.debAmount = debAmount
        self.balance = self.balance - self.debAmount
        print("Amount debited ", self.debAmount)
        print("remaing Balance:" , self.balance )
        
    def crd(self,crdAmount):
        self.crdAmount = crdAmount
        self.balance = self.balance + self.crdAmount
        print("Amount credited ", self.crdAmount)
        print("remaing Balance:" , self.balance )
        

        
b1 = Account(3000,234)
b1.crd(400)
        
        
          
   

        
        
 
    
    
  