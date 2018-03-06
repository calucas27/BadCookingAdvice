import tweepy
import os

consumer_key = 'your consumer key'
consumer_secret = 'your consumer secret'
access_token = 'your access token'
access_token_secret = 'your secret token'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

os.system("./cookbook.sh")
file = open('cookbook.out','r')
tweet = file.read()
file.close()
api.update_status(status=tweet)