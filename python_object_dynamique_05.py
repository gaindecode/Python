class Voiture:
	pass

titine=Voiture()
tuture=Voiture();
titine.plaque="1234 JG 73"

print "Plaque Titine:", titine.plaque
#print "Plaque Tuture:", tuture.plaque 
#erreur car plaque non definit pour tuture

#__dict__ propriete permettant d acceder au dictionnaire des attributs de l objet
print titine.__dict__ 
print tuture.__dict__ 

#on peut ajouter un attribut avec __dict__['attribut']=""
tuture.__dict__['plaque']="4567 MP 82"
print "Plaque Tuture:", tuture.plaque 

#exemple creation de propriete
class Noeud :
	def __init__(self,ident):
		self.ident=ident
		self.fils=[]
n1=Noeud(1)
n2=Noeud(2)
n3=Noeud(3)
n1.fils.append(n2)
n2.fils.append(n3)
n3.fils.append(n1)

def has_loop(root):
	if root.deja_vu:
		return True
	root.deja_vu=True
	r=False
	for n in root.fils:
		r|=has_loop(n)
	return r

n1.deja_vu=False;
n2.deja_vu=False
n3.deja_vu=False

print "A une boucle :", has_loop(n1)

#suppression propriete
del n1.deja_vu
print n1.deja_vu

