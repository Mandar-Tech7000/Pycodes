'''Typecasting Is a Way To Convert One Datatype To Another (If Possible)!'''

DS = "0102"

print(type(DS)) # ==> It Showing Str
# print(DS - 2)   ==> It Not Work !

DS = int(DS)
print(type(DS)) # ==> Hence, It showing Int 
print(DS - 2)   # ==> It Substract From 0102 - 2 = 0100


# Some Examples !

A = "20"
B = 10.0
C = 1

print(type(A))  # ==> str
print(type(B))  # ==> Float
print(type(C))  # ==> int

# Try To Change Variable Type And Use The Typecasting Function !

A = float(A)    # ==> 20.0
B = int(B)      # ==> 10
C = str(C)      # ==> '1'

print(A)        # Change, 
print(B)        # Datatype,
print(C)        # Successfully !
 
print(type(A))  # ==> float
print(type(B))  # ==> int
print(type(C))  # ==> str