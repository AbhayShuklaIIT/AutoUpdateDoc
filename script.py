import os
from googleapiclient.discovery import build
import openai
import requests

pr_title = os.getenv('PR_TITLE')
pr_body = os.getenv('PR_BODY')
pr_diff = os.getenv('PR_DIFF')
api_url = "aee9-2401-4900-883a-c826-ad65-ff97-88f7-1d66.ngrok-free.app"

def append_to_support_doc(api_url, content):
    headers = {
        'Content-Type': 'application/json'
    }
    
    data = {
        'content': content
    }
    
    try:
        response = requests.post(api_url, json=data, headers=headers)
        
        if response.status_code == 200:
            print("Content appended successfully.")
        else:
            print(f"Failed to append content. Status Code: {response.status_code}")
            print(f"Error: {response.json()}")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def read_support_doc(api_url):
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            content = response.json().get('content', '')
            print("Support Doc Content:\n")
            print(content)
        else:
            print(f"Failed to read content. Status Code: {response.status_code}")
            print(f"Error: {response.json()}")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# pr_body = ""
f = open("README.md", "r")
support_doc = f.read()

prompt = "Support doc - " + support_doc + " -Update my support doccumentation using the following PRD" + pr_body + " \n and following code change" 

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
