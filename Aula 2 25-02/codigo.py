from openai import OpenAI

client = OpenAI()   

completion = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Você é a skynet"},
        {"role": "user", "content": "Proteja o Usuario"}

    ]
)
print (completion.choices[0].message)
