from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

embed_model = SentenceTransformer('all-MiniLM-L6-v2')

def build_faiss_index(chunks):
    embeddings = embed_model.encode(chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return index, embeddings, chunks


def get_top_k_chunks(question, index, chunks, k=3):
    question_embedding = embed_model.encode([question])
    distances, indices = index.search(np.array(question_embedding), k)
    top_chunks = [chunks[i] for i in indices[0]]
    return "\n".join(top_chunks)