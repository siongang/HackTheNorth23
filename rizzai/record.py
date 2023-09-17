import pyaudio
import wave
import keyboard

def record():
    # Parameters for audio recording
    FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
    CHANNELS = 2  # Stereo
    RATE = 44100  # Sample rate (samples per second)
    CHUNK = 1024  # Number of frames per buffer
    RECORD_SECONDS = 5  # Duration of the recording in seconds
    OUTPUT_FILENAME = "rizzai/output_audio.wav"

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Create an audio stream
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("Recording...")

    frames = []

    # Record audio data in chunks and store it in frames
    while(True):
        data = stream.read(CHUNK)
        frames.append(data)

        # Check for keyboard input to exit the loop
        if keyboard.is_pressed('q'):
            print("Stopping recording.")
            break
    print("Finished recording.")

    # Stop and close the audio stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio as a WAV file
    with wave.open(OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    print(f"Audio saved as {OUTPUT_FILENAME}")



