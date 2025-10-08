#!/usr/bin/env python
# coding: utf-8

# In[137]:


import pandas as pd
import winsound
import matplotlib.pyplot as plt
import random
import openpyxl
import getpass 

def level():
    
    import winsound
    
    while True:
        
        level = int(input("Elige un nivel\n"
        "1. Fácil (20 intentos)\n"
        "2. Medio (12 intentos)\n"
        "3. Difícil (5 intentos)\n"
         "Introduce el nivel deseado:  "))
        
        if level == 1:
            return 20
            
        elif level == 2:
            return 12
        
        elif level == 3:
            return 5
            
        else:
            print  ("Opcion no valida, intentalo de nuevo")
            winsound.PlaySound('C:\Windows\Media\Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            
            
def Save_Data(nombre, resultado_partida, attempts, archivo = "Resultados.xlsx"):

    import openpyxl
    
    excel_doc = openpyxl.load_workbook('C:\EjerciciosPython\modulos\Resultados.xlsx')
    hoja= excel_doc['Resultados']
    hoja.append(["Nombre", "Resultado", "Intentos"])
    hoja.append([nombre, resultado_partida, attempts])
    excel_doc.save('C:\EjerciciosPython\modulos\Resultados.xlsx')
    print(f"Registro guardado exitosamente en {archivo}")



def solitario():
    
    
    number_to_guess = random.randint(1,1000)
    print("***** Bienvenido al modo solitario del juego: Adivina el numero ***** ")
    winsound.PlaySound('C:\Windows\Media\Windows Logon.wav', winsound.SND_FILENAME)
    
    
    attempts = 0
    total_attempts = level()
    resultado_partida = ''
    
    
    while attempts < total_attempts:
        
        number_tried = int(input(" Introduce un numero del 1 al 1000\n "))
        
        
        if number_tried <1 or number_tried > 1000:
            print(" El numero debe ser entre el 1 y el 1000. Intentalo de nuevo")
            winsound.PlaySound('C:\Windows\Media\Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            continue
            
        attempts +=1    
        
        if number_tried == number_to_guess:
            print(" HAS ACERTADO!! Enhorabuena has ganado la partida")
            winsound.PlaySound('C:\Windows\Media\tada.wav', winsound.SND_FILENAME)
            resultado_partida = 'partida ganada'
            break
            
        if number_tried != number_to_guess and attempts < total_attempts:
            print(" Has cometido un fallo!")
            winsound.PlaySound('C:\Windows\Media\Windows Hardware Fail.wav', winsound.SND_FILENAME)
            
            if number_tried < number_to_guess:
                print("El numero misterioso es un numero MAYOR")
                    
            if number_tried > number_to_guess:
                print("El numero misterioso es un numero MENOR")
                   
                    
    if attempts == total_attempts:  
        print("Ooooh has perdido esta partida, el numero era", number_to_guess)
        winsound.PlaySound('C:\Windows\Media\Windows Critical Stop.wav', winsound.SND_FILENAME)
        resultado_partida = 'partida perdida'
        
                
    nombre = input("Introduce tu nombre  \n") 
    Save_Data(nombre, resultado_partida, attempts, archivo = "Resultados.xlsx")

Menu_ppal()
    
def double_game():
   
    attempts = 0
    total_attempts = level()
    resultado_partida = ''
    
    print("***** Bienvenido al modo doble del juego: Adivina el numero.***** \n"
          "En esta opcion de juego el jugador 1 introducira un numero \n"
          "del 1 al 1000 y el jugador 2 tendra que adivinarlo. \n"
          "El numero introducido por el jugador 1 NO aparecera en la pantalla \n"
          "hasta que el juego concluya")
    winsound.PlaySound('C:\Windows\Media\Windows Logon.wav', winsound.SND_FILENAME)
    
    number_to_guess = int(getpass.getpass("JUGADOR 1: Introduce un numero del 1 al 1000"))

    
    
    while number_to_guess < 1 or number_to_guess > 1000:
        print("El número debe estar entre 1 y 1000. Intentalo de nuevo")
        number_to_guess = int(getpass.getpass("JUGADOR 1: Introduce un numero del 1 al 1000"))
        winsound.PlaySound('C:\Windows\Media\Windows Pop-up Blocked.wav', winsound.SND_FILENAME)     
                           
    while attempts < total_attempts:
        
        number_guessed = input("JUGADOR 2: Intenta adivinar el numero del 1 al 1000 que \n"
                            "el JUGADOR 1 ha introducido\n")
        
        number_guessed = int(number_guessed)
        
        if not (1 <= number_guessed <= 1000):
            print(" El numero debe ser entre el 1 y el 1000. Intentalo de nuevo")
            winsound.PlaySound('C:\Windows\Media\Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            continue   
            
            
        attempts +=1
        

            
        if number_guessed != number_to_guess and attempts < total_attempts:
            print(" Has cometido un fallo!")
            winsound.PlaySound('C:\Windows\Media\Windows Hardware Fail.wav', winsound.SND_FILENAME)
            
            if number_guessed < number_to_guess:
                print("El numero misterioso es un numero MAYOR")
                    
            if number_guessed > number_to_guess:
                print("El numero misterioso es un numero MENOR")
                
                
        if number_guessed == number_to_guess:
            print(" HAS ACERTADO!! Enhorabuena has ganado la partida")
            winsound.PlaySound('C:\Windows\Media\tada.wav', winsound.SND_FILENAME)
            resultado_partida = 'partida ganada'
            break
                   
                    
    if attempts == total_attempts and number_guessed != number_to_guess:  
        print("Ooooh has perdido esta partida, el numero era", number_to_guess)
        winsound.PlaySound('C:\Windows\Media\Windows Critical Stop.wav', winsound.SND_FILENAME)
        resultado_partida = 'partida perdida'
        
                
    nombre = input("Introduce tu nombre  \n") 
    
    Save_Data(nombre, resultado_partida, attempts, archivo = "Resultados.xlsx")
    
Menu_ppal()    
    
def Menu_estadistica():
    
    while True:
        print("***** Bienvenido al apartado de Estadísticas del juego: Adivina el número *****")
        winsound.PlaySound(r'C:\Windows\Media\Windows Logon.wav', winsound.SND_FILENAME)

        try:
            opcion = int(input("*** Menu ***\n"
                               "1. Resultados Generales\n"
                               "2. Top 5 jugadores\n"
                               "3. Filtrado por usuario\n"
                               "4. Volver a Menu principal\n"
                               "Elige una opción:\n"))

            if opcion == 1:
                Estadistica_general()  

            elif opcion == 2:
                Top_cinco()  

            elif opcion == 3:
                Estadisticas_jugador()  

            elif opcion == 4:
                print("Volviendo al Menú Principal...")
                return  # 🚀 Esto asegura que el menú se cierra correctamente y vuelve al principal

            else: 
                print("Opción no válida, inténtalo de nuevo.")  

        except ValueError:
            print("Error: Ingresa un número válido.")  

    
Menu_ppal() 

def Estadistica_general():
    
    df = pd.read_excel('C:\EjerciciosPython\modulos\Resultados.xlsx')
    partidas_ganadas = df[df['Resultado'] == 'partida ganada'].groupby('Nombre').size()
    partidas_perdidas = df[df['Resultado'] == 'partida perdida'].groupby('Nombre').size()
    intentos_totales = df.groupby('Nombre')['Intentos'].sum()
    
    resultados = pd.DataFrame({'Partidas Ganadas': partidas_ganadas,
                               'Partidas Perdidas': partidas_perdidas,
                               'Intentos Totales': intentos_totales}).fillna(0)
    
    print(resultados)

    ganadas = df[df['Resultado'] == 'partida ganada'].groupby('Nombre').size()
    
    plt.pie(ganadas, labels=ganadas.index)
    plt.title('Partidas ganadas por jugador')
    plt.show()
    
    perdidas = df[df['Resultado'] == 'partida perdida'].groupby('Nombre').size()
    
    plt.pie(perdidas, labels=perdidas.index)
    plt.title('Partidas perdidas por jugador')
    plt.show()
    
Menu_estadistica()
    
    
def Top_cinco():
    
    df = pd.read_excel(r'C:\EjerciciosPython\modulos\Resultados.xlsx')
        
    ganadas = df[df['Resultado'] == 'partida ganada'].groupby('Nombre').size()
    
    
    top_cinco = ganadas.sort_values(ascending=False).head(5)
    print(" Top 5 jugadores con más partidas ganadas:")
    print(top_cinco)

    
    plt.figure(figsize=(6, 6))
    plt.pie(top_cinco, labels=top_cinco.index)
    plt.title('Partidas ganadas - Top 5 jugadores')
         
Menu_estadistica()    
    
def Estadisticas_jugador():
        
    df = pd.read_excel('C:\EjerciciosPython\modulos\Resultados.xlsx')
        
    usuario_elegido = input("Elige el nombre de un jugador para mostrar sus estadisticas:")
    
    jugador_analizado = df[df["Nombre"] == usuario_elegido]
        
        
    if jugador_analizado.empty:
        print  ("Opcion no valida, intentalo de nuevo")
        winsound.PlaySound('C:\Windows\Media\Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
        return
        
    partidas_ganadas_jug = (jugador_analizado['Resultado'] == 'partida ganada').sum()
    partidas_perdidas_jug = (jugador_analizado['Resultado'] == 'partida perdida').sum()
    intentos_jug = (jugador_analizado['Intentos']).sum()    
        
       
    print('Datos del jugador:', usuario_elegido)
    print('Partidas ganadas:', partidas_ganadas_jug)
    print('Partidas perdidas:', partidas_perdidas_jug)
    print('Intentos:', intentos_jug)
            
    plt.figure(figsize=(6, 4))
    plt.bar(["Ganadas", "Perdidas"], [partidas_ganadas_jug, partidas_perdidas_jug], color=['green', 'red'])
    plt.title(f"Partidas de {usuario_elegido}")
    plt.ylabel("Cantidad de partidas")
    plt.show()
    
    break
    

Menu_estadistica()
    
def Menu_ppal():
    
    while True:
        print("***** Bienvenido al Juego Adivina el número *****")
        winsound.PlaySound(r'C:\Windows\Media\Ring 05.wav', winsound.SND_FILENAME)

        try:
            opcion = int(input("*** Menu ***\n"
                               "1. Juego Solitario\n"
                               "2. Juego Dobles\n"
                               "3. Estadística del Juego\n"
                               "4. Salir\n"
                               "Elige una opción:\n"))

            if opcion == 1:
                solitario()  

            elif opcion == 2:
                double_game()  

            elif opcion == 3:
                Menu_estadistica()  

            elif opcion == 4:
                print("Saliendo del juego...")
                return  

            else:
                print("Opción no válida, inténtalo de nuevo.")

        except ValueError:
            print("Error: Ingresa un número válido.")  # Previene errores si el usuario ingresa texto en vez de un número
            
Menu_ppal()    
    


# In[ ]:





# In[ ]:





# In[ ]:




