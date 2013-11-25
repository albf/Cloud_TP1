import Tkinter
import tkMessageBox
from Tkinter import *

top = Tk()
L1 = Label(top, text="Choississez le nombre de serveurs : ")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)

E1.pack(side = RIGHT)

def helloCallBack():
   if len(E1.get())!=0:
           tkMessageBox.showinfo( "Vous avez choisi : ", E1.get()+" serveur(s)")


B = Tkinter.Button(top, text ="Envoyer", command = helloCallBack)

B.pack()

top.mainloop()
