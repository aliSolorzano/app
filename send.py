# import necessary packages

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from tkinter import *
import tkinter as tk
from tkinter import messagebox


def mensaje():
    msg = MIMEMultipart()


    message = elcontenido.get()

    # setup the parameters of the message
    password = suContra.get()
    msg['From'] = micorreo.get()
    msg['To'] = sucorreo.get()
    msg['Subject'] = elasunto.get()

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)


    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    messagebox.showinfo(message="Se ha enviado correctamente el mensaje a el correo: " + str(msg['To']), title="Título")



root = Tk()
root.title("Enviador")
root.config(bg="white")

disenoText = ('arial',10,"bold")

#Aqui esta el text y la entrada del correo de quien lo manda
lblDe = Label(root,text="De:",bg="white",pady=10,font=disenoText).grid(column=1,row=1,sticky=E)
micorreo = tk.StringVar()
deCorreo = Entry(root,textvariable=micorreo,width=50).grid(column=2,row=1,)


lblContra = Label(root,text="Contraseña:",bg="white",pady=10,font=disenoText).grid(column=1,row=2,sticky=E)
suContra = tk.StringVar()
Contra = Entry(root,textvariable=suContra,width=50).grid(column=2,row=2)



#Aqui esta el texto y la entrada del correo de para quien es
lblPara = Label(root,text="Para:",bg="white",pady=10,font=disenoText).grid(column=1,row=3,sticky=E)
sucorreo = tk.StringVar()
deCorreo = Entry(root,textvariable=sucorreo,width=50).grid(column=2,row=3)


#aqui va el asunto
asunto = Label(root,bg="white",text="Asunto",pady=10,font=disenoText).grid(column=1,row=4,sticky=E)
elasunto = tk.StringVar()
Asunto = Entry(root,textvariable=elasunto,width=50).grid(column=2,row=4)


contenido = Label(root,bg="white",text="Contenido",pady=20,font=disenoText).grid(column=1,row=5,sticky=E)
elcontenido = tk.StringVar()
msj = Entry(root,textvariable=elcontenido,width=50).grid(column=2,row=5)


btn = Button(root,text="Enviar",command=mensaje)
btn.grid(column=2,row=6)

root.mainloop()
