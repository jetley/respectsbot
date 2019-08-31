"""
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
    for tweet in tweepy.Cursor(api.mentions_timeline, since="2019-01-01").items():
        try:
            imagePath = random.choice(os.listdir("images/"))
            tweetId = tweet.user.id
            username = tweet.user.screen_name
            api.update_with_media('images/' + imagePath, "@" + username + " ", in_reply_to_status_id=tweet.id)
            print('Replying to ' + username + 'with ' + imagePath)

        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
    time.sleep(15)