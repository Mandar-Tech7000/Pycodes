MyDix = {
    "D": "Darandale Sanchit",
    "S": "My Owner", 
    "Sanchit": "Noob Coder",
    "DS": [1, 5, 2, 4],
    "Anotherdix": {'sanchit': 'Coder'}
}

print(MyDix.keys())   # It Show Keys Like 'D', 'S', 'sanchit' Etc
print(MyDix.values()) # It Show Value Of Key like "Darandale Sanchit", "Noob Coder" etc
print(MyDix.items())  # It Show All Key And Value From Dictionary (Mydix)

print(MyDix)
newdix = {
    "My Friend": "You", # , is Very Important
    "Your Friend": "Me" # It Will Add New Keys In Dictionary (Mydix)
}
MyDix.update(newdix)
print(MyDix)

print(MyDix.get("DS"))