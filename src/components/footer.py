import streamlit as st

def footer_home():

    st.markdown("""
    <style>

    .footer-wrap {
        display: flex;
        justify-content: center;
        margin-top: 4rem;
        margin-bottom: 1rem;
    }

    .footer {
        padding: 0.7rem 1.4rem;
        border-radius: 999px;

        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(10px);

        border: 1px solid rgba(255,255,255,0.12);

        color: rgba(255,255,255,0.75);

        font-size: 1rem;
        letter-spacing: 0.4px;

        transition: all 0.25s ease;
    }

    .footer:hover {
        transform: translateY(-2px);
        background: rgba(255,255,255,0.12);
    }

    .footer span {
        color: white;
        font-weight: 1000;
    }

    </style>

    <div class="footer-wrap">
        <div class="footer">
            Built with ambition by <span>DHRUVIL</span> • 2026
        </div>
    </div>
    
    """, unsafe_allow_html=True)