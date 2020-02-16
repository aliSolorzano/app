from send import *
import tkinter as tk
from tkinter import *
from tkinter import messagebox

def enviar():
    if miCorreo.get() == "admin" and miContra.get()=="admin":
        root.destroy()
        main()
    else:
        messagebox.showwarning(message="Correo incorrecto",title="Error")

root = Tk()
root.title("Iniciar sesión")
root.config(bg="white")
x = (root.winfo_screenwidth() - root.winfo_reqwidth())*0.4
y = (root.winfo_screenheight() - root.winfo_reqheight())* 0.5
#Anchura X Altura
root.geometry("+%d+%d" % (x,y))
root.resizable(0,0)
disenoText = ('arial',20,"bold")


lbl = Label(root,text="Iniciar sesión",font=disenoText,bg="white")
lbl.grid(row=0,column=1)

lblCorreo = Label(root,text="Correo",bg="white")
lblCorreo.grid(row=1,column=0)

miCorreo = StringVar()
correo = tk.Entry(root,textvariable=miCorreo,borderwidth=2)
correo.grid(row=1,column=1,sticky=W)

lblContra = Label(root,text="Contraseña",bg="white")
lblContra.grid(row=2,column=0)

miContra = StringVar()
contra = Entry(root,textvariable=miContra,borderwidth=2,show="*")
contra.grid(row=2,column=1,sticky=W)


btn = Button(root,text="Enviar",command=enviar,bg="white",bd=1)
btn.grid(row=3,column=1,pady=5)

root.mainloop()
