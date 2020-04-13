import praw
import os

#Reddit API login

reddit = praw.Reddit(client_id='6_4z5ED51KUb8g', client_secret='LUxQnirGsYm4iZuxfpRe6_9qLAg', user_agent='Ebook client v0.1')

#Active Sub reddit
subreddit = reddit.subreddit('FreeEBOOKS')

#Create a txt file
f=open("books.txt","at")

#function to scrape the link
def getURL(comment):
    commentlines = comment.splitlines()
    for line in commentlines:
        if (line.find('amazon.in') == 1):#Searching for amazon.in links
            f.write(line[12:-2]+"\n")
            os.system("firefox " + line[12:-2])#Opening all the links with firefox

#Searching through the subreddit for new posts
for post in subreddit.new():
    #Checking for books which are tagged as expired
    if (post.link_flair_text!= "Expired"):
        for comment in post.comments:
            #Checking for comment by a link sharing bot
            if (comment.author == "amazon-converter-bot"):
                f.write("{} (flair:{})\n".format(post.title,post.link_flair_text))
                getURL(comment.body)

f.close()
