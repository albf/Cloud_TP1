import Tkinter
import tkMessageBox
from Tkinter import *
import os

global tab_entry, tab_label, top, nb_serveurs
top = Tk() #la fenetre principale
L1 = Label(top, text="Choisissez le nombre de serveurs : ") #le label dans la premiere fenetre
L1.pack(side = LEFT)
L1.place(x=0,y=25)
E1 = Entry(top, bd =2) #l'entree dans la premiere fenetre
E1.pack(side = RIGHT)
E1.place(x=10,y=50)
E1.insert(1,"0")
nb_serveurs = 0
tab_entry = [] #le tableau contenant toutes les entrees qui vont etre creees plus tard
tab_label = [] #le tableau contenant tous les labels qui vont etre crees plus tard

#tab est un tableau contenant des widgets, supprimerTab detruit tous les widgets et vide tab
def supprimerTab(tab):
	for i in tab:
		i.destroy()
	tab=[]

#une fonction a etre changee
def afficherFichiers():
	#print "afficherFichiers"
	pass

#calcule le nombre de lignes d'un fichier donne
def fichier_longueur(f_nom):
	f = open(f_nom) #on ouvre le fichier                
	lignes = 0 #le nombre de lignes
	taille_tampon = 1024 * 1024 #la taille du tampon
	read_f = f.read #l'optimisation de la boucle
	tampon = read_f(taille_tampon) #le tampon
	while tampon: #tant qu'il reste des octets a lire
	        lignes += tampon.count('\n') #incrementation du nombre de lignes
	        tampon = read_f(taille_tampon) #lecture des prochains octets
	f.close() #on ferme le fichier
	return lignes #retourne le nombre de lignes

#ouvre la fenetre ou on affiche le repertoire
def choixServeur():
	#print "choixServeur"
	f = open("/home/user/Desktop/python/Cloud_TP1/liste_adresses",'w') #on ouvre le fichier contenant les adresses des serveurs
	for i in tab_entry: #pour chaque entree
		f.write(i.get()+"\n") #on extrait la nouvelle adresse et on l'ecrit a la ligne correspondante
	f.close() #on ferme le fichier
	seq=os.listdir("/home/user/Desktop/python/Cloud_TP1/rep_fichiers") #liste des fichiers presents dans les repertoires concernes
	#on supprime les widgets deja existants
	supprimerTab(tab_entry) 
	supprimerTab(tab_label)
	j=0 #une variable permettant de determiner la position des widgets
	for i in seq: #on construit tous les nouveaux widgets
		l = Label(top,text="Fichier num "+str(j+1))
		l.pack(side = LEFT)
		l.place(x=0,y=(2*j+1)*25)
		tab_label.append(l)
		e = Entry(top,bd=2)
		e.insert(0,i)
		e.pack(side = RIGHT)
		e.place(x=10,y=(j+1)*50)
		tab_entry.append(e)
		j = j+1
	B.place(x=5,y=(len(seq)+1)*50)  #la nouvelle position du bouton B
	B.configure(command=afficherFichiers) #la nouvelle fonction du bouton B

#ouvre la fenetre ou on affiche les adresses des serveurs
def creationEntreesNomsServeurs(nb_serveurs,top):
	nb_lig = fichier_longueur("/home/user/Desktop/python/Cloud_TP1/liste_adresses") #nombre d'adresses (1 ligne = 1 adresse)
	f = open("/home/user/Desktop/python/Cloud_TP1/liste_adresses") #on ouvre le meme fichier
	lig = f.readlines() #on lit son contenu
	if(nb_lig < nb_serveurs): #si le nombre de lignes du fichier est inferieur au nombre de serveurs choisi a l'etape precedente, alors on va afficher toutes les adresses dans le nb_lig premieres entrees 
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
		for i in range(nb_lig,nb_serveurs): #et ensuite on va introduire les entrees vides restantes
			l = Label(top, text="Nom du serveur num "+str(i+1)+" : ")
			l.pack(side = LEFT)
			l.place(x=0,y=(2*i+1)*25)
			tab_label.append(l)
			e = Entry(top,bd=2)
			e.pack(side = RIGHT)
			e.place(x=10,y=(i+1)*50)
			tab_entry.append(e)
	else:
		for i in range(0,nb_serveurs): #on va introduire les nb_serveurs premieres adresses
			l = Label(top, text="Nom du serveur num "+str(i+1)+" : ")
			l.pack(side = LEFT)
			l.place(x=0,y=(2*i+1)*25)
			tab_label.append(l)
			e = Entry(top,bd=2)
			e.insert(0,lig[i][:-1])
			e.pack(side = RIGHT)
			e.place(x=10,y=(i+1)*50)
			tab_entry.append(e)
	f.close() #on ferme le fichier

#ouvre la fenetre ou il faut inserer le nombre de serveurs
def entreeNomsServeurs():
	#print "entreeNomsServeurs"
	if int(E1.get())>0: #si le nombre de serveurs est > 0, alors on change la fenetre
		nb_serveurs = int(E1.get())
		E1.destroy()
		L1.destroy()
		B.configure(command=choixServeur)
		creationEntreesNomsServeurs(nb_serveurs,top)
		B.place(x=5,y=(nb_serveurs+1)*50)

B = Tkinter.Button(top, text ="Envoyer", command = entreeNomsServeurs) #le bouton "Envoyer"
B.pack()
B.place(x=5,y=100) #sa position

top.mainloop()
