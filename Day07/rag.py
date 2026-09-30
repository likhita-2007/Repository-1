from sentence_transformers import SentenceTransformer
import chromadb
model = SentenceTransformer("all-MiniLM-L6-v2")
print("Model loaded successfullypy")
file_name="sample2.txt"
with open(file_name,"r") as file:
    text = file.read()

#Chunkking
chunks=[]
chunk_size = 100
for i in range(0, len(text), chunk_size):
    chunk = text[i:i+chunk_size]
    chunks.append(chunk)

embeddings = model.encode(chunks)

print(embeddings.shape)