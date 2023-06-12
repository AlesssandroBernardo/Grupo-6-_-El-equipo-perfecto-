import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

import pandas as pd

dataset = pd.read_csv('Dataset_Complejidad_Algoritmica.csv')
pd.set_option('display.max_columns', None)  # Para mostrar todas las columnas

ventana = tk.Tk()
ventana.geometry("800x500")
ventana.title("App")
def dibujar_form1(ventana):
    lienzo = tk.Canvas(ventana, width=1000, height=800)
    lienzo.pack()
    imagen = tk.PhotoImage(file="campo_futbol.gif")
    lienzo.create_image(350, 200, image=imagen)
    lienzo.create_oval(200 - 10, 100 - 10, 200 + 10, 100 + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 150 - 10, 200 + 10, 150 + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 250 - 10, 200 + 10, 250 + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 300 - 10, 200 + 10, 300 + 10, outline='black', fill='blue')

    lienzo.create_oval(340 - 10, 100 - 10, 340 + 10, 100 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 150 - 10, 340 + 10, 150 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 250 - 10, 340 + 10, 250 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 300 - 10, 340 + 10, 300 + 10, outline='black', fill='blue')

    lienzo.create_oval(450 - 10, 150 - 10, 450 + 10, 150 + 10, outline='black', fill='blue')
    lienzo.create_oval(450 - 10, 250 - 10, 450 + 10, 250 + 10, outline='black', fill='blue')

    ventana.mainloop()

def dibujar_form2(ventana):
    lienzo = tk.Canvas(ventana, width=1000, height=800)
    lienzo.pack()
    imagen = tk.PhotoImage(file="campo_futbol.gif")
    lienzo.create_image(350, 200, image=imagen)
    lienzo.create_oval(200 - 10, 100 - 10, 200 + 10, 100 + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 150 - 10, 200 + 10, 150 + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 250 - 10, 200 + 10, 250 + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 300 - 10, 200 + 10, 300 + 10, outline='black', fill='blue')

    lienzo.create_oval(340 - 10, 125 - 10, 340 + 10, 125 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 200 - 10, 340 + 10, 200 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 275 - 10, 340 + 10, 275 + 10, outline='black', fill='blue')

    lienzo.create_oval(450 - 10, 125 - 10, 450 + 10, 125 + 10, outline='black', fill='blue')
    lienzo.create_oval(450 - 10, 200 - 10, 450 + 10, 200 + 10, outline='black', fill='blue')
    lienzo.create_oval(450 - 10, 275 - 10, 450 + 10, 275 + 10, outline='black', fill='blue')

    ventana.mainloop()


#3-5-2
def dibujar_form3(ventana):
    lienzo = tk.Canvas(ventana, width=1000, height=800)
    lienzo.pack()
    imagen = tk.PhotoImage(file="campo_futbol.gif")
    lienzo.create_image(350, 200, image=imagen)
    lienzo.create_oval(200 - 10, 125 - 10, 200 + 10, 125 + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 200 - 10, 200 + 10, 200 + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 275 - 10, 200 + 10, 275 + 10, outline='black', fill='blue')

    lienzo.create_oval(340 - 10, 75 - 10, 340 + 10,  75 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 125 - 10, 340 + 10, 125 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 200 - 10, 340 + 10, 200 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 275 - 10, 340 + 10, 275 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 325 - 10, 340 + 10, 325 + 10, outline='black', fill='blue')

    lienzo.create_oval(450 - 10, 150 - 10, 450 + 10, 150 + 10, outline='black', fill='blue')
    lienzo.create_oval(450 - 10, 250 - 10, 450 + 10, 250 + 10, outline='black', fill='blue')

    ventana.mainloop()

#4-5-1
def dibujar_form4(ventana):
    lienzo = tk.Canvas(ventana, width=1000, height=800)
    lienzo.pack()
    imagen = tk.PhotoImage(file="campo_futbol.gif")
    lienzo.create_image(350, 200, image=imagen)
    lienzo.create_oval(200 - 10, 100 - 10, 200 + 10, 100 + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 150 - 10, 200 + 10, 150 + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 250 - 10, 200 + 10, 250 + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 300 - 10, 200 + 10, 300 + 10, outline='black', fill='blue')

    lienzo.create_oval(340 - 10, 75 - 10, 340 + 10,  75 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 125 - 10, 340 + 10, 125 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 200 - 10, 340 + 10, 200 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 275 - 10, 340 + 10, 275 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 325 - 10, 340 + 10, 325 + 10, outline='black', fill='blue')

    lienzo.create_oval(450 - 10, 200 - 10, 450 + 10, 200 + 10, outline='black', fill='blue')

    ventana.mainloop()

