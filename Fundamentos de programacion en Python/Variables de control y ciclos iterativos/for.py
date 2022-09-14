


for i in range(11): #excluye11
    print("valor de i es:", i)
    
    
    
for i in range(0,11,2): #excluye11 #(aumenta de 2 en 2)
    print("valor de i es:", i)
    
        
for i in range(10,-2,-2): #excluye11 #(decrementa de 2 en 2)
    print("valor de i es:", i)
    
v1= int(input("vi: "))
vf=int(input("vf: "))
p=int(input("p: "))

for i in range(v1,vf,p): #excluye11 #(decrementa de 2 en 2)
    print("valor de i es:", i)  #323 6979701


ciclo = "andres"
for i in ciclo:
    print(i, end= " ")

#funcion continue

for i in range(10):
    if i==5:
        continue #continue va a obviar o omitir mi condicion y sigue con el ciclo
    print(i)

for m in range(10):
    if m==5:
        break #continue va a obviar o omitir mi condicion y sigue con el ciclo
    print(m)
print("its over")