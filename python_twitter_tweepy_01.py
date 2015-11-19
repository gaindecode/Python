#Auteur: Khalebios
#Date:19/11/2015 14:41
#Description: Client python permettant l'authentification et l'affichage de la timeline

import tweepy

access_token='290703918-mehDGRGJ6dszHmvuf2jGg7Ze9bGGcb2RSI2fVEpJ'
access_token_secret=str('uGdnjZspEixp4YS8bdstgBUmtzvzgWC61afUCEXbCxSFQ')
consumer_secret=str('YHK9Bj9oOlRzvMUmtoyAwrK4Rrm8kZwtd5GrhuBsiOh8ADRFf8')
consumer_key=str('1LaWIO7wUT15eT7GtM5e74sz7')


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
