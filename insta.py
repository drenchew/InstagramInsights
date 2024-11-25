from instagrapi import Client
from tkinter import ttk
import tkinter as tk

class InstagramInsights:
    def __init__(self, username, password):
        """
        Initialize the InstagramInsights class and log in to Instagram.
        """
        self.client = Client()
        try:
            self.client.login(username, password)
            print("Login successful!")
        except Exception as e:
            print(f"Login failed: {e}")
            raise

    def get_followers(self, username, save=False):
        """
        Get the list of followers of a specified user.

        Args:
            username (str): The username of the target account.
            save (bool): If True, save the followers to a file.

        Returns:
            list: A list of followers' usernames.
        """
        followers_usernames = []
        try:
            user_id = self.client.user_id_from_username(username)
            followers = self.client.user_followers_v1(user_id)

            for follower in followers:
                follower_username = follower.username + '\n'
                if save:
                    with open('followers.txt', 'a') as file:
                        file.write(follower_username)

                followers_usernames.append(follower_username.strip())

            return followers_usernames
        except Exception as e:
            print(f"An error occurred: {e}")
            raise {f'Cant get followers of {username}'}

    def get_unfollowers(self, username, save=False):
        """
        Identify users who unfollowed the account since the last check.

        Args:
            username (str): The username of the target account.
            save (bool): If True, save the unfollowers to a file.

        Returns:
            set: A set of usernames who have unfollowed.
        """
        try:
            with open('followers.txt', 'r') as file:
                previous_followers = set(file.read().splitlines())

            current_followers = set(self.get_followers(username, save=True))
            unfollowers = previous_followers.difference(current_followers)

            if save:
                with open('unfollowers.txt', 'w') as file:
                    for unfollower in unfollowers:
                        file.write(unfollower + '\n')

            return unfollowers
        except FileNotFoundError:
            print("followers.txt not found. Run get_followers() first to save initial followers.")
            return set()
        except Exception as e:
            print(f"An error occurred: {e}")
            return set()
        


if __name__ == "__main__":
   
 pass