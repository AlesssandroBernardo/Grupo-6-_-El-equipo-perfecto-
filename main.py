import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from tkinter import ttk


dataset = pd.read_csv('Dataset_Complejidad_Algoritmica.csv')
pd.set_option('display.max_columns', None)  # Para mostrar todas las columnas
dataset = pd.read_csv('Dataset_Complejidad_Algoritmica.csv')
pd.set_option('display.max_columns', None)  # Para mostrar todas las columnas

def nombreJugador(id_jugador):
    df = pd.read_csv('dataset.csv', header=0)

    for i in range (0,20):
        if id_jugador == int(df.iloc[i, 0].split(';')[0]):
            print(df.iloc[i, 0].split(';')[1])
            return df.iloc[i, 0].split(';')[1]
def IDJugador(nombre_jugador):
    df = pd.read_csv('dataset.csv', header=0)

    for i in range (0,20):
        if nombre_jugador == str(df.iloc[i, 0].split(';')[1]):
            return df.iloc[i, 0].split(';')[0]
        
def lista_442():
    jugadores = []
    for id_jugador in delanteros[:4]:
        nombre = nombreJugador(int(id_jugador))
        jugadores.append(nombre)

    for id_jugador in centrocampistas[:4]:
        nombre = nombreJugador(int(id_jugador))
        jugadores.append(nombre)

    for id_jugador in defensas[:2]:
        nombre = nombreJugador(int(id_jugador))
        jugadores.append(nombre)

    for id_jugador in porteros[:1]:
        nombre = nombreJugador(int(id_jugador))
        jugadores.append(nombre)
    ventana_lista = tk.Toplevel(ventana)
    ventana_lista.title("Lista del equipo perfecto 4-4-2")
# Crear etiquetas para mostrar los nombres de los jugadores
    etiqueta_delanteros = tk.Label(ventana_lista, text="Delanteros:")
    etiqueta_centrocampistas = tk.Label(ventana_lista, text="Centrocampistas:")
    etiqueta_defensas = tk.Label(ventana_lista, text="Defensas:")
    etiqueta_porteros = tk.Label(ventana_lista, text="Porteros:")

# Posicionar las etiquetas en la ventana
    etiqueta_delanteros.pack()

# Mostrar los nombres de los jugadores en las etiquetas
    for id_jugador in delanteros[:4]:
        nombre = nombreJugador(int(id_jugador))
        etiqueta = tk.Label(ventana_lista, text=nombre)
        etiqueta.pack()
    etiqueta_centrocampistas.pack()

    for id_jugador in centrocampistas[:4]:
        nombre = nombreJugador(int(id_jugador))
        etiqueta = tk.Label(ventana_lista, text=nombre)
        etiqueta.pack()
    etiqueta_defensas.pack()

    for id_jugador in defensas[:2]:
        nombre = nombreJugador(int(id_jugador))
        etiqueta = tk.Label(ventana_lista, text=nombre)
        etiqueta.pack()
    etiqueta_porteros.pack()
    for id_jugador in porteros[:1]:
        nombre = nombreJugador(int(id_jugador))
        etiqueta = tk.Label(ventana_lista, text=nombre)
        etiqueta.pack()
    combo_jugadores = ttk.Combobox(ventana_lista, values=jugadores)
    combo_jugadores.pack()
    def lesionar_jugador():
        jugador_seleccionado = str(combo_jugadores.get())
        
        if IDJugador(jugador_seleccionado):
            # Eliminar el jugador de la lista correspondiente
            if IDJugador(jugador_seleccionado) in delanteros:
                delanteros.remove(IDJugador(jugador_seleccionado))
            elif IDJugador(jugador_seleccionado) in centrocampistas:
                centrocampistas.remove(IDJugador(jugador_seleccionado))
            elif IDJugador(jugador_seleccionado) in defensas:
                defensas.remove(IDJugador(jugador_seleccionado))
            elif IDJugador(jugador_seleccionado) in porteros:
                porteros.remove(IDJugador(jugador_seleccionado))

        ventana_lista.destroy()  # Cerrar la ventana actual
        lista_442()
    boton_lesionar = tk.Button(ventana_lista, text="Lesionar", command=lesionar_jugador)
    boton_lesionar.pack()

