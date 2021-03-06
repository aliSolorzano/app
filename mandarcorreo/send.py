# import necessary packages
from login import *
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def mensaje():
    msg = MIMEMultipart()

    content = msj.get("1.0", END)

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

def limpiar():
    print(miCorreo.get())



def main():

    master = tk.Tk()
    master.config(bg="white")
    master.title("Enviador")
    master.resizable(0,0)

    disenoText = ('arial',10,"bold")
    disenoText1 = ('arial',10)

    #Aqui esta el text y la entrada del correo de quien lo manda
    lblDe = tk.Label(master,text="De:",bg="white",font=disenoText).grid(column=0,row=0,sticky=W)
    micorreo = tk.StringVar()
    deCorreo = tk.Entry(master,textvariable=micorreo,width=50,bd=1,font=disenoText1)
    deCorreo.grid(column=0,row=1,sticky=W)

    #Aqui va la contraseña
    lblContra = tk.Label(master,text="Contraseña:",bg="white",font=disenoText).grid(column=0,row=2,sticky=W)
    suContra = tk.StringVar()
    Contra = tk.Entry(master,textvariable=suContra,show="*",width=50,bd=1,font=disenoText1)
    Contra.grid(column=0,row=3,sticky=W)


    #Aqui esta el texto y la entrada del correo de para quien es
    lblPara = tk.Label(master,text="Para:",bg="white",font=disenoText).grid(column=0,row=4,sticky=W)
    sucorreo = tk.StringVar()
    suCorreo = tk.Entry(master,textvariable=sucorreo,width=50,bd=1,font=disenoText1)
    suCorreo.grid(column=0,row=5,sticky=W)


    #aqui va el asunto
    asunto = tk.Label(master,bg="white",text="Asunto:",font=disenoText).grid(column=0,row=6,sticky=W)
    elasunto = tk.StringVar()
    Asunto = tk.Entry(master,textvariable=elasunto,width=50,bd=1,font=disenoText1)
    Asunto.grid(column=0,row=7,sticky=W)

    #Aqui va el contenido de el correo
    msj = tk.Text(master,width=80,height=20,wrap=WORD,bd=1,font=disenoText1)
    msj.grid(column=0,row=8,pady=10)


    #boton para enviar el correo
    btn = tk.Button(master,bg="white",text="Enviar",command=limpiar)
    btn.grid(column=0,row=9)

    #btn = tk.Button(master,bg="white",text="limpiar",command=limpiar)
    #btn.grid(column=1,row=9)

    master.mainloop()
