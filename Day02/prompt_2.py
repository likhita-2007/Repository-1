import ollama
response = ollama.chat(
    model="llama3.2:3b", 
    messages=[
        {
            "role": "user", 
            "content": "Find a Startup in India with no clear product and strategy, but has raised a lot of money."
        }
    ]
)
print (response["message"]["content"])