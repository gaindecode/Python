class Voiture:
	pass

titine=Voiture()


print "Titine a la propriete Plaque:", hasattr(titine,'plaque')
setattr(titine,'plaque',"3654 LK 69")
print "Valeur plaque:", getattr(titine,'plaque')
print "Titine a la propriete Plaque:", hasattr(titine,'plaque')
delattr(titine,'plaque')
