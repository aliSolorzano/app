from send import *
import tkinter as tk
from tkinter import *
from tkinter import messagebox

def enviar():
    print(miCorreo.get())
    print(miContra.get())
    root.destroy()
    main()

root = Tk()
root.title("Iniciar sesión")

disenoText = ('arial',20,"bold")

lbl = Label(root,text="Iniciar sesión",font=disenoText)
lbl.grid(row=0,column=1)

lblCorreo = Label(root,text="Correo")
lblCorreo.grid(row=1,column=0,sticky=W)

miCorreo = StringVar()
correo = Entry(root,textvariable=miCorreo)
correo.grid(row=1,column=1)

lblContra = Label(root,text="Contraseña")
lblContra.grid(row=2,column=0)

miContra = StringVar()
contra = Entry(root,textvariable=miContra)
contra.grid(row=2,column=1)


btn = Button(root,text="Enviar",command=enviar)
btn.grid(row=3,column=1)

root.mainloop()
