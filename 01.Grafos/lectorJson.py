import json
f = open('multiplos200Ref.json')
estructura = json.load(f)

# Imprimo los nodos que tienen vecindad derecha
for i in estructura['E']:
    print(i)

# Imprimo la vecindad derecha de a
print (estructura['E']['20'])

# Imprimo la cardinalidad derecha de a
print (len(estructura['E']['20']))

f.close()