ventana = tk.Tk()
ventana.geometry("800x500")
ventana.title("App")
def dibujar_form1(ventana,a,b,c):
    lienzo = tk.Canvas(ventana, width=1000, height=800)
    lienzo.pack()
    imagen = tk.PhotoImage(file="campo_futbol.gif")
    lienzo.create_image(350, 200, image=imagen)
    lienzo.create_oval(200 - 10, 85 - 10, 200 + 10, 85 + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 160 - 10, 200 + 10, 160 + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 235 - 10, 200 + 10, 235 + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 310 - 10, 200 + 10, 310 + 10, outline='black', fill='blue')
    add=0;
    for elemento in defensas:
        lienzo.create_text(205, 105 + add, text=str(elemento))
        add += 75;


    lienzo.create_oval(340 - 10, 85  - 10, 340 + 10, 85  + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 160 - 10, 340 + 10, 160 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 235 - 10, 340 + 10, 235 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 310 - 10, 340 + 10, 310 + 10, outline='black', fill='blue')
    add=0;
    for elemento in centrocampistas:
        lienzo.create_text(345, 105 + add, text=str(elemento))
        add += 75;


    lienzo.create_oval(450 - 10, 150 - 10, 450 + 10, 150 + 10, outline='black', fill='blue')
    lienzo.create_oval(450 - 10, 250 - 10, 450 + 10, 250 + 10, outline='black', fill='blue')
    add=0;
    for elemento in delanteros[:c]:
        lienzo.create_text(460, 165 + add, text=str(elemento))
        add += 100;

    ventana.mainloop()
def dibujar_form2(ventana,a,b,c):
    lienzo = tk.Canvas(ventana, width=1000, height=800)
    lienzo.pack()
    imagen = tk.PhotoImage(file="campo_futbol.gif")
    lienzo.create_image(350, 200, image=imagen)
    lienzo.create_oval(200 - 10, 85  - 10, 200 + 10, 85  + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 160 - 10, 200 + 10, 160 + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 235 - 10, 200 + 10, 235 + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 310 - 10, 200 + 10, 310 + 10, outline='black', fill='blue')
    add=0;
    for elemento in defensas[:a]:
        lienzo.create_text(200, 110 + add, text=str(elemento))
        add += 75;

    lienzo.create_oval(340 - 10, 125 - 10, 340 + 10, 125 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 200 - 10, 340 + 10, 200 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 275 - 10, 340 + 10, 275 + 10, outline='black', fill='blue')
    add=0;
    for elemento in centrocampistas[:b]:
        lienzo.create_text(340, 145 + add, text=str(elemento))
        add += 75;



    lienzo.create_oval(450 - 10, 125 - 10, 450 + 10, 125 + 10, outline='black', fill='blue')
    lienzo.create_oval(450 - 10, 200 - 10, 450 + 10, 200 + 10, outline='black', fill='blue')
    lienzo.create_oval(450 - 10, 275 - 10, 450 + 10, 275 + 10, outline='black', fill='blue')
    add=0;
    for elemento in delanteros[:c]:
        lienzo.create_text(450, 145 + add, text=str(elemento))
        add += 75;


    ventana.mainloop()
#3-5-2
def dibujar_form3(ventana,a,b,c):
    lienzo = tk.Canvas(ventana, width=1000, height=800)
    lienzo.pack()
    imagen = tk.PhotoImage(file="campo_futbol.gif")
    lienzo.create_image(350, 200, image=imagen)
    lienzo.create_oval(200 - 10, 100  - 10, 200 + 10,100  + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 175 - 10, 200 + 10, 175 + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 250 - 10, 200 + 10, 250 + 10, outline='black', fill='blue')
    add=0;
    for elemento in defensas[:a]:
        lienzo.create_text(205, 125 + add, text=str(elemento))
        add += 75;


    lienzo.create_oval(340 - 10, 80 - 10, 340 + 10,  80 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 140 - 10, 340 + 10, 140 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 200 - 10, 340 + 10, 200 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 260 - 10, 340 + 10, 260 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 320 - 10, 340 + 10, 320 + 10, outline='black', fill='blue')
    add=0;
    for elemento in centrocampistas[:b]:
        lienzo.create_text(340, 100 + add, text=str(elemento))
        add += 60;


    lienzo.create_oval(450 - 10, 150 - 10, 450 + 10, 150 + 10, outline='black', fill='blue')
    lienzo.create_oval(450 - 10, 250 - 10, 450 + 10, 250 + 10, outline='black', fill='blue')
    add = 0;
    for elemento in delanteros[:c]:
        lienzo.create_text(450, 175 + add, text=str(elemento))
        add += 100;


    ventana.mainloop()
