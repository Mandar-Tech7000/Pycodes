# ----------------------------------------------------------------------------------------------------------------------------- #
                                                        # PRACTICE SET #
# ----------------------------------------------------------------------------------------------------------------------------- #

'''
1) Write a program to create a dictionary of Hindi Words with values as their English Translation provide user with an option to look it up.

2) Write a program to input eight number from the user and display all the unique numbers (once)

3) Can we have a set with 18(int) and "18"(str) as a value in it?

4) What will be the length of the following set s:
   s = set()
   s.add(20)
   s.add(20.0)
   s.add("20")

5) S = {} 
   What Is The Type of Set ?

6) Create an empty dictionary allow 4 friends to enter their favourite language as values and use keys as their names . Assume that their names are unique.

7) If name of 2 friends are same; What will do the program in problem no. 6 ?

8) If language of 2 friends are same, what will happen to the program in problem no. 6?
'''

# ----------------------------------------------------------------------------------------------------------------------------- #

# 1) ==>
'''
Hindi = {
    "Namaste": "Hello",
    "Khel": "Game",
    "Dibba": "Box",
    "Sabun": "Soap",
    "Dudh": "Milk"
}

print("Your Options Are :", Hindi.keys())

D  = input("Enter The Hindi Word : ")

# print("The Meaning Of Your Word Is :", Hindi.[D])

# Below Line Will Not Through a Error if the key (Word) Is Not Present In The Dictionary !
print("The Meaning Of Your Word Is :", Hindi.get(D))

# ----------------------------------------------------------------------------------------------------------------------------- #

# 2) ==>

DS1 = int(input("Enter Number 1: "))
DS2 = int(input("Enter Number 2: "))
DS3 = int(input("Enter Number 3: "))
DS4 = int(input("Enter Number 4: "))
DS5 = int(input("Enter Number 5: "))
DS6 = int(input("Enter Number 6: "))
DS7 = int(input("Enter Number 7: "))
DS8 = int(input("Enter Number 8: "))


DS = {DS1, DS2, DS3, DS4, DS5, DS6, DS7, DS8}
print(DS)

# ----------------------------------------------------------------------------------------------------------------------------- #

# 3) ==>

ds = {18, "18"}

print(ds)
print(len(ds))

# ----------------------------------------------------------------------------------------------------------------------------- #

# 4) ==>

s = set()
s.add(20)
s.add(20.0)
s.add("20")

print(len(s)) # It Show 2, Bcos It Count 20 & 20.0 As One Item 

# ----------------------------------------------------------------------------------------------------------------------------- #
'''
# 5) ==>

e = {}
print(type(e)) # It Show 'Dict'

# ----------------------------------------------------------------------------------------------------------------------------- #

# 6) ==>

favlang = {}

A = input("Enter Your favourite Language Shiv: ")
B = input("Enter Your favourite Language Shlok: ")
C = input("Enter Your favourite Language Ovi: ")
D = input("Enter Your favourite Language Sanskruti: ")

favlang["Shiv"] = A
favlang["Shlok"] = B
favlang["Ovi"] = C
favlang["Sanskruti"] = D

print(favlang)