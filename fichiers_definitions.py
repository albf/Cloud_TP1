import json
import pickle

class fichier:
	def __init__(self,id,adress):
		try:
			fobj = open(adress, 'r')
			self.data = fobj.read()
			self.id = id
		except IOError:
			print ("Probleme avec dans la overture du fichier")
	def to_JSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
	def to_PICKLE(self):
		return pickle.dumps(self)
	def print_text(self):
		print(self.data)