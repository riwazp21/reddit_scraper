import praw
import sys

def content_scraper(url):
    
    reddit = praw.Reddit(
        client_id='jh9iRoDr15Ce22oM4rNT2Q',
        client_secret='nftbO-r1ReVlv4QDH3tD7raEGMu2Gg',
        user_agent='Riwaz',
    )

    submission = reddit.submission(url = url)
    submission.comments.replace_more(limit=None)
    comment_queue = submission.comments[:] 

    
    f = open("comments.txt","w")

    while comment_queue:
        comment = comment_queue.pop(0)
    #    print(comment.body)
        f.write(comment.body + '\n')
        comment_queue.extend(comment.replies)
    f.close()


if __name__ == "__main__":
    #url = "https://www.reddit.com/r/redditdev/comments/110z3ii/issues_retrieving_the_entire_comment_tree_on_a/"
    
   
    url = sys.argv[1]
    print(url)
    content_scraper(url)

