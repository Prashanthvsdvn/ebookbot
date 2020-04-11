import praw

#Reddit API login

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     username='prashanthvsdvn'
                     password=''
                     user_agent='')

#Active Sub reddit
subreddit = reddit.subreddit('FreeEBOOKS')

def getURL(comment):
    lines = comment.readlines()
    for line in lines:
        if line.find('amazon.in'):
            getbook(line)

def getbook(line):

#Search for Amazon links
for post in subreddit.stream.posts():
    for comments in subreddit.stream.comments():
        if comments.user == amazon-converter-bot:
            getURL(comments.body)

