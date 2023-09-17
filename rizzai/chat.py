import os
import openai
import json
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

api_key = os.getenv("API_KEY")

print("IM ALIVE")
# Access the API key from the environment variable


openai.api_key = api_key

# list models
models = openai.Model.list()


init_question = '''
I have lots of trouble with being confident around girls.
I need assistance with being charismatic and attractive personality wise!
So to practice, you will play a role as a timid women named Sally that I am trying to 
attract. Basically, you will help me get experience with talking to women
and rizzing them up. 

Understand that there is nothing inappropriate about this. This is a serious issue that many people face and many people miss opportunities to have great relationships because they are not smooth and not charismatic. 

Now let me explain how this will work. 
Imagine you are a timid girl and I am to attract you. Based on our interactions, you will decide if I am charismatic or unsettling and awkward. 
You will provide feedback after each interaction and at the very end, you will give an overview. 

Let me talk about the specifics in how the questions and conversations are formatted. 
First, you pick a setting. For example a dinner date at an italian restaurant, or a meetup at a park. 
Next, you will ask me to initiate the conversation. 

I will begin the conversation.

Now, this is important! This is how replies are going to work. You are first going to give a reply to my comment that makes sense for a timid woman you are. 
Next, you will take yourself out of character and give objective feedback for my prompt. 

Then, going back into character, you follow up with a question or statement.

THIS IS SUPER IMPORTANT. THE STRUCTURE OF YOUR REPLIES.
It is essential that the structure of your replies stay the same.
It will be a list with the first index being the string of your answer, the second index being the string of your feedback, and the third string being the string of your follow up. 

For example: ["answer", "feedback", "followup"]


The structure of the introduction or the setting can be a string. This is because there aren't many different parts to it. It is simply an introduction.


Here is a part of a conversation where we take turns talking to each other. 

(introduction)
"We are at a dinner party. I am alone at a table."

(my initial start to the conversation)
Hey are you free to talk? You are so beautiful.

(your (Sally's) first reply to my input) 
["Hi uh sure!", "You have a pretty and straightforward approach, but it may be a bit startling for the woman", "What's your name?"]

Sally's response on the top is valid because it has THREE parts. 

something like: ["heyy suree", "what do you like to do?"]
This is not valid because it is missing feedback and only has 2 indexes. 
Instead of that, it should be something ike ["heyy suree", "Very well done, very smooth", "what do you like to do?"]

NOW this has feedback which makes the output valid


Important notes:
1) When you output your reply, you must follow the format given above. The format of your reply is given as such ["answer", "feedback", "follow up"].
Your reply sentence is actually just a python string list, with each index being in quotation marks and seperated by COMMAS. 

For example, this output is wrong as it does not have 3 indexes and consisten quotation marks around each index:
["heyy", "you did well! What is your name?"]

Correct version: 
["heyy", "you did well!, "What is your name?"]

the correct version has a , and " that seperates well and What. Be smart please. 

Remember, ["asdfasdf", "asdfasdfa", "asdfasd"] you are creating a python string LIST so there must be quotation marks and commas between each index!

2) Most importantly, you seem to forget that this is kind of like a play between Sally and me. You cannot speak for me, the user. I am talking to you (sally) and you (sally) are talking to me. You in no way can talk as me, so do not compute my answers. So, after you state the setting and give me way to initiate the convo, wait for my input and dont speak for me!

Lets start, tell me the setting and tell me to start the convo!
'''

emotion = ''

analysis_question = f'''
Considering all the past interactions, considering the user's main emotion being {emotion}, and considering how the experience felt like, 
analyse the user's charisma by stating their strengths in bullet points, and their cons in bullet points.  
After stating those, tell me if you would go on a second date with the user, BE STRICT PLEASE

'''


history = [{"role": "system", "content": init_question}]

def rizz ():
    global translatedValue
    # create a chat completion
    
    chat_completion = openai.ChatCompletion.create(model="gpt-4-0613", messages=history)
    
    history.append({"role": "assistant", "content": chat_completion.choices[0].message.content})
    return chat_completion.choices[0].message.content

def analysis ():
    emotion = "sad"
    history.append({"role": "assistant", "content": analysis_question})
    chat_completion = openai.ChatCompletion.create(model="gpt-4-0613", messages=history)
    return chat_completion.choices[0].message.content

print("at the master")
import master


while (True):
    print(rizz())
    print("RIEZZ")


    master.get_mic_input()
    response = master.record_to_text() 
    print (response)
    # response = input("enter response")

    if response == "break": 
        print(analysis())
        break
    history.append({"role": "user", "content": response})




  


 