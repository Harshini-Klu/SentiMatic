import streamlit as st
from textblob import TextBlob

# ========== App Configuration ==========
st.set_page_config(
    page_title="QuickSentiment AI",
    page_icon="😊",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ========== Opening Page ==========
def show_opening_page():
    st.title("Welcome to SentiMatic")
    st.markdown("""
    ## Your Intelligent Text Emotion Detector
    
    ✨ **Discover the emotional tone behind any text** with our advanced NLP technology.
    Perfect for:
    - Social media monitoring
    - Customer feedback analysis
    - Market research
    - Personal journaling
    
    ### How It Works
    1. Type or paste your text
    2. Click "Analyze Sentiment"
    3. Get instant emotional insights
    
    *Ready to begin? Navigate to "Sentiment Analyzer" in the sidebar →*
    """)
    
    if st.button("👉 Get Started Now"):
        st.session_state.page = "analyzer"
        st.rerun()

# ========== Analyzer Page ==========
def show_analyzer_page():
    st.title("🔍 Sentiment Analyzer")
    st.markdown("---")
    
    user_input = st.text_area("Type your text here:", "They ended their relationship")
    
    if st.button("Analyze Sentiment"):
        with st.spinner("🤖 AI is analyzing..."):
            analysis = TextBlob(user_input).sentiment.polarity
            
            col1, col2 = st.columns(2)
            with col1:
                if analysis > 0.1:
                    st.success(f"Positive 😊 (Score: {analysis:.2f})")
                elif analysis < -0.2:
                    st.error(f"Negative 😞 (Score: {analysis:.2f})")
                else:
                    st.info(f"Neutral 😐 (Score: {analysis:.2f})")
            
            with col2:
                st.metric("Sentiment Intensity", f"{abs(analysis)*100:.0f}%")
                
            st.progress((analysis + 1) / 2)

# ========== App Navigation ==========
if 'page' not in st.session_state:
    st.session_state.page = "opening"

# Sidebar Navigation
with st.sidebar:
    st.title("QuickSentiment AI")
    nav_choice = st.radio("Navigate to:", 
                         ["🏠 Home", "🔍 Sentiment Analyzer"],
                         index=0 if st.session_state.page == "opening" else 1)
    
    if nav_choice == "🏠 Home":
        st.session_state.page = "opening"
    else:
        st.session_state.page = "analyzer"

# Page Router
if st.session_state.page == "opening":
    show_opening_page()
else:
    show_analyzer_page()
