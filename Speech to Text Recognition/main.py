import speech_recognition


def record_voice():
    microphone = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as live_phone:
        microphone.adjust_for_ambient_noise(live_phone)
        print("I'm listening...")
        audio = microphone.listen(live_phone)

    try:
        phrase = microphone.recognize_google(audio, language='en')
        print(f"You said: {phrase}")
        return phrase
    except speech_recognition.UnknownValueError:
        print("I didn't understand you")
        return ""


if __name__ == "__main__":
    phrase = record_voice()

    with open("./Speech to Text Recognition/voice.txt", "w") as file:
        file.write(phrase)
    print("Done!")
