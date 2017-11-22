import praw
import os
import re

def authenticate():
    cid = os.environ["bot_client_id"]
    secret = os.environ["bot_secret"]
    user_pass = os.environ["bot_user_password"]
    user_name = os.environ["bot_user_name"]
    user_agent = os.environ["bot_user_agent"]

    reddit = praw.Reddit(client_id=cid,
                         client_secret=secret,
                         password=user_pass,
                         user_agent=user_agent,
                         username=user_name)
    return reddit

reddit = authenticate()
my_subreddits = list(reddit.user.subreddits(limit=None))

print(list(my_subreddits[1].stream.comments()))
