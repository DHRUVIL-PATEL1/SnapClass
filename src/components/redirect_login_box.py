import streamlit as st

def box(name, img_url, width, margin):
  st.markdown(f"""
    <h2>I'm <br>{name}</h2>
    <img src='{img_url}' style='width: {width}px; margin-bottom: {margin}px'/>
  """, unsafe_allow_html=True)