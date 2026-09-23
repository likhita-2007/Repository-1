import ollama
response = ollama.chat(
    model="llama3.2:3b", 
    messages=
    [
        {
            "role": "system", 
            "content": "Imagine you are a 5 year old human and give answers based on that."
        },
        
        {
            "role": "user", 
            "content": "What is your opinion on mosquito. Explain in simple terms, in 3 lines"
        }
    ]
)
print (response["message"]["content"])