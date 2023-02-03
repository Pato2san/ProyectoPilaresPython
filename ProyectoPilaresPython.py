"""Imitando funcionamiento de 
https://www.digikey.com/es/resources/conversion-calculators/conversion-calculator-resistor-color-code"""

import tkinter
B1 = 15
B2 = 15
B3 = 15
B4 = 15
Be = 15
Resis = 0
Resistor = 0
ohm = "Ω"
Resistor = 0

"""Mensaje de Bienvenida"""
print(" ")
print(" ")
print("Bienvenidos")
print("Proyecto Python Pilares")
print("ABRAHAM SANCHEZ 426LB010")
print(" ")
print("Codigo de Colores resistencia")
print(" ")
print(" ")


def convertir():
    try:
        banda1 = str(cajaTexto1.get())
        banda2 = str(cajaTexto2.get())
        banda3 = str(cajaTexto3.get())
        banda4 = str(cajaTexto4.get())
        
        """Conversion de banda1"""
        banda1 = banda1.upper()
        if banda1 == "NEGRO":
            B1 = 0
        elif banda1 == "CAFE":
            B1 = 10
        elif banda1 == "ROJO":
            B1 = 20
        elif banda1 == "NARANJA":
            B1 = 30
        elif banda1 == "AMARILLO":
            B1 = 40
        elif banda1 == "VERDE":
            B1 = 50
        elif banda1 == "AZUL":
            B1 = 60
        elif banda1 == "VIOLETA":
            B1 = 70
        elif banda1 == "GRIS":
            B1 = 80
        elif banda1 == "BLANCO":
            B1 = 90
        else:
              B1 = 15
              etiqueta16["text"] = f"Algo salio mal" 

        """Conversion de banda2"""
        banda2 = banda2.upper()
        if banda2 == "NEGRO":
            B2 = 0
        elif banda2 == "CAFE":
            B2 = 1
        elif banda2 == "ROJO":
            B2 = 2
        elif banda2 == "NARANJA":
            B2 = 3
        elif banda2 == "AMARILLO":
            B2 = 4
        elif banda2 == "VERDE":
            B2 = 5
        elif banda2 == "AZUL":
            B2 = 6
        elif banda2 == "VIOLETA":
            B2 = 7
        elif banda2 == "GRIS":
            B2 = 8
        elif banda2 == "BLANCO":
            B2 = 9
        else:
              B2 = 15
              etiqueta16["text"] = f"Algo salio mal" 
        
        """Conversion de banda3"""
        banda3 = banda3.upper()
        if banda3 == "NEGRO":
            B3 = 1
        elif banda3 == "CAFE":
            B3 = 10
        elif banda3 == "ROJO":
            B3 = 100
        elif banda3 == "NARANJA":
            B3 = 1000
        elif banda3 == "AMARILLO":
            B3 = 10000
        elif banda3 == "VERDE":
            B3 = 100000
        elif banda3 == "AZUL":
            B3 = 1000000
        elif banda3 == "VIOLETA":
            B3 = 10000000
        elif banda3 == "GRIS":
            B3 = 100000000
        elif banda3 == "BLANCO":
            B3 = 1000000000
        elif banda3 == "ORO":
            B3 = 0.1
        elif banda3 == "PLATA":
            B3 = 0.01
        else:
              B3 = 15
              etiqueta16["text"] = f"Algo salio mal" 

        """Conversion de banda4"""
        banda4 = banda4.upper()
        if banda4 == "CAFE":
            B4 = 1
        elif banda4 == "ROJO":
            B4 = 2
        elif banda4 == "VERDE":
            B4 = 0.5
        elif banda4 == "AZUL":
            B4 = 0.25
        elif banda4 == "VIOLETA":
            B4 = 0.1
        elif banda4 == "GRIS":
            B4 = 0.05
        elif banda4 == "ORO":
            B4 = 5
        elif banda4 == "PLATA":
            B4 = 10
        else:
              B4 = 15
              etiqueta16["text"] = f"Algo salio mal"
        
        """Deteccion de error"""
        if B1 == Be:
            etiqueta16["text"] = f"Algo salio mal"
        elif B2==Be:
            etiqueta16["text"] = f"Algo salio mal"
        elif B3==Be:
            etiqueta16["text"] = f"Algo salio mal"
        elif B4==Be:
            etiqueta16["text"] = f"Algo salio mal"
        else:
            Resis = (B1 + B2 ) * B3

            """Rutina Giga Mega kilo """
            if Resis >= 1000000000:
                ohm = "GΩ"
                Resistor = Resis/1000000000                
            else:
                if 1000000 <= Resis < 1000000000 :
                    ohm = "MΩ"
                    Resistor = Resis/1000000
                else:
                    if 1000 <= Resis < 1000000 :
                        ohm = "KΩ"
                        Resistor = Resis/1000
                    else:
                        ohm = "Ω"
                        Resistor = Resis
                               
            etiqueta16["text"] = f"La Resistencia es: {Resistor} {ohm} ± {B4}% Tolerancia"        
    except:
        etiqueta16["text"] = f"Algo salio mal"

