from watchlist import Watchlist

class Profile:

    # creates user
    def createUser(self):
        user_name = input("What would you like your username to be: ")

        if not self.is_real_user(user_name):

            with open("database/usernames.txt", "a+") as f:
                f.write(user_name + "\n")
            with open("database/" + user_name + ".txt", "a+") as f:
                f.write("[]")
            print("You created an account with the username: " + user_name)
        else:
            print("Sorry, that username has been taken.")

    # Logs into user and retrieves their data. Returns None if that user does not exist
    def login(self):
        # user_watchlist.watchlist = ["TSLA"]
        user_name = input("What is your username?")
        if self.is_real_user(user_name):
            print("You have logged into: " + user_name)
        else:
            print("Sorry that account does not exist")

    # Given a string it returns True or Flase if that username is in usernames.txt
    def is_real_user(self, user_name):
        with open("database/usernames.txt", "r") as f:
            test_name = f.readline().strip()
            if test_name == user_name:
                return True



