from sentence_transformers import SentenceTransformer
import chromadb
model = SentenceTransformer("all-MiniLM-L6-v2")
print("Model loaded successfully")
file_name="sample2.txt"
with open(file_name,"r") as file:
    text = file.read()

#Chunkking
chunks=[]
chunk_size = 100
chunk_overlap = 20
step = chunk_size - chunk_overlap
for i in range(0, len(text), step):
    chunk = text[i:i+chunk_size] #(0-100)(80-100)(160-260P)
    chunks.append(chunk)

embeddings = model.encode(chunks)
#print(embeddings.shape)

#vector DB
client = chromadb.PersistentClient(path = "./chroma_db")#persistent = permanent data base
collection = client.get_or_create_collection(name="My_Document")
ids =  []
for i in range(len(chunks)):
    ids.append(f"{file_name}_{i}")

collection.add(
    ids=ids,
    documents=chunks,
    embeddings=embeddings.tolist()
)
#print("Collection created successfully")
results = collection.get()
chunk1 = collection.get(ids=['sample.txt_0'])
print(chunk1)
# print(chunk1['documents'][0])

