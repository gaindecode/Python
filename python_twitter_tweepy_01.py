#Auteur: Khalebios
#Date:19/11/2015 14:41
#Description: Client python permettant l'authentification et l'affichage de la timeline

import tweepy

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
