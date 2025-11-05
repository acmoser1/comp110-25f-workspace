"""Instantiate the Profile class."""

from lessons.profile import Profile

# Create new variable, user1, with username 110_rulez
user1: Profile = Profile("110_rulez")
# Update private attribute to false
user1.private = False
# Call the tweet method
user1.tweet("OOP is cool!")
