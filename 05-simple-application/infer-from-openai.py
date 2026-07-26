from openai import OpenAI

with open(r"C:\Users\user\Desktop\Shubham-AI\Shared\ey-ai-upskill-10-main\ey-ai-upskill-10-main\key-vault\huggingface\openai\api.key") as f:
    api_key = f.read().strip()

client = OpenAI(api_key=api_key)

reponse = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        { "role": "system", "content": "You are a helpful assistant"},
        { "role": "user", "content": "Tell me about quantum computing"}
    ]
)

print(reponse.choices[0].message.content)