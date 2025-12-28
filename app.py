import streamlit as st
from ai_engine.summarize import summarize_text

st.header("Text Summarizer AI")

text_input=st.text_area("Enter text to summarize",height=200)

if st.button("Summarize"):
    if text_input.strip():
        with st.spinner("Summarizing text..."):
            summary=summarize_text(text_input)
            st.subheader("Summary")
            st.write(summary)
    else:
        st.warning("Please enter some text.")    

