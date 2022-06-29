from api import OPENAI_API_KEY
import openai
def formula(x):
    openai.api_key = OPENAI_API_KEY
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt= x,
        temperature=0.7,
        max_tokens=20
    )
    ans = response.choices[0].get('text')
    print(ans)
    

formula('whats a dog')

