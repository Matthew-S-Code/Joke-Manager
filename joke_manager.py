import urllib.request, json, os

"""
create a class that initially defines itself and makes sure that itself and new files stay in 
the local folder and create a file called saved_jokes.txt and save it to self.filepath

create a subroutine for fetching jokes
this goes to the api url, requests a joke and the joke is acquired as the response
read the response, decode it and assign it to a new variable after turning it into a dictionary
check if setup and punchline are in there, create a new variable combining the setup and punchline 
and then return the setup and punchline combo

create a subroutine to save the joke
this takes in the parameter of the joke text
open the self.filepath in append mode and write in the joke text using the 'both' variable to make it easier

"""

class JokeManager:
    def __init__(self):
        current_folder = os.path.dirname(__file__)
        self.api_url = "https://official-joke-api.appspot.com/random_joke"
        self.filepath = os.path.join(current_folder, "saved_jokes.txt")

    def fetch_joke(self):
        with urllib.request.urlopen(self.api_url) as response:
            raw_string = response.read().decode("utf-8")
            dict_of_joke = json.loads(raw_string)
            if "setup" in dict_of_joke and "punchline" in dict_of_joke:
                setup = dict_of_joke["setup"]
                punchline = dict_of_joke["punchline"]
                both = f"{setup}\n{punchline}\n\n"
                return both

    def save_joke(self, joke_text):
        with open(self.filepath, "a") as my_jokes:
            my_jokes.write(joke_text)


# 1. Boot up the system
bot = JokeManager()

# 2. Fetch data from the internet
todays_joke = bot.fetch_joke()

# 3. Prove it worked
print("Fetched:")
print(todays_joke)

# 4. Save it permanently to the hard drive
bot.save_joke(todays_joke)
