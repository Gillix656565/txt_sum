import streamlit as st
from transformers import pipeline

# Initialize the summarization pipeline
summarizer = pipeline('summarization')

# Set up the Streamlit app layout
st.title("Text Summarization App")
st.write("Paste your text below and get a summary!")

# Text input from the user
user_input = st.text_area("Enter text here:")

if user_input:
    # Ignore the first line of the input text
    lines = user_input.split('\n')
    filtered_input = '\n'.join(lines[1:])

    # Determine the length of the input text
    input_length = len(filtered_input.split())
    
    # Display the number of words in the input text
    st.write(f"**Number of words in original text (excluding first line):** {input_length}")

    # Allow the user to either type or slide to choose the number of words for the summary
    summary_length = st.number_input(
        "Type the number of words for the summary",
        min_value=1, 
        max_value=input_length, 
        value=input_length // 4
    )
    
    if st.button("Summarize"):
        # Generate the summary with the chosen length
        summary = summarizer(filtered_input, max_length=summary_length, min_length=summary_length // 2, do_sample=False)
        summary_text = summary[0]['summary_text']

        # Display the summary and its word count
        st.write("### Summary")
        st.write(summary_text)
        summary_word_count = len(summary_text.split())
        st.write(f"**Number of words in summary:** {summary_word_count}")
else:
    st.write("Please enter some text to summarize.")

# Check if the server is running properly
st.write("Streamlit app is running")
