import streamlit as st
import json
import os

# Load the data
def load_qa_data():
    data_path = "D:\SRM\LLM\LowBot_Demo\LowBot_Demo\LLM_LLJ\LLM_LLJ\data"
    qa_data = {}
    
    # Load all JSON files from the data directory
    for filename in os.listdir(data_path):
        if filename.endswith('.json'):
            with open(os.path.join(data_path, filename), 'r') as f:
                qa_data[filename.replace('_qa.json', '')] = json.load(f)
    
    return qa_data

def load_q_data():
    qa_data = {}
    for filename in os.listdir(data_path):
        if filename.endswith('_qa.json'):
            with open(os.path.join(data_path, filename), 'r', encoding='utf-8') as f:
                qa_data[filename.replace('_qa.json', '')] = json.load(f)
    return qa_data

def load_qaa_data():
    # Use a raw string for the file path to avoid issues with escape characters
    data_path = r"D:\SRM\LLM\LowBot_Demo\LowBot_Demo\LLM_LLJ\LLM_LLJ\data"
    qa_data = {}
    
    # Load all JSON files from the data directory
    for filename in os.listdir(data_path):
        if filename.endswith('.json'):
            with open(os.path.join(data_path, filename), 'r', encoding='utf-8') as f:
                qa_data[filename.replace('_qa.json', '')] = json.load(f)
    
    return qa_data


def search_qa_data(query, qa_data):
    results = []
    for source, data in qa_data.items():
        for qa_pair in data:
            if query.lower() in qa_pair['question'].lower():
                results.append({
                    'source': source,
                    'question': qa_pair['question'],
                    'answer': qa_pair['answer']
                })
    return results

# Page configuration
st.set_page_config(
    page_title="LawBot - Legal Q&A Assistant",
    page_icon="⚖️",
    layout="wide"
)

# Add custom CSS
st.markdown("""
<style>
    .main {
        background-color: #f0f2f6;
    }
    .stTitle {
        color: #1E3D59;
        font-size: 3rem !important;
        text-align: center;
        padding: 1rem;
        border-bottom: 2px solid #1E3D59;
        margin-bottom: 2rem;
    }
    .disclaimer {
        background-color: #FFE5E5;
        color: #721c24;
        padding: 1.5rem;
        border-radius: 5px;
        margin: 1rem 0;
        border: 1px solid #f5c6cb;
        font-weight: 500;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stTextInput > div > div > input {
        background-color: white;
        color: black !important;
        border: 1px solid #ccc;
    }
</style>
""", unsafe_allow_html=True)

# Add logo and title
st.markdown('<h1 class="stTitle">🏛️ LawBot</h1>', unsafe_allow_html=True)

# Add disclaimer
st.markdown('<div class="disclaimer">⚠️ <strong>Disclaimer</strong>: LawBot is for educational use only. The information provided should not be considered as legal advice. Please consult with a qualified legal professional for specific legal matters.</div>', unsafe_allow_html=True)

# Title and description
st.title("🏛️ LawBot Q&A Assistant")
st.markdown("""
This assistant helps you find answers to questions about:
- Indian Constitution
- Indian Penal Code (IPC)
- Code of Criminal Procedure (CrPC)
""")

# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Load QA data
qa_data = load_qaa_data()

# Chat interface
user_input = st.text_input("Ask your legal question:", key="user_input")

if user_input:
    # Search for relevant answers
    results = search_qa_data(user_input, qa_data)
    
    # Add user question to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    if results:
        # Add bot response to chat history
        for result in results:
            response = f"""
**Source**: {result['source'].upper()}
            
**Question**: {result['question']}

**Answer**: {result['answer']}

---
"""
            st.session_state.chat_history.append({"role": "assistant", "content": response})
    else:
        st.session_state.chat_history.append({
            "role": "assistant", 
            "content": "I couldn't find a specific answer to your question. Please try rephrasing or ask a different question."
        })

# Display chat history
st.markdown("### Chat History")
for message in st.session_state.chat_history:
    if message["role"] == "user":
        st.markdown(f"👤 **You**: {message['content']}")
    else:
        st.markdown(f"🤖 **LawBot**: {message['content']}")

# Add footer with additional disclaimer and information
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
<small>
🔍 Tool Information: This tool searches through a curated database of legal questions and answers.
Responses are based on pre-defined Q&A pairs from official legal documents.
For accurate legal advice, please consult with a qualified legal professional.
</small>
</div>
""", unsafe_allow_html=True)