from os import access
import tweepy
import time
import pyjokes
import time
with open("keys","r") as f:
    lines=f.read().splitlines()
    api_key=lines[0]
    api_secret=lines[1]
    access_token=lines[2]
    access_token_secret=lines[3]
#authenticate
auth=tweepy.OAuthHandler(api_key,api_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
while True:
    api.update_status(pyjokes.get_joke())
    time.sleep(300)