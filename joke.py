import random

def generate_random_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the chicken go to the seance? To talk to the other side!",
        "Why don't some fish play piano? Because you can't tuna fish!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ]
    return random.choice(jokes)

print(generate_random_joke())