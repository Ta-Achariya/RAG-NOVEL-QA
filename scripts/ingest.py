


from app.utils import extract_text_from_pdf, chunk_text, embed_chunks, get_chroma_collection
print("\neieie\n")
import os


pdf_dir = "data"
collection = get_chroma_collection()

for filename in os.listdir(pdf_dir):
    if filename.endswith(".pdf"):
        path = os.path.join(pdf_dir, filename)
        text = extract_text_from_pdf(path)
        chunks = chunk_text(text)
        embeddings = embed_chunks(chunks)
        ids = [f"{filename}_{i}" for i in range(len(chunks))]
        collection.add(
            documents=chunks,
            embeddings=embeddings,
            ids=ids,
            metadatas=[{"source": filename}] * len(chunks)
        )

print("complete")