"""Comienza el bucle de la ventana"""
ventana = tkinter.Tk()
ventana.geometry("300x500")

"""Primera y segunda banda de color"""
etiqueta1 = tkinter.Label(ventana,text="Parametros de la Resistencia")
etiqueta1.pack()
etiqueta2 = tkinter.Label(ventana,text="Introduce el Nombre del Color")
etiqueta2.pack()
etiqueta3 = tkinter.Label(ventana,text="Colores posibles en estas dos bandas:")
etiqueta3.pack()
etiqueta4 = tkinter.Label(ventana,text="NEGRO CAFE ROJO NARANJA AMARILLO")
etiqueta4.pack()
etiqueta5 = tkinter.Label(ventana,text="VERDE AZUL VIOLETA GRIS BLANCO")
etiqueta5.pack()
etiqueta6 = tkinter.Label(ventana,text="1.ª banda de color")
etiqueta6.pack()
cajaTexto1 = tkinter.Entry(ventana)
cajaTexto1.pack()
etiqueta7 = tkinter.Label(ventana,text="2.ª banda de color")
etiqueta7.pack()
cajaTexto2 = tkinter.Entry(ventana)
cajaTexto2.pack()

"""Tercera banda de color"""
etiqueta8 = tkinter.Label(ventana,text="Colores posibles en esta banda 3")
etiqueta8.pack()
etiqueta9 = tkinter.Label(ventana,text="NEGRO CAFE ROJO NARANJA AMARILLO VERDE")
etiqueta9.pack()
etiqueta10 = tkinter.Label(ventana,text="AZUL VIOLETA GRIS BLANCO ORO PLATA")
etiqueta10.pack()
etiqueta11 = tkinter.Label(ventana,text="3.ª banda de color/Multiplicador")
etiqueta11.pack()
cajaTexto3 = tkinter.Entry(ventana)
cajaTexto3.pack()

"""Cuarta banda de color"""
etiqueta12 = tkinter.Label(ventana,text="Colores posibles en esta banda 4")
etiqueta12.pack()
etiqueta13 = tkinter.Label(ventana,text="CAFE ROJO VERDE AZUL")
etiqueta13.pack()
etiqueta14 = tkinter.Label(ventana,text="VIOLETA GRIS ORO PLATA")
etiqueta14.pack()
etiqueta15 = tkinter.Label(ventana,text="Ingrese el cuarto color / Tolerancia:")
etiqueta15.pack()
cajaTexto4 = tkinter.Entry(ventana)
cajaTexto4.pack()

"""Rutina Conversion colores a numeros"""
boton1 = tkinter.Button(ventana,text="Valor de la Resistencia",command=convertir)
boton1.pack()
etiqueta16 = tkinter.Label(ventana)
etiqueta16.pack()

ventana.mainloop()
"""FIN :("""