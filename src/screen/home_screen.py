import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_base_layout, style_base_home
from src.components.redirect_login_box import box
from src.components.footer import footer_home

def home_screen():
  
  header_home()

  style_base_layout()
  style_base_home()

  col1, col2 = st.columns(2, gap="large")

  with col1:
    box("Student", "https://i.ibb.co/844D9Lrt/mascot-student.png", 120, 8)

    if st.button("Student Screen", icon=':material/arrow_outward:', icon_position="right", type="primary"):
      st.session_state["login_type"] = "student"
      st.rerun()

  with col2:
    box("Teacher", "https://i.ibb.co/CsmQQV6X/mascot-prof.png", 145, 10)

    if st.button("Teacher Screen", icon=':material/arrow_outward:', icon_position="right", type="primary"):
      st.session_state["login_type"] = "teacher"
      st.rerun()

  footer_home()