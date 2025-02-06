import random

bot_names = ["Mark", "Sally", "Carl", "Aaron", "Rhamz", "Ean", "Kim", "Mikayla", "Josh", "Lewis"]
rand_name_index = random.randint(0, len(bot_names))
name = bot_names[rand_name_index]

def welcome():
    print("**Welcome to dream pizza**")
    print(f"**My name is {name} **\n")


def userInfoQuestions(question):
    userInput = input(question + "\n")
    if not userInput:
        print("Sorry, this cannot be blank")
        return userInfoQuestions(question)
    return userInput



welcome()
userInfoQuestions("Please enter name:")
userInfoQuestions("Please enter phone number:")

