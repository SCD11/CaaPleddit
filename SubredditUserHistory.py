#Idea here to create a script which can we used to depict the demographics of a subreddit
#we will later employ graphs,etc. to visualise the data
import praw

class SubredditDemographics():
        
    def __init__(self, subname, subreddit_instance):
        self.subreddit = subreddit_instance
        self.users = open(str(subname + "Users.txt"), 'a')
        self.demographics = open(str(subname + "Demographics.txt"), 'a')
        self.users_list = []
        self.sub_list = {}
    

    def fetchUsers(self):
        self.fetchPosters()
        self.fetchCommenter()

    def fetchPosters(self):
        for submission in self.subreddit.hot(limit=100):
            # print(submission.author.name)
            try:
                if submission.author.name not in self.users_list:
                    print(type(submission.author.name))
                    self.users_list.append(submission.author.name)
                    self.users.write(submission.author.name + "\n")
            except:
                print("Error Happened!")

    def fetchCommenter(self):
        for submission in self.subreddit.hot(limit=100):
            submission.comments.replace_more(limit=None)
            for comment in submission.comments.list():
                try:
                    if comment.author.name not in self.users_list:
                        self.users_list.append(comment.author.name)
                        self.users.write(comment.author.name + "\n")
                except:
                    print("Error Happened!")
        self.users.close()
        self.demographics.close()


reddit = praw.Reddit(client_id = "u3HlJMzOxS8LCg", client_secret = "sNTYx5xyc2TGWqhsOl8fHSF_sK8", user_agent="ashutosh")
subname = "india"
subreddit = reddit.subreddit(subname)

obj = SubredditDemographics(subname,subreddit)
# obj.fetchUsers()