# import necessary packages

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def mensaje():
    msg = MIMEMultipart()

    content = msj.get("1.0", END)
    entry_content.set(content)
    message = content

    # setup the parametegridrs of the message
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


def gettext():

    content = msj.get("1.0", END)

    messagebox.showinfo(message=content, title="Título")
    print(msj.get(1.0, "end"))

master = tk.Tk()
master.config(bg="white")
master.title("Enviador")

disenoText = ('arial',10,"bold")

#Aqui esta el text y la entrada del correo de quien lo manda
lblDe = tk.Label(master,text="De:",bg="white",pady=10,font=disenoText).grid(column=1,row=1,sticky=E)
micorreo = tk.StringVar()
deCorreo = tk.Entry(master,textvariable=micorreo,width=50).grid(column=2,row=1,)


#Aqui va la contraseña
lblContra = tk.Label(master,text="Contraseña:",bg="white",pady=10,font=disenoText).grid(column=1,row=2,sticky=E)
suContra = tk.StringVar()
Contra = tk.Entry(master,textvariable=suContra,show="*",width=50).grid(column=2,row=2)


#Aqui esta el texto y la entrada del correo de para quien es
lblPara = tk.Label(master,text="Para:",bg="white",pady=10,font=disenoText).grid(column=1,row=3,sticky=E)
sucorreo = tk.StringVar()
deCorreo = tk.Entry(master,textvariable=sucorreo,width=50).grid(column=2,row=3)


#aqui va el asunto
asunto = tk.Label(master,bg="white",text="Asunto",pady=10,font=disenoText).grid(column=1,row=4,sticky=E)
elasunto = tk.StringVar()
Asunto = tk.Entry(master,textvariable=elasunto,width=50).grid(column=2,row=4)

#Aqui va el contenido de el correo
contenido = tk.Label(master,bg="white",text="Contenido",pady=20,font=disenoText).grid(column=1,row=5,sticky=E)
msj = tk.Text(master,width=80,height=20,wrap=WORD)
msj.grid(column=2,row=5)

entry_content = tk.StringVar()
entry = tk.Entry(master, textvariable=entry_content)


#boton para enviar el correo
btn = tk.Button(master,bg="white",text="Enviar",command=mensaje)
btn.grid(column=2,row=6)

master.mainloop()
