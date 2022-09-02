import praw
import os

def bot_login():
    try:
        print("logging in: ", os.getenv("reddit_username"))
        reddit = praw.Reddit(client_id = os.getenv("client_id"),
                    client_secret = os.getenv("client_secret"),
                    user_agent = os.getenv("user_agent"),
                    username = os.getenv("reddit_username"),
                    password = os.getenv("reddit_password"))   
        print("logged in!")
    except:
        print("Login failed")

    return reddit
