import Tkinter
import tkMessageBox
from Tkinter import *
import os

global tab_entry, tab_label
top = Tk()
L1 = Label(top, text="Choisissez le nombre de serveurs : ")
L1.pack(side = LEFT)
L1.place(x=0,y=25)
E1 = Entry(top, bd =2)
E1.pack(side = RIGHT)
E1.place(x=10,y=50)
E1.insert(1,"0")
nb_serveurs = 0
tab_entry = []
tab_label = []

def afficherFichiers():
	pass

def miseAJour():	
	f = open("/home/user/Desktop/python/Cloud_TP1/liste_adresses",'w')
	for i in tab_entry:
		f.write(i.get()+"\n")
	f.close()

def fichier_longueur(f_nom):
	f = open(f_nom)                  
	lines = 0
	buf_size = 1024 * 1024
	read_f = f.read # loop optimization
	buf = read_f(buf_size)
	while buf:
	        lines += buf.count('\n')
	        buf = read_f(buf_size)
	f.close()
	return lines

#ouvre la fenetre ou il faut afficher le repertoire
def choixServeur():
	miseAJour()
	j=0
	seq=os.listdir("/home/user/Desktop/python/Cloud_TP1/rep_fichiers")
	for i in range(0,len(tab_label)):
		tab_label[i].destroy()
	for i in range(0,len(tab_entry)):
		tab_entry[i].destroy()
	tab_label=[]
	tab_entry=[]
	for i in seq:
		l = Label(top2,text="Fichier num "+j)
		l.pack(side = LEFT)
		l.place(x=0,y=(2*j+1)*25)
		tab_label.append(l)
		e = Entry(top,bd=2)
		e.insert(0,i)
		e.pack(side = RIGHT)
		e.place(x=10,y=(j+1)*50)
		tab_entry.append(e)
		j = j+1


#ouvre la fenetre ou on affiche les adresses des serveurs
def creationEntreesNomsServeurs(nb_serveurs,top):
	nb_lig = fichier_longueur("/home/user/Desktop/python/Cloud_TP1/liste_adresses")
	f = open("/home/user/Desktop/python/Cloud_TP1/liste_adresses")
	lig = f.readlines()
	if(nb_lig < nb_serveurs):
		for i in range(0,nb_lig):
			l = Label(top, text="Nom du serveur num "+str(i+1)+" : ")
			l.pack(side = LEFT)
			l.place(x=0,y=(2*i+1)*25)
			tab_label.append(l)
			e = Entry(top,bd=2)
			e.insert(0,lig[i][:-1])
			e.pack(side = RIGHT)
			e.place(x=10,y=(i+1)*50)
			tab_entry.append(e)
		for i in range(nb_lig,nb_serveurs):
			l = Label(top, text="Nom du serveur num "+str(i+1)+" : ")
			l.pack(side = LEFT)
			l.place(x=0,y=(2*i+1)*25)
			tab_label.append(l)
			e = Entry(top,bd=2)
			e.pack(side = RIGHT)
			e.place(x=10,y=(i+1)*50)
			tab_entry.append(e)
	else:
		for i in range(0,nb_serveurs):
			l = Label(top, text="Nom du serveur num "+str(i+1)+" : ")
			l.pack(side = LEFT)
			l.place(x=0,y=(2*i+1)*25)
			tab_label.append(l)
			e = Entry(top,bd=2)
			e.insert(0,lig[i][:-1])
			e.pack(side = RIGHT)
			e.place(x=10,y=(i+1)*50)
			tab_entry.append(e)
	f.close()

#ouvre la fenetre ou il faut inserer le nombre de serveurs
def entreeNomsServeurs():
	if int(E1.get())>0:
		nb_serveurs = int(E1.get())
		E1.destroy()
		L1.destroy()
		B.configure(command=choixServeur)
		creationEntreesNomsServeurs(nb_serveurs,top)
		B.place(x=5,y=(nb_serveurs+1)*50)

B = Tkinter.Button(top, text ="Envoyer", command = entreeNomsServeurs)
B.pack()
B.place(x=5,y=100)

top.mainloop()