def dibujar_form5(ventana):
    lienzo = tk.Canvas(ventana, width=1000, height=800)
    lienzo.pack()
    imagen = tk.PhotoImage(file="campo_futbol.gif")
    lienzo.create_image(350, 200, image=imagen)
    lienzo.create_oval(200 - 10, 75  - 10, 200 + 10,  75  + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 125 - 10, 200 + 10,  125 + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 200 - 10, 200 + 10,  200 + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 275 - 10, 200 + 10,  275 + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 325 - 10, 200 + 10,  325 + 10, outline='black', fill='blue')

    lienzo.create_oval(340 - 10, 125 - 10, 340 + 10, 125 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 200 - 10, 340 + 10, 200 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 275 - 10, 340 + 10, 275 + 10, outline='black', fill='blue')

    lienzo.create_oval(450 - 10, 150 - 10, 450 + 10, 150 + 10, outline='black', fill='blue')
    lienzo.create_oval(450 - 10, 250 - 10, 450 + 10, 250 + 10, outline='black', fill='blue')

    ventana.mainloop()




def formacion1():
    if var.get() == "4-4-2":
        form1 = tk.Toplevel()
        form1.geometry("1000x500")
        form1.title("Formacion 1")

        def cerrar_ventana():
            form1.destroy()

        cancha = tk.PhotoImage(file="campo_futbol.gif")
        Imgcancha = tk.Label(form1, text="Hola", image=cancha)
        boton = tk.Button(form1,text="Cerrar Ventana",command=cerrar_ventana)
        boton.pack()
        dibujar_form1(form1)

    elif var.get() == "4-3-3":
        form2 = tk.Toplevel()
        form2.geometry("1000x500")
        form2.title("Formacion 2")
        def cerrar_ventana():
            form2.destroy()

        boton = tk.Button(form2, text="Cerrar Ventana", command=cerrar_ventana)
        boton.pack()
        cancha = tk.PhotoImage(file="campo_futbol.gif")
        Imgcancha = tk.Label(form2, text="Hola", image=cancha)
        dibujar_form2(form2)

    elif var.get() == "3-5-2":
        form3 = tk.Toplevel()
        form3.geometry("1000x500")
        form3.title("Formacion 3")
        def cerrar_ventana():
            form3.destroy()

        boton = tk.Button(form3, text="Cerrar Ventana", command=cerrar_ventana)
        boton.pack()
        cancha = tk.PhotoImage(file="campo_futbol.gif")
        Imgcancha = tk.Label(form3, text="Hola", image=cancha)
        dibujar_form3(form3)

    elif var.get() == "4-5-1":
        form4 = tk.Toplevel()
        form4.title("Formacion 4")
        form4.geometry("1000x500")
        def cerrar_ventana():
            form4.destroy()

        boton = tk.Button(form4, text="Cerrar Ventana", command=cerrar_ventana)
        boton.pack()
        cancha = tk.PhotoImage(file="campo_futbol.gif")
        Imgcancha = tk.Label(form4, text="Hola", image=cancha)
        dibujar_form4(form4)

    elif var.get() == "5-3-2":
        form5 = tk.Toplevel()
        form5.title("Formacion 5")
        form5.geometry("1000x500")

        def cerrar_ventana():
            form5.destroy()
        boton = tk.Button(form5, text="Cerrar Ventana", command=cerrar_ventana)
        boton.pack()
        cancha = tk.PhotoImage(file="campo_futbol.gif")
        Imgcancha = tk.Label(form5, text="Hola", image=cancha)
        dibujar_form5(form5)
    else:
        messagebox.showinfo("Mensaje", "Elige una opción")

