import praw
import os

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

def main():

    reddit = authenticate()

    subreddit = reddit.subreddit('test')
    key_phrase = os.environ["bot_phrase"]
    key_response = os.environ["bot_response"]

    for comment in subreddit.stream.comments():
        if key_phrase in comment.body.lower():
            comment.reply(key_response)

if __name__ == "__main__":
    main()
