
from tkinter import *
import tkinter as ttk
from base_n_to_decimal import *
from decimal_to_base_n import *

def iniciarcon():
    res = convertobase(converto10(numero.get(), int(base.get())),int(baseconver.get()))
    resultado.set(res)
    pass


raiz =ttk.Tk()
raiz.title("Convertidor de bases");
raiz.geometry("800x180")
wx=800;
wy=600;

miframe = ttk.Frame(raiz, width=(wx), height=(wy))
miframe.config(bg="#01DFA5")
Titulo = Label(miframe, text="Convertidor de Base")
Titulo.grid(row=0, columnspan=6, padx=5, pady=10)

lblnumero = ttk.Label(miframe, text="Ingrese un numero")
lblnumero.grid(row=1,column=0,sticky="w",padx=5, pady=10)

lblbase = ttk.Label(miframe, text="Ingrese base")
lblbase.grid(row=2, column=0,sticky="w", padx=5, pady=10)

numero = StringVar()
txtnumero = ttk.Entry(miframe,textvariable=numero)
txtnumero.grid(row=1,column=1,padx=5, pady=10)

base = StringVar()
txtbase = ttk.Spinbox(miframe,from_=2,to=20,textvariable=base)
txtbase.grid(row=2,column=1,padx=5, pady=10)


imgL = PhotoImage(file="fl2.gif")
lblimg = ttk.Label(miframe, image=imgL)
lblimg.grid(row=1,column=2,rowspan=2,sticky="w", padx=5, pady=10)
lblimg.config(bg="#01DFA5")


lblbaseconvertir = ttk.Label(miframe, text="Ingrese base a convertir")
lblbaseconvertir.grid(row=1,column=3,sticky="w", padx=5, pady=10)


baseconver = StringVar()
txtbase = ttk.Spinbox(miframe,from_=2,to=20,textvariable=baseconver)
txtbase.grid(row=1,column=4,padx=5, pady=10)

btncon = ttk.Button(miframe,text="CONVERTIR",command=iniciarcon)
btncon.grid(row=2,column=3,columnspan=2,padx=5, pady=10)

lblimg2 = ttk.Label(miframe, text="Resultado:")
lblimg2.grid(row=3,column=0,columnspan=3, sticky="e",padx=5, pady=10)

resultado = StringVar()
lblimg2 = ttk.Label(miframe, textvariable=resultado)
lblimg2.grid(row=3,column=3,rowspan=3,sticky="w", padx=5, pady=10)



miframe.pack()


raiz.mainloop()
