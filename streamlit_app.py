import streamlit as st
import os

st.set_page_config(layout = "wide")

with st.sidebar:
  DOCS_DIR = os.path.abspath("./uploaded_docs")
  if not os.path.exists(DOCS_DIR):
    os.makedirs(DOCS_DIR)
  st.subheader("Add to my Knowledge Base")
  with st.form("my-form", clear_on_submit = True):
    uploaded_files = st.file_uploader("Upload a file to the Knowledge Base:", accept_multiple_files = True)
    submitted = st.form_submit_button("Upload!")

  if uploaded_files and submitted:
    for uploaded_file in uploaded_files:
      st.success(f"File {uploaded_file.name} uploaded successfully")
      with.open(os.path.join(DOCS_DIR, uploaded_file.name), "wb") as f:
        f.write(uploaded_file.read())
    
  
