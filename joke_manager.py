import urllib.request, json, os


class JokeManager:
    def __init__(self):
        current_folder = os.path.dirname(__file__)
        self.api_url = "https://official-joke-api.appspot.com/random_joke"
        self.filepath = os.path.join(current_folder, "saved_jokes.txt")

    def fetch_joke(self):
        try:
            with urllib.request.urlopen(self.api_url) as response:
                raw_string = response.read().decode("utf-8")
                dict_of_joke = json.loads(raw_string)
                if "setup" in dict_of_joke and "punchline" in dict_of_joke:
                    setup = dict_of_joke["setup"]
                    punchline = dict_of_joke["punchline"]
                    both = f"{setup}\n{punchline}\n\n"
                    return both
        except Exception as e:
            return f"Error fetching joke {e}"

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
