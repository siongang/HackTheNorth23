import record
import speech
import facial
import concurrent.futures


facial_emotions = []
# Create a ThreadPoolExecutor with a specified number of worker threads
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:

    record_ex = executor.submit(record.record)
    facial_ex = executor.submit(facial.facial)

    # Wait for all functions to complete
    concurrent.futures.wait([record_ex, facial_ex])   
    # Optionally, you can retrieve the results of the functions
    
    facial_emotions = facial_ex.result()


# speech.speech_to_text("HackTheNorth23/rizzai/output_audio.wav")q

print(facial_emotions)