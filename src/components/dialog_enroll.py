import streamlit as st
from src.database.config import supabase
from src.database.db import enroll_student_to_subject
import time



@st.dialog("Enroll in Subject")
def enroll_dialog():
  st.write("Enter the subject code to enroll in the class")
  join_code = st.text_input("Subject Code", placeholder="CS101", key="enroll_code")

  if st.button("Enroll Now", width="stretch", type="primary"):
    if join_code:
    
      # Check if subject exists
      response = supabase.table("subjects").select("*").eq("subject_code", join_code).execute()
      if response.data:
        subject = response.data[0]
        student_id = st.session_state.student_data["student_id"]

        check = supabase.table("subject_students").select("*").eq("student_id", student_id).eq("subject_id", subject["subject_id"]).execute()
        if check.data:
          st.warning("You are already enrolled in this subject.")
          
        else:
          # Enroll student in the subject
          enroll_student_to_subject(student_id, subject["subject_id"])
          st.success(f"Enrolled in {subject['name']} successfully!")
          time.sleep(2)
          st.rerun()
      else:
        st.error("Subject not found. Please check the code and try again.")

    else:
      st.warning("Please enter the subject code.")