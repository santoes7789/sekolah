name = "my name goes here";
def starting():
    print("**Welcome to dream pizza**")
    print(f"**My name is {name} **")


def userInfoQuestions(question):
    userInput = input(question + "\n")
    if not userInput:
        print("Sorry, this cannot be blank")
        return userInfoQuestions(question)
    return userInput



starting()
userInfoQuestions("Please enter name:")
userInfoQuestions("Please enter phone number:")

