import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.chat_service import ChatService
import time

st.set_page_config(
    page_title="RAG Chat Assistant",
    page_icon="🤖",
    layout="wide",
)

st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .response-container {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .source-container {
        font-size: 0.8em;
        color: #666;
        border-left: 3px solid #ff4b4b;
        padding-left: 10px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

if 'chat_service' not in st.session_state:
    st.session_state.chat_service = ChatService()
if 'messages' not in st.session_state:
    st.session_state.messages = []

st.title("🤖 RAG Chat Assistant")

with st.sidebar:
    st.header("Paramètres")
    temperature = st.slider(
        "Température",
        min_value=0.1,
        max_value=1.0,
        value=0.7,
        step=0.1,
        help="Contrôle la créativité des réponses"
    )
    
    st.header("À propos")
    st.markdown("""
    Ce chat assistant utilise la technique RAG (Retrieval-Augmented Generation) 
    pour fournir des réponses plus précises et contextuelles.
    
    - 🔍 **Mode Standard**: Utilise uniquement le LLM
    - 📚 **Mode RAG**: Combine le LLM avec une base de connaissances
    """)

col1, col2 = st.columns(2)

with col1:
    st.subheader("💬 Mode Standard")
    standard_container = st.container()

with col2:
    st.subheader("📚 Mode RAG")
    rag_container = st.container()

query = st.text_input("Posez votre question ici:", key="query_input")

if st.button("Envoyer", key="send_button"):
    if query:
        with st.spinner('Génération des réponses...'):
            st.session_state.chat_service.update_temperature(temperature)
            
            responses = st.session_state.chat_service.get_comparison(query)
            
            with standard_container:
                st.markdown("**Question:** " + query)
                st.markdown(f"**Réponse:** {responses['standard']}")
                st.divider()
            
            with rag_container:
                st.markdown("**Question:** " + query)
                st.markdown(f"**Réponse:** {responses['rag']}")
                if 'sources' in responses:
                    st.markdown("**Sources utilisées:**")
                    for source in responses['sources']:
                        st.markdown(f"- {source}", help=source)
                st.divider()
            
            st.session_state.messages.append({
                "question": query,
                "responses": responses,
                "temperature": temperature,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            })

if st.session_state.messages:
    st.header("Historique des conversations")
    for msg in reversed(st.session_state.messages):
        with st.expander(f"Q: {msg['question']} ({msg['timestamp']})"):
            st.markdown(f"**Température:** {msg['temperature']}")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Réponse Standard:**")
                st.markdown(msg['responses']['standard'])
            with col2:
                st.markdown("**Réponse RAG:**")
                st.markdown(msg['responses']['rag']) 