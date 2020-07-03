#Idea here to create a script which can we used to depict the demographics of a subreddit
#we will later employ graphs,etc. to visualise the data
#subs : r/india, r/indiaspeaks, r/pakistan r/chutyapa, r/islam r/izlam, r/kerimama r/bangladesh,r/nepal2 r/nepal, r/murica r/usa, r/canada, r/unitedkingdom
import praw

class SubredditDemographics():
        
    def __init__(self, subname, subreddit_instance, reddit_instance):
        self.reddit_instance = reddit_instance
        self.subreddit = subreddit_instance
        self.users = open(str(subname + "Users.txt"), 'a')
        self.demographics = open(str(subname + "Demographics.txt"), 'a')
        self.users_list = []
        self.sub_dict = {
            "pakistan": { "count" : 0, "users" : []},
            "bangladesh" : {"count" : 0, "users" : []},
            "nepal" : {"count" : 0, "users" : []},
            "usa" : {"count" : 0, "users" : []},
            "uk" : {"count" : 0, "users" : []},
            "canada" : {"count" : 0, "users" : []},
            "islam" : {"count" : 0, "users" : []},
            "randia" : {"count" : 0, "users" : []},
            "indiaspeaks" : {"count" : 0, "users" : []}
        }


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
        for submission in self.subreddit.hot(limit=50):
            submission.comments.replace_more(limit=None)
            for comment in submission.comments.list():
                try:
                    if comment.author.name not in self.users_list:
                        self.users_list.append(comment.author.name)
                        self.users.write(comment.author.name + "\n")
                except:
                    print("Error Happened!")

    def checkDemography(self):
        print("*"*100)
        for user in self.users_list:
            try:
                user_instance = self.reddit_instance.redditor(user)
                self.checkIfPakistani(user_instance)
                self.checkIfBulla(user_instance)
                self.checkIfNepali(user_instance)
                self.checkIfBangladeshi(user_instance)
                self.checkIfUSA(user_instance)
                self.checkIfUk(user_instance)
                self.checkIfCanada(user_instance)
                self.checkIfRandia(user_instance)
                self.checkIfIndiaSpeaks(user_instance)
            except:
                print("Error occuried while CAA!")
        self.writeOutput()

    def checkIfPakistani(self, user_instance):
        for submission in user_instance.submissions.hot(limit=20):
            if str(submission.subreddit).strip().lower() == "pakistan" or str(submission.subreddit).strip().lower() == "chutyapa":
                self.sub_dict["pakistan"]["count"] += 1
                self.sub_dict["pakistan"]["users"].append(user_instance.name)
                print("pakistani spotted")
                return
    
    def checkIfBangladeshi(self, user_instance):
        for submission in user_instance.submissions.hot(limit=20):
            if str(submission.subreddit).strip().lower() == "bangladesh" or str(submission.subreddit).strip().lower() == "kiremama":
                self.sub_dict["bangladesh"]["count"] += 1
                self.sub_dict["bangladesh"]["users"].append(user_instance.name)
                print("Bangladeshi spotted")
                return

    def checkIfCanada(self, user_instance):
        for submission in user_instance.submissions.hot(limit=20):
            if str(submission.subreddit).strip().lower() == "canada" or str(submission.subreddit).strip().lower() == "metacanada":
                self.sub_dict["canada"]["count"] += 1
                self.sub_dict["canada"]["users"].append(user_instance.name)
                print("Canadi spotted")
                return
    
    def checkIfUk(self, user_instance):
        for submission in user_instance.submissions.hot(limit=20):
            if str(submission.subreddit).strip().lower() == "unitedkingdom" or str(submission.subreddit).strip().lower() == "uk":
                self.sub_dict["uk"]["count"] += 1
                self.sub_dict["uk"]["users"].append(user_instance.name)
                print("British spotted")
                return

    def checkIfUSA(self, user_instance):
        for submission in user_instance.submissions.hot(limit=20):
            if str(submission.subreddit).strip().lower() == "usa" or str(submission.subreddit).strip().lower() == "murica":
                self.sub_dict["usa"]["count"] += 1
                self.sub_dict["usa"]["users"].append(user_instance.name)
                print("Yanki spotted")
                return

    def checkIfBulla(self, user_instance):
        for submission in user_instance.submissions.hot(limit=20):
            if str(submission.subreddit).strip().lower() == "islam" or str(submission.subreddit).strip().lower() == "izlam":
                self.sub_dict["islam"]["count"] += 1
                self.sub_dict["islam"]["users"].append(user_instance.name)
                print("Pincturewala Spotted!")
                return
    
    def checkIfNepali(self, user_instance):
        for submission in user_instance.submissions.hot(limit=20):
            if str(submission.subreddit).strip().lower() == "nepal":
                self.sub_dict["nepal"]["count"] += 1
                self.sub_dict["nepal"]["users"].append(user_instance.name)
                print("Nepali spotted")
                return

    def checkIfRandia(self, user_instance):
        for submission in user_instance.submissions.hot(limit=20):
            if str(submission.subreddit).strip().lower() == "india" or str(submission.subreddit).strip().lower() == "librandu":
                self.sub_dict["randia"]["count"] += 1
                self.sub_dict["randia"]["users"].append(user_instance.name)
                print("Randian spotted")
                return
    
    def checkIfIndiaSpeaks(self, user_instance):
        for submission in user_instance.submissions.hot(limit=20):
            if str(submission.subreddit).strip().lower() == "indiaspeaks" or str(submission.subreddit).strip().lower() == "chodi":
                self.sub_dict["indiaspeaks"]["count"] += 1
                self.sub_dict["indiaspeaks"]["users"].append(user_instance.name)
                print("Virat spotted")
                return
        

    def writeOutput(self):
        for key in self.sub_dict.keys():
            temp = open(str(key+".txt"),"a")
            temp.write(key.capitalize() + " : " + str(self.sub_dict[key]["count"]))
            self.demographics.write(key.capitalize() + " : " + str(self.sub_dict[key]["count"]) + "\n")
            temp.write(str("\nUSERS ARE : \n"))
            for user in self.sub_dict[key]["users"]:
                temp.write(user + "\n")
            temp.write("*"*100 + "\n")
            temp.close()
        self.closeEverything()
     
    def closeEverything(self):
        print(self.sub_dict)
        self.users.close()
        self.demographics.close()

reddit = praw.Reddit(client_id = "u3HlJMzOxS8LCg", client_secret = "sNTYx5xyc2TGWqhsOl8fHSF_sK8", user_agent="ashutosh")
subname = input("Enter the name of the sub : ")
subreddit = reddit.subreddit(subname)

obj = SubredditDemographics(subname,subreddit,reddit)
obj.fetchUsers()
obj.checkDemography()


#some observatios related to praw
#submission.subreddit is enough to get the name of a reddit
#submission.subreddit.id and subreddit.name are useless