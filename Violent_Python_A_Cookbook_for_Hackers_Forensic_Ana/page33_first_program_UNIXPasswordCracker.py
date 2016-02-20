import crypt
#calculate an encrypted UNIX password hash, we simply
#call the function crypt.crypt() crypt(password,salt parameters)
passw=crypt.crypt("papa365","T2")
print passw

passw=crypt.crypt("bernard2000","pa")
print passw

passw=crypt.crypt("helene1990","ye")
print passw






