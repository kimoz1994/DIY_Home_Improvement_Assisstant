#!/usr/bin/env python3

import streamlit as st
import pandas as pd
import minsearch
import requests
from PIL import Image
# ----------------------
# Your existing code
# ----------------------

diy_dataset = pd.read_csv('DIY_dataset/final_dataset.csv')
diy_dataset = diy_dataset.dropna(subset=['content'])
diy_dataset_dict = diy_dataset.to_dict(orient='records')

index = minsearch.Index(
    text_fields=['chapter_title','content'],
    keyword_fields=["playlist_title"]
)
index.fit(diy_dataset_dict)

def search(query):
    results = index.search(
        query=query,
        num_results=5
    )
    return results

def build_context(search_results):
    context = ""
    for doc in search_results:
        context = context  + f"playlist_title: {doc['playlist_title']}\nchapter_title:{doc['chapter_title']}\ncontent:{doc['content']}\n\n"
    return context

def build_prompt(query,context):
    user_message = query + '\n The context is:\n ' + context
    return user_message

def create_system_message():
    system_message = """youre a DIY home improvement assistant. answer the question based only on the context.

    """
    return system_message

def llm(user_message,system_message):
    #url = "http://localhost:1234/v1/chat/completions"
    url = "http://host.docker.internal:1234/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "Llama-3.2-3B-Instruct-GGUF",
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0,
        "max_tokens": -1,
        "stream": False
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()['choices'][0]['message']['content']

def answer_with_reference(search_results,answer):
    """this function adds the reference links returned from the retrieval step to the answer return from the LLM"""
    st.markdown("### Answer")
    st.write(answer)
    st.markdown("### References")
    for idx, result in enumerate(search_results):
        reference = str(idx+1)+ ' - ' + result['chapter_title'] +' - '+ result['clip_link']
        st.write(reference)

def rag(query):
    search_results = search(query)
    context = build_context(search_results)
    user_message = build_prompt(query,context)
    system_message = create_system_message()
    answer = llm(user_message,system_message)
    answer_and_reference = answer_with_reference(search_results,answer)
    return answer_and_reference

# ----------------------
# Streamlit UI
# ----------------------

image = Image.open("App_Image.png")
st.image(image, use_column_width=True)
st.title("🔧 DIY Home Improvement Assistant")

query = st.text_input("Ask your DIY question: eg. How can I fix the sink?")

if st.button("Search"):
    if query.strip():
        rag(query)
    else:
        st.warning("Please enter a question first.")
