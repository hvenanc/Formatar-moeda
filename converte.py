import re

#Lista com valores formatadas no padrão brasileiro
valores = ['1,99','10,99','100,99','1.000,99','10.888,99','100.999,88']

def converter(lista):

    x = 0
    valoresFormatados = []
    while(x < len(lista)):
        
        item = str(lista[x])
        item = re.sub('[.]','',item)
        item = item.replace(',','.')
        valoresFormatados.append(float(item))
        x+=1
      
    return valoresFormatados

x = converter(valores)
print(x)
    
