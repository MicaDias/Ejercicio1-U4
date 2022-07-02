import tkinter as tk
from tkinter import *
from tkinter import ttk, font
class Aplicacion:
    __ventana=None
    __altura=None
    __peso=None
    __imc=None
    __mostrarPeso=None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title("Calculadora de IMC")
        self.__ventana.resizable(0,0)
        fuente = font.Font(weight='bold')
        self.marco=ttk.Frame(self.__ventana, borderwidth=2, relief="raised", padding=(10,10))
        self.__altura=DoubleVar()
        self.__peso=DoubleVar()
        self.__imc=DoubleVar()
        self.__mostrarPeso=StringVar()

        self.__altura.set('')
        self.__peso.set('')
        self.__imc.set('')
        
        self.alturaEntry=ttk.Entry(self.marco, textvariable=self.__altura, width=30)
        self.alturaEntry.focus()
        self.pesoEntry=ttk.Entry(self.marco, textvariable=self.__peso, width=30)
        self.alturaLabel=ttk.Label(self.marco, text="Altura", font=fuente, padding=(5,5))
        self.cmLabel=ttk.Label(self.marco, text="cm", font=fuente, padding=(5,5))
        self.pesoLabel=ttk.Label(self.marco, text="Peso", font=fuente, padding=(5,5))
        self.kgLabel=ttk.Label(self.marco, text="kg", font=fuente, padding=(5,5))
        self.separ1=ttk.Separator(self.marco, orient=HORIZONTAL)
        self.boton1=tk.Button(self.marco, text="Calcular",background='green',width=20, command=self.calcular)
        self.boton2 = tk.Button(self.marco, text="Limpiar",background='green',width=20,command=self.limpiar)
        self.mostrarMensaje=ttk.Label(self.marco, text="Tu Indice de Masa Corporal (IMC) es:", font=fuente, padding=(5,5))
        self.mensajeDePeso=ttk.Label(self.marco, textvariable=self.__imc,font=fuente,padding=(5,5))
        self.mostrarLabel=ttk.Label(self.marco, textvariable=self.__mostrarPeso, font=fuente, padding=(5,5))
        #ubicarwidgets
        self.marco.grid(column=0, row=0)
        self.alturaLabel.grid(column=0, row=0)
        self.alturaEntry.grid(column=1, row=0, columnspan=2)
        self.cmLabel.grid(column=3,row=0,columnspan=4)
        self.pesoLabel.grid(column=0, row=1)
        self.pesoEntry.grid(column=1, row=1, columnspan=2)
        self.kgLabel.grid(column=3,row=1,columnspan=4)
        self.separ1.grid(column=0, row=3, columnspan=3)
        self.boton1.grid(column=1, row=4)
        self.boton2.grid(column=2, row=4)
        self.mostrarMensaje.grid(column=0,row=5)
        self.mensajeDePeso.grid(column=1,row=5)
        self.mostrarLabel.grid(column=1,row=6)
        self.__ventana.mainloop()
    def calcular(self):
        try:
            valor=float(self.alturaEntry.get())
            valor2=float(self.pesoEntry.get())
        except ValueError:
            messagebox.showerror(title='Error de tipo',message='Debe ingresar un valor numérico')
        else:
            alturaMetros=valor/100
            alturaMetros=alturaMetros**2
            self.__imc.set(valor2/alturaMetros)
            if self.__imc.get()<18.5:
                self.__mostrarPeso.set('Peso inferior al normal')
            elif self.__imc.get()>=18.5 and self.__imc.get()<=24.9:
                self.__mostrarPeso.set('Peso Normal')
            elif self.__imc.get()>=25 and self.__imc.get()<29.9:
                self.__mostrarPeso.set('Peso superior al normal')
            elif self.__imc.get()>=30:
                self.__mostrarPeso.set('Obesidad')
    def limpiar(self):
        self.__altura.set("")
        self.__peso.set("")
        self.__imc.set("")
        self.__mostrarPeso.set("")
        self.alturaEntry.focus()