#4-5-1
def dibujar_form4(ventana,a,b,c):
    lienzo = tk.Canvas(ventana, width=1000, height=800)
    lienzo.pack()
    imagen = tk.PhotoImage(file="campo_futbol.gif")
    lienzo.create_image(350, 200, image=imagen)
    lienzo.create_oval(200 - 10, 85  - 10, 200 + 10, 85  + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 160 - 10, 200 + 10, 160 + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 235 - 10, 200 + 10, 235 + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 310 - 10, 200 + 10, 310 + 10, outline='black', fill='blue')
    add=0;
    for elemento in defensas[:a]:
        lienzo.create_text(205, 105 + add, text=str(elemento))
        add += 75;




    lienzo.create_oval(340 - 10, 80 - 10, 340 + 10,  80 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 140 - 10, 340 + 10, 140 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 200 - 10, 340 + 10, 200 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 260 - 10, 340 + 10, 260 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 320 - 10, 340 + 10, 320 + 10, outline='black', fill='blue')
    add=0;
    for elemento in centrocampistas[:b]:
        lienzo.create_text(340, 105 + add, text=str(elemento))
        add += 60;


    lienzo.create_oval(450 - 10, 200 - 10, 450 + 10, 200 + 10, outline='black', fill='blue')
    add=0;
    for elemento in delanteros[:c]:
        lienzo.create_text(450, 220 + add, text=str(elemento))
        add += 75;

    ventana.mainloop()
def dibujar_form5(ventana,a,b,c):
    lienzo = tk.Canvas(ventana, width=1000, height=800)
    lienzo.pack()
    imagen = tk.PhotoImage(file="campo_futbol.gif")
    lienzo.create_image(350, 200, image=imagen)
    lienzo.create_oval(200 - 10, 80  - 10, 200 + 10,  80  + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 140 - 10, 200 + 10,  140 + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 200 - 10, 200 + 10,  200 + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 260 - 10, 200 + 10,  260 + 10, outline='black', fill='blue')
    lienzo.create_oval(200 - 10, 320 - 10, 200 + 10,  320 + 10, outline='black', fill='blue')
    add=0;
    for elemento in defensas[:a]:
        lienzo.create_text(205, 105 + add, text=str(elemento))
        add += 60;



    lienzo.create_oval(340 - 10, 125 - 10, 340 + 10, 125 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 200 - 10, 340 + 10, 200 + 10, outline='black', fill='blue')
    lienzo.create_oval(340 - 10, 275 - 10, 340 + 10, 275 + 10, outline='black', fill='blue')
    add=0;
    for elemento in centrocampistas[:b]:
        lienzo.create_text(345, 150+add, text=str(elemento))
        add+=75;




    lienzo.create_oval(450 - 10, 150 - 10, 450 + 10, 150 + 10, outline='black', fill='blue')
    lienzo.create_oval(450 - 10, 250 - 10, 450 + 10, 250 + 10, outline='black', fill='blue')
    add=0;
    for elemento in centrocampistas[:c]:
        lienzo.create_text(455, 175+add, text=str(elemento))
        add+=100;
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
        boton2 = tk.Button(form1,text="Ver lista",command=lista_442)        
        boton.pack()
        boton2.pack()
        dibujar_form1(form1,4,4,2)

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
        dibujar_form2(form2,4,4,3)

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
        dibujar_form3(form3,3,5,2)

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
        dibujar_form4(form4,4,5,1)

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
        dibujar_form5(form5,5,3,2)
    else:
        messagebox.showinfo("Mensaje", "Elige una opción")

centrocampistas =[]
defensas=[]
delanteros=[]
porteros=[]


diccionario = {
    'CC': 'red',  
    'CCDF': 'red',  
    'CCDL': 'red',  
    'DF': 'blue',   
    'DFCC': 'red',
    'DLDF': 'red',  
    'PO': 'yellow',  
    'DL': 'green',  
    'DLCC': 'yellow'  
}

def agregar_arista(G, df, node1, node2,indice=None,peso=None):
    if indice is None:
        indice = agregar_arista.counter
    else:
        agregar_arista.counter=indice
    if peso is None:
        peso = 100 - int(df.iloc[indice, 0].split(';')[11])
    G.add_edge(node1, node2, weight=peso)
    agregar_arista.counter += 1

# Inicializar el contador en 0
agregar_arista.counter = 0
    

