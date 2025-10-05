import pyttsx3

def main():
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Ask the user to enter text
    text = input("Enter the text you want to hear: ")

    # Speak the text aloud
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    main()