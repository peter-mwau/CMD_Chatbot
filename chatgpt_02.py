import openai

openai.api_key = "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"

messages=[]
system_msg = input("What type of chatbot would you like to create?\n\t")
messages.append({"role": "system", "content": system_msg})

print('Your chatbot assistant is Ready!')
while input != "quit()":
    user_msg = input("User: ")
    messages.append({"role": "user", "content": user_msg})
    completion  = openai.ChatCompletion.create(model='gpt-3.5-turbo',  messages=messages)
    print(completion.choices[0].message.content)
    messages.append({"role": "system", "content": completion.choices[0].message.content})





