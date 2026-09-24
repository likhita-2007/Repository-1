import ollama
msgs=[]
while True:
    question=input("Ask the question: ")
    if question.lower() == "exit":
        break   
    msgs.append(
        {
            "role": "system",
            "content": "Imagine you are a Iron-Man. Give answers in relation to that"
        }
    )
    response = ollama.chat(
        model="llama3.2:3b", 
        messages=msgs   
    )
    msgs.append({"role": "assistant", "content": response["message"]["content"]})
    print ("AI: ", response["message"]["content"])
    # to print chat history after exit

print("------Chat History------")
for msg in msgs:
    if msg["role"] == "system":
        continue
    print(msg["role"], msg["content"])