#### Take ii
### The best code I work on it so far 

import openai


name = "Soll"
def askGPT(text):
    openai.api_key = "sk-"
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = text,
        temperature = 0.6,
        max_tokens = 150,
    )
    return print(response.choices[0].text)

def main():
    while True:
        print('ai: what do you want to ask about today!!!\n'+name)  
        myQn = input()
        askGPT(myQn)
        print('\n')

main()
