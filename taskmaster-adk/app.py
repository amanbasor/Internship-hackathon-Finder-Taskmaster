import streamlit as st
from orchestrator import run_opportunity_workflow
from database import save_opportunities

# Page setup
st.set_page_config(page_title="Internship-Hackathon Finds", layout="wide")

# Custom UI styling matching the reference interface
st.markdown("""
    <style>
    /* Dark Background */
    .stApp {
        background-color: #121316;
        color: #FFFFFF;
    }
    
    /* Main Title Styling */
    .main-title {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 2rem;
        color: #FFFFFF;
    }
    .main-title span {
        color: #71767B;
        font-weight: 400;
    }

    /* Column Cards */
    .agent-card {
        background-color: #202226;
        border-radius: 12px;
        padding: 20px;
        height: 220px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        border: 1px solid #2D3036;
        margin-bottom: 2rem;
    }
    .agent-header {
        width: 100%;
        display: flex;
        justify-content: space-between;
        color: #E7E9EA;
        font-weight: 500;
        font-size: 1.05rem;
        border-bottom: 1px solid #2D3036;
        padding-bottom: 10px;
    }

    /* Centered Spinner inside cards */
    .spinner-box {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
        margin-top: 15px;
    }

    /* Output Section Heading (Times New Roman) */
    .output-heading {
        font-family: "Times New Roman", Times, serif;
        font-size: 2.2rem;
        color: #FFFFFF;
        margin-top: 2rem;
        margin-bottom: 0.5rem;
        letter-spacing: 1px;
    }

    /* Output Content */
    .output-content {
        font-family: "Times New Roman", Times, serif;
        font-size: 1.15rem;
        color: #E7E9EA;
        line-height: 1.6;
        background-color: #1B1D21;
        padding: 1.5rem;
        border-radius: 8px;
        border: 1px solid #2D3036;
    }

    /* Footer Styling */
    .footer {
        text-align: center;
        color: #FFFFFF;
        font-size: 1.5rem;
        font-weight: 600;
        margin-top: 4rem;
        padding-bottom: 2rem;
    }

    /* Custom Input and Button styling */
    .stTextInput>div>div>input {
        background-color: #202226;
        color: #FFFFFF;
        border: 1px solid #2D3036;
        border-radius: 8px;
    }
    .stButton>button {
        background-color: #E7E9EA;
        color: #000000;
        font-weight: 600;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1.5rem;
    }
    .stButton>button:hover {
        background-color: #FFFFFF;
        color: #000000;
    }
    </style>
""", unsafe_allow_html=True)

# Main Title Header
st.markdown('<div class="main-title">Internship-Hackathon <span>Finds</span></div>', unsafe_allow_html=True)

# Agent Cards Layout (Shortened, 3 columns with centered spinners)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="agent-card">
            <div class="agent-header">
                <span>Agent 1: Researcher</span>
                <span>🔍</span>
            </div>
            <div class="spinner-box">
                <div class="stSpinner"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="agent-card">
            <div class="agent-header">
                <span>Agent 2: Eligibility Checker</span>
                <span>🛡️</span>
            </div>
            <div class="spinner-box">
                <div class="stSpinner"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="agent-card">
            <div class="agent-header">
                <span>Agent 3: Ranking Agent</span>
                <span>🏆</span>
            </div>
            <div class="spinner-box">
                <div class="stSpinner"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Input Controls
query = st.text_input("Enter Search Criteria:", "Find software engineering internships and hackathons open to postgraduates.")
student_id = st.text_input("Student Identifier:", "student_02")
run_btn = st.button("Run Multi-Agent Pipeline")

# Output Section
if run_btn:
    if query.strip():
        with st.spinner("Processing agents..."):
            try:
                final_result = run_opportunity_workflow(query)
                
                # Output heading in Times New Roman
                st.markdown('<div class="output-heading">OUTPUT</div>', unsafe_allow_html=True)
                st.markdown("---")
                
                # Output contents
                st.markdown(f'<div class="output-content">{final_result}</div>', unsafe_allow_html=True)
                
                # DB Sync
                try:
                    save_opportunities(student_id, final_result)
                except Exception:
                    pass
            except Exception as e:
                st.error(f"Execution Error: {e}")

# Bottom Footer
st.markdown('<div class="footer">Made by Aman</div>', unsafe_allow_html=True)