import pandas as pd

import streamlit as st

if __name__ == '__main__':
    
    st.set_page_config(
        page_title="Students Mental Health",
        page_icon="😊",
    )
    
    st.markdown("## Depression Prediction Model")
    st.markdown("This model predicts the probability of a student being depressed based on the following features:")

    st.markdown("Please fill in the following details to get the prediction.")


    # Carreer Concerns
    carrer_concerns_options = [ 
        "Not Concerned", 
        "Slightly Concerned",
        "Neutral",
        "Concerned",
        "Extremely Concerned"
    ]
    carreer_concerns = st.select_slider(
        "How Concerned are you about your future career?",
        options=carrer_concerns_options,
        value="Neutral",
    )
    
    # Study Load
    study_load_options = [ 
        "Very Light", 
        "Light",
        "Neutral",
        "Heavy",
        "Very Heavy"
    ]
    study_load = st.select_slider(
        "How heavy is your study load?",
        options=study_load_options,
        value="Neutral",
    )
    
    # Teacher Student Relationship
    teacher_student_relationship_options = [ 
        "Very Poor", 
        "Poor",
        "Neutral",
        "Good",
        "Very Good"
    ]
    teacher_student_relationship = st.select_slider(
        "How is your relationship with your teachers?",
        options=teacher_student_relationship_options,
        value="Neutral",
    )
    
    # Academic Performance
    academic_performance_options = [ 
        "Very Poor", 
        "Poor",
        "Neutral",
        "Good",
        "Very Good"
    ]
    academic_performance = st.select_slider(
        "How is your academic performance?",
        options=academic_performance_options,
        value="Neutral",
    )

    # Sleep Quality
    sleep_quality_options = [ 
        "Very Poor", 
        "Poor",
        "Neutral",
        "Good",
        "Very Good"
    ]
    sleep_quality = st.select_slider(
        "How is your sleep quality?",
        options=sleep_quality_options,
        value="Neutral",
    )

    # Stress Level
    stress_level_options = [ 
        "Very Low", 
        "Low",
        "Neutral",
        "High",
        "Very High"
    ]
    stress_level = st.select_slider(
        "How is your stress level?",
        options=stress_level_options,
        value="Neutral",
    )
    
    # simple_input_data = {
    #     'future_career_concerns': [2],
    #     'study_load': [2],
    #     'teacher_student_relationship': [5],
    #     'sleep_quality': [4],
    #     'academic_performance': [3],
    #     'stress_level': [4],
    # }
