def main():
#---------PRIMER CUADRADO-------
    CantP = 0
    CantComp = []
    CantC = 0
    CantPrt = []
    Prt = 0
    UltDigi = 0
#----------FIN PRIMER CUADRADO------

    while True:
        try:
        #--------SEGUNDO CUADRADO-------
            CP = int(input("Ingresa el código de pieza (0 para salir): "))
            
        #-----FIN SEGUNDO CUADRADO------
            
            # Si CP es 0, sale del programa
        #-------PRIMER CONDICIONAL
            if CP == 0:
                print("Finalizó el programa. Se procesaron", CantP, "piezas")
                print("Se procesaron", sum(CantComp), "componentes")
                print("Se obtuvo como precio total por todas las piezas", sum(CantPrt))
                break
        #------TERMINA EL CODIGO CON CADA UNO DE SUS "PRINT"-------
            
        
        #CONDICIONALES 10 Y 11------
            if 1 <= CP <= 99:
            #-----INICIO BLOQUE 13------
                print(f"Código de pieza ingresado: {CP}")
                CantP += 1
                Prt = 0
                CantC = 0
            #----FIN BLOQUE 14----
                
                while True:
                    try:
                        CC = int(input("Inserte Código de componente (0 para ingresar otro CP, min 3 dígitos): "))
                        
                        # Si CC es 0, salir del bucle interno y pide otro CP
                    #-----INICIO CONDICIONAL 17-----
                        if CC == 0:
                            CantPrt.append(Prt)
                            CantComp.append(CantC)
                            print(f"Precio Total para la pieza {CP}: {Prt}")
                            break
                        
                        
                    #----CONDICIONAL 22-----
                        if 100 <= CC:
                            
                            print(f"Código de componente ingresado: {CC}")
                            UltDigi = CC % 100 # toma los dos ultimos valores para comparar con CP
                            
                            if UltDigi == CP:
                                print(f"Componente perteneciente al CP: {CP}")
                                
                                
                                while True:
                                    try:
                                        Prc = int(input("Ingresa precio del componente (de $1000 a $9999): "))
                                        
                                    #------CONDICIONAL 29 Y 30-----
                                        if 1000 <= Prc <= 9999:
                                            Prt += Prc
                                            CantC += 1
                                            print("Ingrese nuevo codigo de componente")
                                            break 
                                    #----BLOQUE 31----
                                        else:
                                            print(f"El precio {Prc} no tiene un valor válido, volver a ingresar")
                                    
                                    except ValueError: #Esto es para que no se puedan usar letras
                                        print("Entrada inválida. Por favor, ingresa un número entero.")
                            
                            else:
                                print(f"Código inválido, no corresponde con el CP: {CP}")
                        
                        else:
                            print("Código de componente inválido. Por favor, ingresa un código de componente de 3 dígitos.")
                    
                    except ValueError:
                        print("Entrada inválida. Por favor, ingresa un número entero.")
            
            else:
                print("Código inválido. Por favor, ingresa un código de pieza entre 1 y 99.")
        
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

#Esta linea es para poder importar un codigo, en este caso main para poder repetir todo y poder llamar a distintos bloques
if __name__ == "__main__":
    main()