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
