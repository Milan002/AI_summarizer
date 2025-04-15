import streamlit as st
import requests
from bs4 import BeautifulSoup
import os
import google.generativeai as genai

# Set your Gemini 2.0 Flash API key here or use an environment variable
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', 'AIzaSyAfCe61__3gi7xIN_lJr-wNNXVFQyw9vL0')
genai.configure(api_key=GEMINI_API_KEY)

def fetch_webpage_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract visible text
        texts = soup.stripped_strings
        content = ' '.join(texts)
        return content[:50000]  # Limit to 50k chars for efficiency
    except Exception as e:
        return f"Error fetching content: {e}"

def summarize_content(content):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Extract the key information and generate a concise summary of the following web page content:\n{content}"
    response = model.generate_content(prompt)
    return response.text.strip()

st.title("AI Webpage Summarizer (Gemini 2.0 Flash)")
url = st.text_input("Enter a URL to summarize:")

if url:
    with st.spinner('Fetching and analyzing content...'):
        content = fetch_webpage_content(url)
        if content.startswith('Error'):
            st.error(content)
        else:
            summary = summarize_content(content)
            st.subheader("Summary:")
            st.write(summary)
