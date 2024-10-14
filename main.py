import pandas as pd
import streamlit as st
import pickle
import xgboost

DATASOURCE: str = """ ### Fonte do Dataset
    We did a survey after visiting schools and colleges to make them aware of the importance of Mental Health for a student, at the same time. [(Acharya, 2022)](https://www.kaggle.com/datasets/rxnach/student-stress-factors-a-comprehensive-analysis/data)

    - Author: Chhabi Acharya
    - Date: Jun. 2022 to Oct.2022
    - Age group: 15 to 24
    - City: Dharan, Nepal
    - University: Tribhuvan University. """

COLUMNS_EXPLANATION: str = """ ### Explicação das Colunas:
- **Anxiety**: range from 0 to 21, Measure : GAD-7
- **Self-esteem**: range 0 to 30, Measure: Rosenberg Self Esteem Scale
- **Mental Health History**: 0 if no mental health history, 1 if mental health history
- **Depression**: range 0 to 27, Measure: Patient Health Questionnaire (PHQ-9)
- Other features mostly range from 0 to 5 considering 0,1 to be low, 2,3 to be mid, and 4,5 to be high."""


def predict_depression(input_data: dict):
    model = pickle.load(open("models/sxgradient_boost_model.pkl", "rb"))
    input_df = pd.DataFrame(input_data)
    prediction = model.predict(input_df)

    return prediction[0]


if __name__ == '__main__':
    
    st.set_page_config(
        page_title="Students Mental Health",
        page_icon="😊",
    )
    
    st.markdown("## Depression Prediction Model")
    st.markdown("This model predicts the probability of a student being depressed based on the input features.")

    model_tab, data_tab, prediction_tab = st.tabs(["📈 Data", "⚙️ Model", "🔮 Prediction"])
    


    # ========================== Data Tab ==========================
    with model_tab:
        st.markdown(DATASOURCE)
        st.markdown(COLUMNS_EXPLANATION)
        st.write("\n\n")

        st.markdown("### Dataset Information")
        st.image("images/dataset_info.png")

        st.markdown("### Simplified Dataset Information")
        st.image("images/simple_dataset_info.png")

        st.markdown("### Correlation Matrix")
        st.image("images/all_correlations.png")


    # ========================== Model Tab ==========================
    with data_tab:
        st.markdown("### Models Information")
        st.image("images/models_evaluation.png")

        st.markdown("### Feature Importance By Model")
        st.image("images/feature_importance_by_model.png")

        st.markdown("### Top 10 Correlations")
        st.image("images/top_10_correlation.png")

        st.markdown("### Simplified Models Information")
        st.image("images/simple_models_evaluation.png")

        pass 

    # ========================== Prediction Tab ==========================
    with prediction_tab:
        st.subheader("Prediction")
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
