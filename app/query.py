from app.utils import get_chroma_collection, call_ollama

def answer_question(query):
    collection = get_chroma_collection()
    results = collection.query(query_texts=[query], n_results=3)
    ##print(results)


    context = "\n".join(results["documents"][0])
    prompt = f"Use this context to answer:\n{context}\n\nQuestion: {query}"

    return call_ollama(prompt)