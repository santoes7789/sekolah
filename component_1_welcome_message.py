# import library random
import random

# bot names
bot_names = ["Carl", "Rhamz", "Ean", "Sally",
             "Bob", "Aaron", "Gabriel", "Lucas", "Maia"]


def welcome():
    index = random.randint(0, len(bot_names))
    name = bot_names[index]
    print("***Welcome to Dream Pizza***")
    print("***My name is", name, "***")
    print("***I will be here to help you order your delicious Dream Pizza***")


def main():
    welcome()


main()
