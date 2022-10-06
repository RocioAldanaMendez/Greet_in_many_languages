#Greet in many languages
#declaro variables
mi_diccionario = {
'russian' :  'Privet mir',
'portuguese' : 'Ola mundo',
'french' : 'Salut monde',
'german' : 'Hallo Welt',
'chinese' : 'Ni hao',
'spanish' : 'Hola mundo',
'indian' : 'Namaste duniya',
'japanese' : 'Kon nichiwa sekai',
'holandes' : 'Hallo Wereld',
'ucraniano' : 'Privit Svit',
'polaco' : 'Witaj swiecie'}

#pido entrada al usuario
print("Ingrese el idioma en que quiere que lo saluden: ")
lenguage = input()

print(mi_diccionario[lenguage])

