import streamlit as st
from dotenv import load_dotenv
import os
import openai
from openai import OpenAI



 
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")  

st.title("Story Generator")
prompt = st.text_input("write a story")
genres = st.selectbox("Tone:", ["Fiction", "NonFiction", "Sci-Fi", "Horror", "Romance", "Comedy", "Thriller", "Mystery", "Fantasy", "Historical"])
if st.button("Generate Story"):
   if prompt:
    with st.spinner("Generate Story"):
      system_msg= {"role": "system",
                   "content": f" Write a {genres.lower()}  story based on: {prompt}. Include **Title:** line."
                   } 
      user_msg = {"role": "user", "content": prompt} 
      messages = [system_msg, user_msg]
      client = OpenAI()
      response = client.chat.completions.create(model="gpt-4.1-mini", messages=messages)
      email = response.choices[0].message.content
    st.markdown(email)
else:
  st.warning("Enter a description first!")s
