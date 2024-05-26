import os
from googleapiclient.discovery import build
import openai


pr_title = os.getenv('PR_TITLE')
pr_body = os.getenv('PR_BODY')
pr_diff = os.getenv('PR_DIFF')

# pr_body = ""
f = open("README.md", "r")
support_doc = f.read()

prompt = "Support doc - " + support_doc + " -Update my support doccumentation using the following PRD" + pr_body + " \n and following code change" 

# k = b'LfHKLsPWn6VvsLPcA4uuX7j5w5IB1HifiCj48sTwxs4='

# encMessage = fernet.encrypt(message.encode())

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = os.getenv("OPENAPI_KEY")

# Example function to generate a completion from the GPT model
def generate_text(prompt, model="gpt-3.5-turbo", max_tokens=4096):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response['choices'][0]['message']['content'].strip()

# Example usage
# prompt = "Tell me a joke."
result = (generate_text(prompt))

f = open("README.md", "a")
print(result)
f.write(result+"Abhay")
f.close()
