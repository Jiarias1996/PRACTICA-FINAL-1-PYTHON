#Paso 1 . Buscar el valor o definir el valor actual del euro y dolar con rescpto al peso Mexicano

tipo_cambio_eur_a_mex = 23.70
tipo_cambio_Usd_a_mex = 20.75

#Paso 2. Solicitar al usurio el tipo de conversion (euro a mex o dolar a mex)

tipo_cambio = input ("Ingrese moneda origen para la conversion (EUR/USD): "  )


#Paso 3. Solicitar al usuario el monto a convertir
    
monto_a_convertir = float (input("Ingrese el monto a convertir: "))


#Paso 4. Realizar la conversion utlizando el tipo de cambio correspondiente
#Paso 5. Mostrar el resultado de la conversion

if tipo_cambio.upper() == "EUR":   

    resultado = monto_a_convertir * tipo_cambio_eur_a_mex
    print("El resultado de la conversion de EUR a MEX es : ", resultado)

elif tipo_cambio.upper() == "USD":
        
    resultado = monto_a_convertir * tipo_cambio_Usd_a_mex
    print("El resultado de la conversion de USD a MEX es : ", resultado)  
else: 
    print ("No esta disponible esa operacion")
 