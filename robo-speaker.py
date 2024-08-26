import pyttsx3

engine = pyttsx3.init()

while True:
    text = input("Enter what you want to speak (type 'exit' to stop): ")

    if text.lower() == "exit":
        print("Exiting...")
        break

    engine.say(text)
    engine.runAndWait()
