import random

def generate_random_emoji():
    emojis = ["^_^", "O_O", "-_-", ">_<", ":)", ":(", ":D", ":P"]
    return random.choice(emojis)

print(generate_random_emoji())