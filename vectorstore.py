# RAG module: CSV ingestion and vector DB logic
import pandas as pd

def load_csv_to_chunks(csv_path):
    df = pd.read_csv(csv_path)
    chunks = []
    for index, row in df.iterrows():
        chunk = " | ".join([f"{col}: {row[col]}" for col in df.columns])
        chunks.append(chunk)
    return chunks

# TODO: Add embedding + FAISS/Chroma storage
