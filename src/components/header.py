import streamlit as st

def header_home():

  logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

  st.markdown(f"""
    <div style='display: flex; flex-direction: column; align-items: center; justify-content: center; margin-bottom: 30px; margin-top: 50px;'>
      <img src='{logo_url}' style='height: 100px; position: relative;'/>
      <h1 style='text-align: center; color: #E0E3FF; margin-bottom: 0px; margin-top: 20px; padding: 0px;'>SNAP</h1>
      <h1 style='text-align: center; color: #E0E3FF; margin-bottom: 0px; padding: 0px'>CLASS</h1>
    </div>

    """, unsafe_allow_html=True)
  
def header_dashboard():

  logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

  st.markdown(f"""
    <div style='display: flex; flex-direction: row; align-items: center; justify-content: center;'>
      <img src='{logo_url}' style='height: 80px;'/>
      <h2 style='color: #5865F2; margin-left: 10px;'>SNAP<br>CLASS</h2>
    </div>

    """, unsafe_allow_html=True)