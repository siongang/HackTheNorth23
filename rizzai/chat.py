import os
import openai
import json


# Access the API key from the environment variable
# openai_key = os.getenv("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")

openai.api_key = "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"

# list models
models = openai.Model.list()


def question (question):
    global translatedValue
    # create a chat completion
    chat_completion = openai.ChatCompletion.create(model="gpt-4-0613", messages=[{"role": "user", "content": question}])
    return chat_completion.choices[0].message.content


while (True):
    question = input("enter question")
    if (question) == "break": break
    print(question(input))

 