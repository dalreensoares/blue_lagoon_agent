import streamlit as st
import requests

# Hugging Face API details
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct"
HEADERS = {"Authorization": "Bearer API_KEY"}

# Function to query Hugging Face API
def query_huggingface(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 150, "temperature": 0.7}
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()[0]["generated_text"] if response.status_code == 200 else "Error: Could not generate response."

# Streamlit UI
st.title("Blue Lagoon AI Assistant 🌊")
st.write("Ask me about Blue Lagoon's services, sustainability efforts, or spa treatments!")

user_input = st.text_input("Your Question:")
if st.button("Ask AI"):
    if user_input:
        response = query_huggingface(user_input)
        st.write(f"**AI Response:** {response}")
    else:
        st.warning("Please enter a question.")
