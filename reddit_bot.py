import praw
import time
import sys

reddit = praw.Reddit(
    client_id="id",
    client_secret="secret",
    user_agent="version",
    username='usn',
    password='pwd'
)

subreddit_name = sys.argv[1].title()
subreddit = reddit.subreddit(subreddit_name)

for submission in subreddit.hot():
    for comment in submission.comments:
        if hasattr(comment, 'body'):
            comment_lower = comment.body.lower()  
            if 'word' in comment_lower:
                print(comment.body)
                print()
                comment.reply('An example of how a bot should respond.')
                time.sleep(660)
            