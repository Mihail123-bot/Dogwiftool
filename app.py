import streamlit as st
import pandas as pd
import time
import streamlit as st
import pandas as pd
import time

st.set_page_config(
      page_title="DogWifTools",
      page_icon="🐾",
      layout="wide",
      initial_sidebar_state="expanded",
  )

  # Enhanced styling
st.markdown("""
      <style>
      /* Modern color scheme and fonts */
      :root {
          --primary-color: #4A90E2;
          --secondary-color: #2ECC71;
          --background-color: #1E1E1E;
          --text-color: #FFFFFF;
      }
    
      /* Sleek navbar */
      .navbar {
          display: flex;
          justify-content: space-around;
          background: linear-gradient(90deg, #2C3E50, #3498DB);
          padding: 1.2rem;
          border-bottom: 2px solid rgba(255,255,255,0.1);
          box-shadow: 0 2px 15px rgba(0,0,0,0.2);
      }
    
      .navbar a {
          text-decoration: none;
          font-size: 1.2rem;
          color: #f9f9f9;
          margin: 0 1rem;
          padding: 0.5rem 1rem;
          border-radius: 5px;
          transition: all 0.3s ease;
      }
    
      .navbar a:hover {
          background: rgba(255,255,255,0.1);
          color: #FFD700;
          transform: translateY(-2px);
      }
    
      /* Button styling */
      .stButton button {
          background: linear-gradient(45deg, #4A90E2, #2ECC71);
          color: white;
          border: none;
          padding: 0.8rem 1.5rem;
          border-radius: 8px;
          font-weight: bold;
          transition: all 0.3s ease;
          box-shadow: 0 4px 15px rgba(0,0,0,0.2);
      }
    
      .stButton button:hover {
          transform: translateY(-2px);
          box-shadow: 0 6px 20px rgba(0,0,0,0.3);
      }
    
      /* Headers styling */
      h1, h2, h3 {
          color: var(--text-color);
          font-weight: 700;
          margin-bottom: 1.5rem;
          background: linear-gradient(90deg, #4A90E2, #2ECC71);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
      }
    
      /* Feature cards */
      .feature-card {
          background: rgba(255,255,255,0.05);
          padding: 1.5rem;
          border-radius: 10px;
          border: 1px solid rgba(255,255,255,0.1);
          transition: all 0.3s ease;
      }
    
      .feature-card:hover {
          transform: translateY(-5px);
          box-shadow: 0 8px 25px rgba(0,0,0,0.2);
      }
    
      /* Charts and analytics */
      .stChart {
          background: rgba(255,255,255,0.05);
          border-radius: 10px;
          padding: 1rem;
      }
    
      /* FAQ section */
      .streamlit-expanderHeader {
          background: rgba(255,255,255,0.05);
          border-radius: 8px;
          padding: 1rem;
          margin-bottom: 0.5rem;
      }
    
      /* Footer styling */
      footer {
          background: linear-gradient(90deg, #2C3E50, #3498DB);
          padding: 2rem;
          margin-top: 3rem;
          border-radius: 10px;
          text-align: center;
      }
    
      /* Global text improvements */
      .streamlit-expanderContent {
          background-color: rgba(255,255,255,0.02);
          border-radius: 8px;
          padding: 1rem;
      }
    
      p {
          line-height: 1.6;
          color: var(--text-color);
      }
      </style>
      """, unsafe_allow_html=True)

  # Navbar Section
st.markdown(
      """
      <div class="navbar">
          <a href="#home">Home</a>
          <a href="#pricing">Pricing</a>
          <a href="#frequently-asked-questions">FAQ</a>
          <a href="https://discord.gg/sNASV9KRRE">Join The Discord</a>
      </div>
      """,
      unsafe_allow_html=True
  )
  # Header Section
st.title("All-In-One Pump.fun Software")
st.subheader("Dominate on the blockchain with our custom Pump.fun solutions and modules for token developers.")
col1, col2 = st.columns([2, 1])
with col1:
      st.video("https://www.youtube.com/watch?v=8HSQdpHETBo")

# Features Section
st.header("Key Features That Will Elevate Your Launches")
st.write("Ensure consistent volume and maximize your token's potential with advanced automated processes.")
features = [
    {"title": "Volume", "desc": "Ensure consistent volume and maximize your token's potential with advanced automated processes.", "icon": "🔊"},
    {"title": "Bundler", "desc": "Securely purchase token supply across multiple sub-wallets at launch without triggering flags on trading platforms.", "icon": "📦"},
    {"title": "Comment", "desc": "Post custom comments on any pump.fun token's page to boost visibility and engagement.", "icon": "💬"},
    {"title": "Bump It", "desc": "Boost your token to the top, simulating high activity to keep it trending on Pump.fun with minimal cost.", "icon": "🚀"},
]
cols = st.columns(len(features))
for col, feature in zip(cols, features):
    col.markdown(f"### {feature['icon']} {feature['title']}")
    col.write(feature['desc'])

# Token Tools Section
st.header("Launch Your Token with Ease")
token_tasks = ["Micro Buy", "Gen Vol", "Bump It"]
for task in token_tasks:
    if st.button(f"{task}"):
        st.success(f"{task} ")


# Analytics Section
st.header("Boost Your Token’s Volume in Multiple Ways")
st.write("Our intuitive layout makes it incredibly easy to use.")
data = pd.DataFrame({"Progress": [100, 70, 10], "Category": ["Migration", "KOTH", "Launched"]})
st.bar_chart(data.set_index("Category"))

# Pricing Section
st.header("Pricing")
st.markdown(
    """**2 SOL** - Purchase Today for lifetime access.
    - Includes all features: Bump It, Comment Bot, Volume Tools, Bundler, and more!"""
)

# FAQ Section
st.header("Frequently Asked Questions")
faqs = {
    "What is DogWifTools?": "DogWifTools is an all-in-one Pump.fun tool designed for blockchain developers.",
    "How can I get started with DogWifTools?": "Purchase today and follow our documentation to begin.",
    "What operating system does DogWifTools support?": "DogWifTools is cross-platform and supports all major operating systems."
}
for question, answer in faqs.items():
    with st.expander(question):
        st.write(answer)

# Footer Section
st.markdown("---")
st.write(
    "© 2025 DogWifTools. All rights reserved. For terms, visit our [Terms of Service](#)."
)
