import speech_recognition as sr
from gemini import helper
from sqlite import add_todo_db

def listen_for_wake_word(recognizer, microphone, wake_word="hello"):
    """Continuously listen for a specific wake word."""
    print("Waiting for wake word...")
    while True:
        try:
            # Listen for audio
            recognizer.adjust_for_ambient_noise(microphone, duration=1)
            audio = recognizer.listen(microphone)
            
            # Recognize speech
            text = recognizer.recognize_google(audio).lower()
            print(f"Heard: {text}")
            
            if wake_word in text:
                print("Wake word detected!")
                return True
        except sr.UnknownValueError:
            continue
        except sr.RequestError:
            print("Error with the speech recognition service.")
            return False

def listen_for_command(recognizer, microphone):
    """Listen for the user's command."""
    print("Listening for a command...")
    try:
        recognizer.adjust_for_ambient_noise(microphone, duration=1)
        audio = recognizer.listen(microphone)
        command = recognizer.recognize_google(audio)
        print(f"Command received: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Error with the speech recognition service.")
    return None


if __name__ == "__main__":
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        while True:
            # Wait for wake word
            if listen_for_wake_word(recognizer, mic):
                # Listen for and process the command
                command = listen_for_command(recognizer, mic)
                if command:
                    response = helper(command)
                    response["due"] = response["due"].replace("T"," ")
                    add_todo_db(response['name'],"","m",response['due'])