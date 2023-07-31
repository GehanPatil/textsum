import streamlit as st
from transformers import pipeline

# Create the summarization pipeline
summarizer = pipeline("summarization")

def main():
    st.title("Text Summarization with Transformers")

    # Text input from the user
    input_text = st.text_area("Enter your article:", "")

    # Summarize the input text when the user clicks the "Summarize" button
    if st.button("Summarize"):
        if input_text:
            # Generate the summary using the summarization pipeline
            summary = generate_summary(input_text)
            st.subheader("Summary:")
            st.write(summary)
        else:
            st.warning("Please enter some text to summarize.")

def generate_summary(text):
    # Generate the summary using the summarization pipeline
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False, return_text=True)
    return summary[0]['summary_text']  # Return only the plain text summary

if __name__ == "__main__":
    main()