def Mostrarligas():
    FormLigas = tk.Toplevel()
    FormLigas.title("Ligas Europeas")
    FormLigas.geometry("1500x500")
    LigaEspañola = "LaLiga Española"
    LigaFrancesa="Liga 1 Francesa"
    LigaBundesliga=" Bundesliga"
    LigaItaliana="Serie A"
    LigaPremier="Premier League"

    #LigaEspañola
    etiquetaEspañola = tk.Label(FormLigas, text=LigaEspañola,font=("Arial", 18, "bold"), fg="Black")
    etiquetaEspañola.place(x=10,y=30)

    imagen = Image.open("assets/LigaEspañola.png")
    imagen_redimensionada =imagen.resize((180, 180))
    imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
    etiqueta_imagen = tk.Label(FormLigas, image=imagen_tk)
    etiqueta_imagen.place(x=10,y=75)
    InfoLiga="La Liga española, también\n " \
             "como LaLiga o LaLiga\n " \
             "Santander, es la máxima\n" \
             "categoría del fútbol\n " \
             "profesional en España.\n"
    LabelInfoligaEspañola = tk.Label(FormLigas, text=InfoLiga, font=("Arial", 10,"bold"), fg="Black")
    LabelInfoligaEspañola.place(x=10, y=300)





    #LigaFrancesa
    etiquetaLigaFrancesa = tk.Label(FormLigas, text=LigaFrancesa,font=("Arial", 18, "bold"), fg="Black")
    etiquetaLigaFrancesa.place(x=350,y=30)
    imagen2 = Image.open("assets/Ligue1.png")
    imagen_redimensionada2 =imagen2.resize((180, 180))
    imagen_tk2 = ImageTk.PhotoImage(imagen_redimensionada2)
    etiqueta_imagen2 = tk.Label(FormLigas, image=imagen_tk2)
    etiqueta_imagen2.place(x=350,y=75)
    InfoLigaFrancia="La Ligue 1, también conocida\n" \
                    "como la Liga Francesa, es la\n" \
                    "máxima categoría del fútbol\n" \
                    "profesional en Francia.\n"
    LabelInfoligaFrancia = tk.Label(FormLigas, text=InfoLigaFrancia, font=("Arial", 10,"bold"), fg="Black")
    LabelInfoligaFrancia.place(x=350, y=300)


    #Bundesliga
    etiquetaLigaBundesliga = tk.Label(FormLigas, text=LigaBundesliga,font=("Arial", 18, "bold"), fg="Black")
    etiquetaLigaBundesliga.place(x=659,y=30)
    imagen3 = Image.open("assets/Bundesliga.png")
    imagen_redimensionada3 = imagen3.resize((160, 180))
    imagen_tk3 = ImageTk.PhotoImage(imagen_redimensionada3)
    etiqueta_imagen3 = tk.Label(FormLigas, image=imagen_tk3)
    etiqueta_imagen3.place(x=659, y=75)
    InfoLigaBundesLiga="La Bundesliga es la máxima categoría\n" \
                       "del fútbol profesional en Alemania\n" \
                       "y una de las ligas más importantes\n" \
                       "de Europa.Ademas,es conocida por su\n" \
                       "ambiente apasionado en los estadios,\n" \
                       "su enfoque en el desarrollo de jóvenes\n" \
                       "talentos y su estilo de juego ofensivo\n" \
                       "y atractivo."
    LabelInfoligaBundesLiga = tk.Label(FormLigas, text=InfoLigaBundesLiga, font=("Arial", 10,"bold"), fg="Black")
    LabelInfoligaBundesLiga.place(x=600, y=300)




    #SerieA
    etiquetaLigaItaliana = tk.Label(FormLigas, text=LigaItaliana,font=("Arial", 18, "bold"), fg="Black")
    etiquetaLigaItaliana.place(x=960,y=30)

    imagen4 = Image.open("assets/SerieA.jpg")
    imagen_redimensionada4 = imagen4.resize((140, 180))
    imagen_tk4 = ImageTk.PhotoImage(imagen_redimensionada4)
    etiqueta_imagen4 = tk.Label(FormLigas, image=imagen_tk4)
    etiqueta_imagen4.place(x=960, y=75)
    InfoSerieA="La Serie A es la máxima categoría\n" \
               "del fútbol profesional en Italia.Ademas,\n" \
               "La Serie A es conocida por su enfoque\n" \
               " táctico, defensivo y por su énfasis\n" \
               " en la disciplina táctica.\n"
    LabelInfoSerieA = tk.Label(FormLigas, text=InfoSerieA, font=("Arial", 10,"bold"), fg="Black")
    LabelInfoSerieA.place(x=900, y=300)



    #Premierleague
    etiquetaLigaPremier = tk.Label(FormLigas, text=LigaPremier,font=("Arial", 18, "bold"), fg="Black")
    etiquetaLigaPremier.place(x=1200,y=30)

    imagen5 = Image.open("assets/PremierLeague.jpg")
    imagen_redimensionada5 =imagen5.resize((180, 180))
    imagen_tk5 = ImageTk.PhotoImage(imagen_redimensionada5)
    etiqueta_imagen5 = tk.Label(FormLigas, image=imagen_tk5)
    etiqueta_imagen5.place(x=1200,y=75)
    InfoPremierLeague="La Premier League es la máxima categoría\n" \
                      "del fútbol profesional en Inglaterra.\n" \
                      "La Premier League se caracteriza\n" \
                      "por su ritmo rápido, juego físico\n" \
                      "y altos niveles de competencia.\n" \
                      "Es conocida por su atmósfera vibrante\n" \
                      "en los estadios y por contar con algunos\n" \
                      "de los mejores jugadores y\n" \
                      "entrenadores del mundo.\n"
    LabelInfoPremierLeague = tk.Label(FormLigas, text=InfoPremierLeague, font=("Arial", 10,"bold"), fg="Black")
    LabelInfoPremierLeague.place(x=1200, y=300)
    FormLigas.mainloop()

etiqueta = tk.Label(ventana, text="El equipo ideal", bg="green")
etiqueta.pack(fill=tk.X)

var = tk.StringVar(ventana)
var.set("Elige una Alineacion")
lista_desplegable = tk.OptionMenu(ventana, var, "4-4-2", "4-3-3", "3-5-2","4-5-1","5-3-2")
lista_desplegable.pack()
boton = tk.Button(ventana, text="Mostrar formacion", command=formacion1)
boton.pack()

botonLigas = tk.Button(ventana, text="Mostrar Ligas ", command=Mostrarligas)
botonLigas.place(x=9,y=30)

cancha = tk.PhotoImage(file="campo_futbol.gif")
Imgcancha = tk.Label(ventana, image=cancha)
Imgcancha.pack()
ventana.mainloop()