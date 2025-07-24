# ------------------------------------------------------------------------------ #
'''
1) Write a program to find greatest of four numbers entered by user.

2) Write a program to find out whether a student is pass or fail, if it requires total 40% and atleast 35% in each subject to pass. assume 3 students and take marks as an input from user.

3) A Spam comment is defined as a text containing following keywords:
   "Make A lot of money","buy Now","Subscribe this","Click this". write a program to detect these spams. 

4) Write a program to find whether a given username contain less than 10 character or not 

5) Write a program which finds out whether a given name is present in a list or not.

6) Write a program to calculate a grade of a student from his marks from following scheme:
    90 - 100 = Ex
    80 - 90 = A
    70 - 80 = B
    60 - 70 = C
       < 50 = D

7) Write a program to find out whether a given post is talking about "sanchit" or not.

'''

# ------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------ #

# 1) ==>
'''
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
num3 = int(input("Enter Number 3: "))
num4 = int(input("Enter Number 4: "))

if (num1>num4):
    N1 = num1
else:
    N1 = num4

if(num2>num3): 
    N2 = num2
else:
    N2 = num3

if (N1>N2):
    print("The Greatest Number Is: ", N1)
else:
    print("The Greatest Number Is: ", N1)

# ------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------ #

# 2) ==>
    
m1 = int(input("Enter Your 1st Subject mark: "))
m2 = int(input("Enter Your 2nd Subject mark: "))
m3 = int(input("Enter Your 3rd Subject mark: "))

if (m1<35 or m2<35 or m3<35):
    print("You are Fail in a one of the subject")
elif(m1+m2+m3)/3 < 35:
    print("You Are Fail because your marks is less than 40%")
else:
    print("Congratulation ! You Are pass !")

# ------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------ #

# 3) ==>

text = input("Enter The Comment: ")

if ("make a lot of money" in text):
    spam = True
elif ("buy now" in text):
    spam = True
elif ("subscribe" in text) :
    spam = True
elif ("click this" in text):
    spam = True
else:
    spam = False


if (spam == True):
    print("This is Spam !!")
else:
    print("This Is Not a Spam !")

# ------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------ #

# 4) ==>

u = input("Enter The Username: ")

if (len(u)) == 10:
    print("The Character In The Username Is 10")
else:
    print("The Character In The Username Is Not 10, The Length Of Username Is: ", len(u))

# ------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------ #

# 5) ==>

names = ["sanchit", "shiv", "raj", "rakshit", "shlok", "sanskruti", "ovi"]
name = input("Enter Name To Check: ")

if (name in names):
    print("Name Is Present In The List")
else: 
    print("The Name Is Not Present In The List")

# ------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------ #

# 6) ==>

marks = int(input("Enter Your Marks: "))

if marks>=90:
    Grade = "Ex"
elif marks>=80:
    Grade = "A"
elif marks>=70:
    Grade = "B"
elif marks>=60:
    Grade = "C"
elif marks>=50:
    Grade = "D"
elif marks>=35:
    Grade = "F"
elif marks<35:
    Grade = "Fail"
else: 
    print("You Are Fail !")

print("Your Grade Is: ", Grade)

# ------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------ #
'''
# 7) ==>

comment = input("Enter Any Comment on post: ")

if ("SANCHIT" in comment):
    talk = True
elif ("sanchit" in comment):
    talk = True
elif ("Sanchit" in comment):
    talk = True
elif ("SaNcHiT" in comment):
    talk = True
elif ("sAnChIt" in comment):
    talk = True
elif ("SANchit" in comment):
    talk = True
elif ("sanCHIT" in comment):
    talk = True
else:
    talk = False

if (talk == True):
    print("Given Post is talking About sanchit 😎")
else:
    print("Given Post Is Not Talking About Sanchit 😢")