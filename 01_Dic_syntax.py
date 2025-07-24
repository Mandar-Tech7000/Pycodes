MyDix = {
    "D": "Darandale Sanchit",
    "S": "My Owner", 
    "Sanchit": "Noob Coder",
    "DS": [1, 5, 2, 4],
    "Anotherdix": {'sanchit': 'Coder'}
}

print(MyDix["D"])
print(MyDix["S"])

MyDix['DS'] = [9, 8, 7]
print(MyDix["DS"])
print(MyDix["Sanchit"])
print(MyDix['Anotherdix'])
print(MyDix['Anotherdix']["sanchit"])
