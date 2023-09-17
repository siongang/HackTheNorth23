import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

def speech_to_text(audio_file_path):
    # Specify the audio file path
    audio_file_path = "HackTheNorth23/rizzai/output_audio.wav"  # Replace with the path to your audio file

    # Read the audio file
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)

    # Perform the speech recognition
    try:
        recognized_text = recognizer.recognize_google(audio_data)  # You can use other engines too
        print("Recognized text:", recognized_text)
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

    return recognized_text
