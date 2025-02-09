# import library random
import random

# bot names
bot_names = ["Carl", "Rhamz", "Ean", "Sally",
             "Bob", "Aaron", "Gabriel", "Lucas", "Maia"]

index = random.randint(0, len(bot_names))

name = bot_names[index]

print(name)
