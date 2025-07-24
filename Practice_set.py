                     # Practice Set Programs For Solve #

'''
Q1) Write A Python Program To Display A User Entered Name Followed By Good Afternoon Using Input() Function.

Q2) Write A Program To Fill In A Letter Template Given Below With Name And Date.
    letter = "'Dear |<NAME>|,
             Greeting From DS Coding House ! You Are Selected ! Enjoy Your day !
             Thanks & Regards.
             |<DATE>|"'

Q3) Write A Program To Detect Dounble Spaces In A String.

Q4) Replace The Double Spaces From Problem 3 With Single Spaces.

Q5) Write A Program To Format the letter Using Escape Sequence Characters.
    letter = "Dear Sanchit, I am Happy To Meet You ! See You Soon ❤"

'''


                                 # Answers #
# ------------------------------------------------------------------------------- #

# Q1) ==>

DS= input("Name Of The User Is :")
O = "Good Afternoon, "

M = O + DS
print(M) # Verified ✅

# ------------------------------------------------------------------------------- #

# Q2) ==>

letter = '''
Dear |<NAME>|,
Greeting From DS Coding House ! 
You Are Selected !
 
Thanks & Regards.
|<DATE>|'''


D = input("Enter Your Name : ")
S = input("Enter Date : ")

letter = letter.replace("|<NAME>|", D)
letter = letter.replace("|<DATE>|", S)

print(letter) # Verify ✅

# ------------------------------------------------------------------------------ #
# Q3) ==>

SD = "Hello,  DS" 
print(SD.find("  "))

# ------------------------------------------------------------------------------ #
# Q4) ==>

print(SD.replace("  ", " ")) # Verify ✅

# ------------------------------------------------------------------------------ #
# Q5) ==>

letter = "Dear Sanchit, \n\tI am Happy To Meet You ! \n\tSee You Soon ❤"
print(letter) # Verify ✅




# ----------- Solutions Are Done & Verified, Thank You For Visit ❤ ------------ #