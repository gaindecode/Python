#Auteur: Khalebios
#Date:19/11/2015 17:50
#Description: Client python permettant l'authentification et l'affichage de la timeline
#Recherche un utilisateur:avoir un user object (regarder l'api Twitter pour plus de fonctionnalite

import tweepy
import json

access_token=''
access_token_secret=str('')
consumer_secret=str('')
consumer_key=str('')


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text


user = api.get_user('onegalsen')
print str(user.screen_name)
print str("Nombre de Followers: ")+str(user.followers_count) 
print str("Nombre de tweets favoris: ")+str(user.favourites_count)
try :
	for friend in user.friends():
   		print friend.screen_name
except tweepy.TweepError as e:
	print "premier i message******************************"
	#print api.rate_limit_status()


#Pagination
print
print "Pagination!!"
# Iterate through all of the authenticated user's friends
try:
	numberfriends=0
	for friend in tweepy.Cursor(api.friends).items():
    	# Process the friend here
    		print friend.screen_name
		numberfriends=numberfriends+1
	print numberfriends
		
except tweepy.TweepError as e:
	print "premier message******************************"
	#print e[0][0]  
    	#data = json.dumps(e[0][0])
	print "Error from the api"
except Exception,e:
	print "deuxieme message******************************"
	print e


