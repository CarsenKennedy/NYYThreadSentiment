import praw
import secrets
from datetime import datetime 


reddit = praw.Reddit(
    client_id=secrets.client_id,
    client_secret=secrets.client_secret,
    password=secrets.password,
    user_agent=secrets.user_agent,
    username=secrets.username,
)

list_of_threads_to_analyze = []
season_start = '30-March-2023'
dt_start = datetime.strptime(season_start, '%d-%B-%Y')
for submission in reddit.redditor("Yankeebot").submissions.new(limit = 300):
    if "WHAT YOU WANT" in submission.title or 'Game Thread:' in submission.title:
        temp = submission.title 
        x =temp.split('-')
        y = x[-1].split('@')
        
        new = datetime.strptime(y[0],' %B %d, %Y ')
        if new >= dt_start:
            list_of_threads_to_analyze.append(submission.url)
print(list_of_threads_to_analyze)
print(len(list_of_threads_to_analyze))    