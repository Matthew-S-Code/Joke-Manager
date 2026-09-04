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

    def read_jokes(self):
        try:
            with open(self.filepath, "r") as my_file:
                data = my_file.read()
                return data 
        except FileNotFoundError:
            return "No jokes saved yet!"



bot = JokeManager()

while True:
    print("\n--- Joke Bot ---")
    print("1. New joke")
    print("2. Read saved jokes")
    print("3. Exit")

    choice = input("Select an option: 1, 2, 3\t> ")

    if choice == "1":
        joke = bot.fetch_joke()
        print(f"\n{joke}")

        save_choice = input("Save this joke? y/n: ").lower()
        if save_choice == "y":
            bot.save_joke(joke)
            print("Joke saved")

    elif choice == "2":
        print()
        print(bot.read_jokes())

    elif choice == "3":
        print("Goodbye")
        break

    else:
        print("Invalid input. Try again")
