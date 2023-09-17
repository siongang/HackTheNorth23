import record
import speech


facial_emotions = []
# def user_answer():
#     # Create a ThreadPoolExecutor with a specified number of worker threads
#     with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:

#         record_ex = executor.submit(record.record)
#         facial_ex = executor.submit(facial2.gen_frames)

#         concurrent.futures.wait([facial_ex, record_ex])   


# user_answer()


def get_mic_input():
    record.record()

# recorded speech to text
def record_to_text():
    return speech.speech_to_text("rizzai/output_audio.wav")
    

# get_mic_input()
# print(record_to_text)
# speech.speech_to_text("HaqckTheNorth23/rizzai/output_audio.wav")q
# print(facial_emotions)