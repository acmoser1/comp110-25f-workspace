"""Definition of the Profile class."""


class Profile:

    username: str
    private: bool

    # Constructor
    def __init__(self, username_input: str):
        self.username = username_input
        self.private = True

    # Method
    def tweet(self, message: str):
        if self.private is False:
            print(message)

    # Magic Method
    def __str__(self) -> str:
        if self.private:
            return f"{self.username}: Private"
        else:
            return f"{self.username}: Public"


# INSTANTIATE
# Create new variable, user1, with username 110_rulez
user1: Profile = Profile("110_rulez")
# Update private attribute to false
user1.private = False
# Call the tweet method
user1.tweet("OOP is cool!")
print(user1)
