import streamlit as st
import openai
import PyPDF2

# Load API key from secrets
openai.api_key = st.secrets["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"]

st.set_page_config(page_title="StudyMate", page_icon="📚", layout="wide")
st.title("📚 StudyMate - AI-Powered Learning Buddy")

menu = ["Home", "Ask AI a Question", "Upload Notes", "About"]
choice = st.sidebar.selectbox("Navigate", menu)

# Ask AI a question
if choice == "Ask AI a Question":
    st.subheader("❓ Ask StudyMate")
    user_q = st.text_input("Enter your question:")
    if st.button("Get Answer") and user_q:
        with st.spinner("Thinking..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", # or "gpt-4" if you have access
                messages=[{"role": "user", "content": user_q}]
            )
            st.success(response.choices[0].message.content)

# Upload PDF and ask questions from it
elif choice == "Upload Notes":
    st.subheader("📂 Upload Notes (PDF)")
    uploaded_file = st.file_uploader("Upload your PDF notes", type=["pdf"])
    if uploaded_file:
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

        st.text_area("Extracted Notes:", text[:1000]) # show first part

        user_q = st.text_input("Ask a question based on your notes:")
        if st.button("Ask AI") and user_q:
            with st.spinner("Analyzing your notes..."):
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a study assistant."},
                        {"role": "user", "content": f"Here are my notes:\n{text}\n\nMy question: {user_q}"}
                    ]
                )
                st.success(response.choices[0].message.content)

# About
elif choice == "About":
    st.subheader("ℹ️ About StudyMate")
    st.write("StudyMate uses AI to help students learn smarter. Upload notes, ask questions, and get instant help.")
