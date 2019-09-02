""" --Comment block. Since Glitch executes the app everytime a modification is performed and there's no stop button, I've come up with the idea of writing a hastag symbol before the comment block to uncomment the comment block and make the bot work again. It works like a "stop" button.

import tweepy
import logging
from config import create_api
import time
import os
import random
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

api = create_api()

imagePath = random.choice(os.listdir("images/"))

while True:
    #Read last tweet ID, wich is saved in a TXT file.
    last_tweet = open("last_tw.txt", "r") 

    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=last_tweet).items(): #since="2019-09-01" --don't touch.
        try:
            imagePath = random.choice(os.listdir("images/")) 

            tweetId = tweet.user.id
            username = tweet.user.screen_name

            #api.update_with_media('images/' + imagePath, "@" + username + " ", in_reply_to_status_id=tweet.id)
            #Debug line. Will be used to simulate 'api.update_with_media'(upper line) until the bot works fine (Prevent accidental replies to mentions while coding).
            print('Replying to ' + username + ' with ' + imagePath) 

            #Opens 'last_twt.txt' and writes 'tweet.user.id' to be read later.
            f = open("last_twt.txt.txt", "a")
            f.write(tweet.user.id)
            f.close()
            print('File written with tweet id ' + tweet.user.id)

        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
    time.sleep(60)
