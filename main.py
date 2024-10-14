import pandas as pd
import streamlit as st
import pickle
import xgboost as xgb


def load_model(filename: str = "sxgradient_boost_model"):
    try:
        with open(f'models\{filename}.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        print(f"Model file '{filename}.pkl' not found.")


def get_input_data():

    pass


def predict_depression(input_data: dict, model):

    input_df = pd.DataFrame(input_data)
    prediction = model.predict(input_df)

    return prediction[0]


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

    input_data = {
        'future_career_concerns': [carrer_concerns_options.index(carreer_concerns)],
        'study_load': [study_load_options.index(study_load)],
        'teacher_student_relationship': [teacher_student_relationship_options.index(teacher_student_relationship)],
        'sleep_quality': [sleep_quality_options.index(sleep_quality)],
        'academic_performance': [academic_performance_options.index(academic_performance)],
        'stress_level': [stress_level_options.index(stress_level)],
    }

    # depression = predict_depression(input_data=input_data, model=load_model())
    depression = predict_depression(input_data=input_data)
    if depression < 5:
        st.write(f"{depression:.4} PHQ9 Scale - Minimal Depression")
    
    elif depression >= 5 and depression < 10:
        st.write(f"{depression:.4} PHQ9 Scale - Mild Depression")
    
    elif depression >= 10 and depression < 15:
        st.write(f"{depression:.4} PHQ9 Scale - Moderate Depression")
    
    elif depression >= 15 and depression < 20:
        st.write(f"{depression:.4} PHQ9 Scale - Moderately Severe Depression")
    
    elif depression >= 20 and depression <= 27:
        st.write(f"{depression:.4} PHQ9 Scale - Severe Depression")
    
    else:
        st.write(f"{depression:.4} PHQ9 Scale - Unknown")

    # input_data = {
    #     'future_career_concerns': [2],
    #     'study_load': [2],
    #     'teacher_student_relationship': [5],
    #     'sleep_quality': [4],
    #     'academic_performance': [3],
    #     'stress_level': [4],
    # }
