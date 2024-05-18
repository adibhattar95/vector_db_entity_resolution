#Import Libraries
import streamlit as st
import random
import time
import os
import warnings
from sentence_transformers  import SentenceTransformer
import pandas as pd
import numpy
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from utils import Frontend
warnings.filterwarnings("ignore")


st.title("VEER")
st.write("*Vector Enabled Entity Resolution*")

if "messages" not in st.session_state:
    st.session_state.messages = []


# Button to trigger clearing
if st.button("Clear Session State"):
    Frontend.clear_session_state()

        
@st.cache_data  # Allow mutation for dataframes
def load_data():
    veer_df = pd.read_csv("datasets/entity_pairs.csv")
    return veer_df

# Use st.cache with show_spinner=False to cache the SentenceTransformer model
@st.cache_resource(show_spinner=True)  # Avoid spinner for model loading
def load_model():
    encoder = SentenceTransformer('all-MiniLM-L6-v2')
    client = QdrantClient(host="localhost", port=6333)
    return encoder, client


# Accept user input
veer_df = load_data()
encoder, client = load_model()

@st.cache_data
def find_matchers_veer(entity_id):
    query_str=veer_df[veer_df['ID'] == entity_id]['entity'].values[0]
    hits = client.search(collection_name="entities",query_vector=encoder.encode(query_str).tolist(),limit=10)
    attributes = []
    entity_ids = []
    score = []
    matched_df = pd.DataFrame()
    for hit in hits:
            if hit.score > 0.7:
                if hit.payload['entity_id'] != entity_id:
                    attributes.append(hit.payload['attributes'])
                    entity_ids.append(hit.payload['entity_id'])
                    score.append(round(hit.score, 6))
    matched_df['entity_id'] = entity_ids
    matched_df['combined_attribute'] = attributes
    matched_df['score'] = score
    return matched_df,query_str


def match_entity_id(prompt):
    temp=[m["entity_id"] for m in st.session_state.messages]
    if prompt not in temp:
        matched_df,query_str = find_matchers_veer(prompt)
        st.session_state.messages.append({"role": "1","master_attr":query_str,"entity_id":prompt,"title1":f"Master Entity ID-{prompt}","title2":"*VEER* Matching Records","title3":"*FERN* Matching Records" ,"veer_rslt":matched_df})
    else:
        for i in st.session_state.messages:
            if i["entity_id"]==prompt:
                st.session_state.messages.append(i)
                break
    
        

if prompt := st.chat_input("Input Entity Id?"):
    # Display user message in chate df to  message container
    lst=prompt.split(" ")
    match_entity_id(lst[-1])
    st.empty()
    Frontend.displayMessages()