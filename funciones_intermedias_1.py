x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
len(x)
#Actualizar valores
x[1][0]=15
print(x)
print('------------')

estudiantes[0]['last_name']='Bryant'
print(estudiantes)
print('------------')

directorio_deportes['fútbol'][0]='Andres'
print(directorio_deportes['fútbol'])
print('------------')

z[0]['y']=30
print(z)
print('------------------------------------------------')

#iterar a traves de una lista de diccionarios
estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iteratedictionary(lista):
    for i in range (0, len(lista)):
        resultado= ""
        for clave,valor in lista[i].items():
            resultado += f" {clave} - {valor}"
        print(resultado)

iteratedictionary(estudiantes)
print('------------------------------------------------')

# obtener valores de una lista de diccionarios

def interatediccionary_2(lista,clave):
    for i in range(0,len(lista)):
        for x,y in lista[i].items():
            if x== clave:
                print(y)

interatediccionary_2(estudiantes,'first_name')
print('------------')
interatediccionary_2(estudiantes,'last_name')

print('------------------------------------------------')

# Iterar a través de un diccionarios con valores de lista

dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printinfo(dicc):
    for clave,valor in dicc.items():
        print(" ")
        print(f"{clave} {len(valor)}")
        for i in range (0,len(valor)):
            print(valor[i])

printinfo(dojo)