# Inicializar el contador en 0
def MostrarGrafo():
    G = nx.Graph()

    df = pd.read_csv('dataset.csv', header=0)
    for i in range(0, 20):
        node_name = df.iloc[i, 0].split(';')[0]
        color = diccionario[df.iloc[i, 0].split(';')[2]]
        G.add_node(node_name, color=color)

    print(100-int(df.iloc[3,0].split(';')[11]))
    agregar_arista(G,df,'14','732')
    agregar_arista(G,df,'71','732')
    agregar_arista(G,df,'77','732')
    agregar_arista(G,df,'732','507')
    agregar_arista(G,df,'1752','2236',indice=5)
    agregar_arista(G,df,'2236','1661')
    agregar_arista(G,df,'1661','1451')
    agregar_arista(G,df,'176','1451')
    agregar_arista(G,df,'2481','126',indice=10)
    agregar_arista(G,df,'126','1101')
    agregar_arista(G,df,'1274','1101')
    agregar_arista(G,df,'1101','1703')
    agregar_arista(G,df,'468','2454',indice=15)
    agregar_arista(G,df,'2118','2454')
    agregar_arista(G,df,'1521','2454')
    agregar_arista(G,df,'2505','2454')

    #los mejores se unen
    agregar_arista(G,df,'507','1451',peso=0)
    agregar_arista(G,df,'1451','1703',peso=0)
    agregar_arista(G,df,'1703','1451',peso=0)
    agregar_arista(G,df,'507','2454',peso=0)
    agregar_arista(G,df,'2454','1703',peso=0)

    nodos_por_color = {}
    for nodo, atributos in G.nodes(data=True):
        color = atributos['color']
        if color in nodos_por_color:
            nodos_por_color[color].append(nodo)
        else:
            nodos_por_color[color] = [nodo]

    aristas_ordenadas = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    arbol_minimo = nx.Graph()
    nodos_contados = {color: 0 for color in nodos_por_color}
    nodos_recorridos = []

    for u, v, datos in aristas_ordenadas:
        color_u = G.nodes[u]['color']
        color_v = G.nodes[v]['color']
    
        if nodos_contados[color_u] < 5 and nodos_contados[color_v] < 5:
            if u not in nodos_recorridos:
                nodos_recorridos.append(u)
                nodos_contados[color_u] += 1
        
        if v not in nodos_recorridos:
            nodos_recorridos.append(v)
            nodos_contados[color_v] += 1
    
        if all(count >= 5 for count in nodos_contados.values()):
            break

# Imprimir los nodos agrupados por color
    for color, nodos in nodos_por_color.items():
        print(color + ":")
        for nodo in nodos:
            if nodo in nodos_recorridos:
                print(nodo)
                if color== 'red':
                    centrocampistas.append(nodo)
                if color=='blue':
                    defensas.append(nodo)
                if color=='yellow':
                    porteros.append(nodo)
                if color =='green':
                    delanteros.append(nodo)
    delanteros.reverse()
    defensas.reverse()
    porteros.reverse()
    centrocampistas.reverse()
    print(delanteros,defensas,porteros,centrocampistas)

# Dibujar el grafo
    pos = nx.circular_layout(G)  # Posiciones de los nodos

# Crear una lista de colores para los nodos
    node_colors = [G.nodes[node]['color'] for node in G.nodes]

    nx.draw(G, pos, with_labels=True, node_size=200, node_color=node_colors, font_weight='bold')

# Dibujar los pesos de las aristas
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)


    texto_porteros="\n".join(porteros)
    texto_defensas="\n".join(defensas)
    texto_centrocampistas="\n".join(centrocampistas)
    texto_delanteros="\n".join(delanteros)


    MostrarBestPlayers(texto_porteros,texto_defensas,texto_centrocampistas,texto_delanteros)



# Mostrar el gráfico
    plt.show()



def MostrarBestPlayers(texto_porteros,texto_defensas,texto_centrocampistas,texto_delanteros):
    FormBest=tk.Toplevel()
    FormBest.title("Best Players")
    FormBest.geometry("1400x500")

    TitlePortero = tk.Label(FormBest, text="Mejores Porteros", font=("Arial", 15, "bold"), fg="Black")
    TitlePortero.place(x=100, y=30)
    label_valores = tk.Label(FormBest, text=texto_porteros, font=("Arial", 12), fg="black")
    label_valores.place(x=100, y=200)



    TitleDefensa = tk.Label(FormBest, text="Mejores Defensas",font=("Arial", 15, "bold"), fg="Black")
    TitleDefensa.place(x=400,y=30)
    label_valores = tk.Label(FormBest, text=texto_defensas, font=("Arial",12), fg="black")
    label_valores.place(x=400, y=200)



    TitleMediocampista = tk.Label(FormBest, text="Mejores Mediocampistas", font=("Arial", 15, "bold"), fg="Black")
    TitleMediocampista.place(x=700, y=30)
    label_valores = tk.Label(FormBest, text=texto_centrocampistas, font=("Arial", 12), fg="black")
    label_valores.place(x=700, y=200)




    TitleDelantero = tk.Label(FormBest, text="Mejores Delanteros", font=("Arial", 15, "bold"), fg="Black")
    TitleDelantero.place(x=1000, y=30)
    label_valores = tk.Label(FormBest, text=texto_delanteros, font=("Arial", 12), fg="black")
    label_valores.place(x=1000, y=200)
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
botonGrafo = tk.Button(ventana, text="Mostrar Grafo ", command=MostrarGrafo)

botonLigas.place(x=9,y=30)
botonGrafo.place(x=700,y=30)


cancha = tk.PhotoImage(file="campo_futbol.gif")
Imgcancha = tk.Label(ventana, image=cancha)
Imgcancha.pack()
ventana.mainloop()
