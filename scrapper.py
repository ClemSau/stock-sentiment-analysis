import praw
from prawcore.exceptions import ResponseException
import logging
import pandas as pd
import datetime as dt

import settings.secret_settings as settings

reddit = praw.Reddit(client_id='AZdS_b1zE5tKow',
                     client_secret='dLToiSb0pTCBGghFERqlmQnBBL6WdQ',
                     user_agent='reddit-sentiment-analysis',
                     username= settings.reddit_username,
                     password= settings.reddit_password)

try:
    temp = reddit.subreddit('investing').new(limit=100)
    print(len(list(temp)))
except:
    logging.error('Something went wrong during the authentication')