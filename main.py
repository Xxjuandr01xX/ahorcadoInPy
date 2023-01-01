## Juego del ahorcado en python

from tkinter import *
from random import randint
from tkinter import messagebox
vidas = 7
letrasAcertadas = 0

letras_usar = []

## funciones
def colocarLetras():
    x=50
    y=155
    contador=0
    Label(game, text="Letras sin Usar ").place(x=50, y=100)
    for i in range(26):
        contador+=1
        letrasLabel[i].place(x=x, y=y)
        x+=30
        if contador == 5:
            y+=40
            contador=0
            x=50
        
def test():
    global vidas
    global letrasAcertadas
    letras_usar.append(letraE.get())
    ##print(letras_usar)
    letrasLabel[ord(letraE.get())-97].config(text="")
    if letraE.get() in palabra:
        if palabra.count(letraE.get()) > 1:
            letrasAcertadas+=palabra.count(letraE.get())
            for i in range(len(palabra)):
                if palabra[i]==letraE.get():
                   guiones[i].config(text=""+letraE.get())
        else:
            letrasAcertadas+=1
            guiones[palabra.index(letraE.get())].config(text=""+letraE.get())
        if letrasAcertadas == len(palabra):
            messagebox.showwarning(title="VICTORIA",message="Felicitaciones has ganado la partida.")
    else:
        vidas-=1
        if vidas == 0:
            messagebox.showwarning(title="DERROTA", message="Se te han acabado las vidas.")
## UI
archivo = open("palabras.txt", "r")
conjuntoPalabras = list(archivo.read().split("\n"))
palabra = conjuntoPalabras[randint(0, len(conjuntoPalabras)-1)].lower()

raiz = Tk()
letraE = StringVar()

raiz.config(width=1000, height=100, bg="blue", relief="groove", bd=10)
game = Frame(raiz)
game.config(width=1000, height=600, relief="sunken", bd=15)
game.grid_propagate(False)
game.pack()

##inputs
Label(game, text="Introduce una letra: ", font=("verdana", 24)).grid(row=0, column=0, pady=10, padx=10)
letra = Entry(game, width=2, font=("verdana", 24), textvariable=letraE).grid(row=0, column=1, padx=10, pady=10)
btn_probar_letra = Button(game, text="Probar", bg="yellow", command=test).grid(row=1, column=0, padx=10, pady=10)

letrasLabel = [Label(game, text=chr(j+97), font=("verdana", 20)) for j in range(26)]
colocarLetras()

guiones = [Label(game, text="_", font=("verdana", 30)) for _ in palabra]
inicial=200
for i in range(len(palabra)):
    guiones[i].place(x=inicial, y=400)
    inicial+=50

raiz.mainloop()
 