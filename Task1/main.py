print("Program Started .......")
questions = {
    "hello": "Hi there!",
    "bye": "Goodbye!",
    "who are you":"My name is Youssef Ghanem",
    "what is your job":"I am a software engineer",
    "what is the domain of the intern":"It is about AI Development"
}
while True:
    user_input = input("How can I help you: ").lower().strip()
    
    response = questions.get(user_input,"Sorry Dont have answer for that")
    print(response)

    if user_input == "bye":
        break


