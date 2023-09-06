import streamlit as st
import numpy as np
import torch
import os
import pandas as pd
import faiss
import time
from sentence_transformers import SentenceTransformer

def fetch_property_info(idx):
        df = pd.read_csv("./data/processed/VN_housing_dataset.csv")
        return df.iloc[idx]

def display_search_results(results):
        if results:
            st.subheader("Search Results:")
            for idx, property_info in enumerate(results):
                st.write(f"**Result {idx + 1}**")
                st.dataframe(property_info, width=600, height=431)  # Display property information
        else:
            st.warning("No results found.")

# Define the search function outside of Search_Property
def search(query, top_k, index, model):
    t = time.time()
    query_emb = model.encode([query], normalize_embeddings=True).astype('float32')
    top_k_res = index.search(query_emb, top_k)
    print('>>>> Results in Total Time: {}'.format(time.time() - t))
    top_k_idx = top_k_res[1][0]
    results = [fetch_property_info(idx) for idx in top_k_idx]
    return results

def Search_Property():
    st.title("Property Search 🏠")

    # Load data and create the search index
    df = pd.read_csv("./data/processed/VN_housing_dataset.csv")
    model_embedding = SentenceTransformer('keepitreal/vietnamese-sbert')
    data1 = df.address.to_list()
    data = data1[:100]
    for i in range(0, len(data)):
        data[i] = data[i].replace('\r',' ')
    encoded_data = model_embedding.encode(data, batch_size=32)
    encoded_data = np.asarray(encoded_data.astype('float32'))
    index = faiss.IndexIDMap(faiss.IndexFlatIP(768))
    index.add_with_ids(encoded_data, np.array(range(len(data))))
    use_gpu = torch.cuda.is_available()  # Check if a GPU is available
    if use_gpu:
        # Use GPU indexing if available
        res = faiss.StandardGpuResources()
        index = faiss.index_cpu_to_gpu(res, 0, faiss.IndexFlatIP(768))
    query = st.text_input("Enter your property search query:")
    search_button = st.button("Search", help="Click to start the search")
    
    if search_button:
        with st.spinner("Searching..."):
            if query:
                results = search(query, 10, index, model_embedding)
                time.sleep(2)  # Simulate a delay
                display_search_results(results)
            else:
                st.warning("Please enter a search query.")
    return
