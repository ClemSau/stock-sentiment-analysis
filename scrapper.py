import praw
import pandas as pd
import datetime as dt

reddit = praw.Reddit(client_id='AZdS_b1zE5tKow',
                     client_secret='dLToiSb0pTCBGghFERqlmQnBBL6WdQ ',
                     user_agent='reddit-sentiment-analysis',
                     username='YOUR_REDDIT_USER_NAME',
                     password='YOUR_REDDIT_LOGIN_PASSWORD')