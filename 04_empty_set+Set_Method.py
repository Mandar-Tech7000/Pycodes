# --------------------------------------------------------------------------------------------- #
                                     # EMPTY SET !!
# --------------------------------------------------------------------------------------------- #
        # Important : This syntx will create an empty dictionary and it is not empty set !

a = {}
print(type(a)) # It Show 'dict'

# An Empty set can be create using the below method/syntax 

b= set()
print(type(b)) # It Show 'set'

# --------------------------------------------------------------------------------------------- #
                                   # SET METHODS !!
# --------------------------------------------------------------------------------------------- #


#Creating An Empty Set
d = set()

## Adding Value In Empty set 
d.add(1)
d.add(2)
d.add(5)
d.add(1) # It Will Not Show In Answer Bcos It Is Set Of Non Repetative element (Repeat nahi honar)
d.add((4, 5, 6))

# d.add([1, 2, 5]) # It Not Work !
# d.add({1, 5}) # It Not Work !

print(d) 

# --------------------------------------------------------------------------------------------- #

## LENGTH OF THE SET !
print(len(d)) # Print The Length Of Set

## REMOVAL OF AN ITEM ! 
d.remove(2)     # remove 2 from set d 
# d.remove(12)  # through an error when try to remove 12 (Which Is not present In The Set)
print(d)


print(d.pop()) #
print(d)