acumulador=0
while True:
    print()
    valor_unitario = float(input("ingrese el valor unitario: "))
    print()
    iva = input("¿el producto cuenta con IVA? ")
    print()
           
    cantidad = int(input("ingrese la cantidad de productos a llevar: "))
    print()
    
    if iva=="S":
        
        porcentaje = valor_unitario*0.19
   
        acumulador+=(valor_unitario + porcentaje)*cantidad
        
        
        print("IVA INCLUIDO")
        print()
        print("SUBTOTAL: ", acumulador)
        print()
   
    if iva=="N":
            
            acumulador+=(valor_unitario)*cantidad
            print("IVA NO INCLUIDO")
            print()
            print("SUBTOTAL: ", acumulador)
    print()       
    productos = input("¿faltan productos por cobrar? ")
    print()
    if productos=="S":
        pass
    else:
        print()
        print(f"Gracias por usar nuestro servicios!, usted debe pagar {acumulador}")
        break

   