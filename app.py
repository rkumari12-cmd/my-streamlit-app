import streamlit as st

# App title
st.set_page_config(page_title="StudyMate", page_icon="📚", layout="wide")

st.title("📚 StudyMate - Your AI Learning Buddy")
st.write("Welcome to **StudyMate**, an app to help students study smarter!")

# Sidebar for navigation
menu = ["Home", "Ask a Question", "Upload Notes", "About"]
choice = st.sidebar.selectbox("Navigate", menu)

# Home page
if choice == "Home":
    st.subheader("🏠 Home")
    st.write("Use StudyMate to ask questions, upload notes, and get AI-powered study help.")

# Q&A section
elif choice == "Ask a Question":
    st.subheader("❓ Ask a Question")
    question = st.text_input("Enter your question:")
    if st.button("Get Answer"):
        # Placeholder logic (can connect to AI later)
        st.success(f"Answer for: {question}\n\n👉 This feature will use AI to generate answers.")

# Upload notes
elif choice == "Upload Notes":
    st.subheader("📂 Upload Notes")
    uploaded_file = st.file_uploader("Upload your PDF notes", type=["pdf"])
    if uploaded_file:
        st.info("✅ File uploaded successfully! (Processing feature can be added here)")

# About page
elif choice == "About":
    st.subheader("ℹ️ About StudyMate")
    st.write("StudyMate is built for hackathons to help students learn with AI.")
