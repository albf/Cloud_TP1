class fichier:
	def __init__(self,id,adress):
		try:
			self.fobj = open(adress, 'r')
			self.id = id
		except IOError:
			print ("Probleme avec dans la overture du fichier")
	def read_print_fichier(self):
		lines = self.fobj.readlines()
		print (lines)