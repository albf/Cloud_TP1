import Tkinter
import tkMessageBox
from Tkinter import *

top = Tk()
L1 = Label(top, text="Choisissez le nombre de serveurs : ")
L1.pack( side = LEFT)
L1.place(x=0,y=25)
E1 = Entry(top, bd =2)
E1.pack(side = RIGHT)
E1.place(x=10,y=50)
E1.insert(1,"0")

nb_serveurs = 0
print "L'entree = %s " % E1.get()




#tab_label = []
tab_entry = []

def choixServeur():
	top2 = Tk()
	j=0
	for i in tab_entry :
		l = Label(top2,text=i.get())
		l.pack(side = LEFT)
		l.place(x=0,y=(j+1)*25)
		j=j+1


def entreeNomsServeurs():
	if int(E1.get())>0:
		nb_serveurs = E1.get()
		tkMessageBox.showinfo( "Vous avez choisi : ", nb_serveurs+" serveur(s)")
		top1 = Tk()
		bouton = Tkinter.Button(top1,text="Envoyer",command=choixServeur)
		bouton.pack()
		for i in range(0,int(nb_serveurs)):
			l = Label(top1, text="Nom du serveur num "+str(i+1)+" : ")
			l.pack(side = LEFT)
			l.place(x=0,y=(2*i+1)*25)
			#tab_label.append(l)
			e = Entry(top1,bd=2)
			e.pack(side = RIGHT)
			e.place(x=10,y=(i+1)*50)
			tab_entry.append(e)
		bouton.place(x=5,y=(int(nb_serveurs)+1)*50)

B = Tkinter.Button(top, text ="Envoyer", command = entreeNomsServeurs)
B.pack()
B.place(x=5,y=100)

top.mainloop()
