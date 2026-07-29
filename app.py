import gradio as gr
import pandas as pd
import joblib

model = joblib.load("diabetes_model.pkl")

age_map = {
    "18–24": 1,
    "25–29": 2,
    "30–34": 3,
    "35–39": 4,
    "40–44": 5,
    "45–49": 6,
    "50–54": 7,
    "55–59": 8,
    "60–64": 9,
    "65–69": 10,
    "70–74": 11,
    "75–79": 12,
    "80+": 13
}

yes_no = {
    "No": 0,
    "Yes": 1
}

def predict_diabetes(
    high_bp,
    high_chol,
    chol_check,
    bmi,
    smoker,
    stroke,
    heart_disease,
    physical_activity,
    fruits,
    veggies,
    heavy_alcohol,
    healthcare,
    no_doc_cost,
    general_health,
    mental_health,
    physical_health,
    difficulty_walking,
    sex,
    age,
    education,
    income
):

    data = pd.DataFrame([{
        "HighBP": yes_no[high_bp],
        "HighChol": yes_no[high_chol],
        "CholCheck": yes_no[chol_check],
        "BMI": bmi,
        "Smoker": yes_no[smoker],
        "Stroke": yes_no[stroke],
        "HeartDiseaseorAttack": yes_no[heart_disease],
        "PhysActivity": yes_no[physical_activity],
        "Fruits": yes_no[fruits],
        "Veggies": yes_no[veggies],
        "HvyAlcoholConsump": yes_no[heavy_alcohol],
        "AnyHealthcare": yes_no[healthcare],
        "NoDocbcCost": yes_no[no_doc_cost],
        "GenHlth": general_health,
        "MentHlth": mental_health,
        "PhysHlth": physical_health,
        "DiffWalk": yes_no[difficulty_walking],
        "Sex": 1 if sex == "Male" else 0,
        "Age": age_map[age],
        "Education": education,
        "Income": income
    }])

    probability = model.predict_proba(data)[0][1]

    score = probability * 100

    if probability >= 0.35:
        result = "⚠️ Higher Screening Risk"
    else:
        result = "✅ Lower Screening Risk"

    return result, f"{score:.1f}%"

with gr.Blocks(title="Diabetes AI Risk Screening") as app:

    gr.Markdown(
        """
        # 🩺 AI Diabetes Risk Screening

        ### Machine-learning based early diabetes risk assessment

        Enter your health information below to generate a screening risk score.

        > **Important:** This application is an educational screening tool and
        > does not provide a medical diagnosis.
        """
    )

    with gr.Row():

        with gr.Column():

            gr.Markdown("## 👤 Basic Information")

            age = gr.Dropdown(
                choices=list(age_map.keys()),
                value="25–29",
                label="Age"
            )

            sex = gr.Radio(
                ["Female", "Male"],
                value="Male",
                label="Sex"
            )

            bmi = gr.Number(
                value=25,
                label="BMI"
            )

            education = gr.Slider(
                1,
                6,
                value=4,
                step=1,
                label="Education Level"
            )

            income = gr.Slider(
                1,
                8,
                value=5,
                step=1,
                label="Income Level"
            )

        with gr.Column():

            gr.Markdown("## ❤️ Medical Information")

            high_bp = gr.Radio(
                ["No", "Yes"],
                value="No",
                label="High Blood Pressure"
            )

            high_chol = gr.Radio(
                ["No", "Yes"],
                value="No",
                label="High Cholesterol"
            )

            chol_check = gr.Radio(
                ["No", "Yes"],
                value="Yes",
                label="Cholesterol Check in Last 5 Years"
            )

            stroke = gr.Radio(
                ["No", "Yes"],
                value="No",
                label="History of Stroke"
            )

            heart_disease = gr.Radio(
                ["No", "Yes"],
                value="No",
                label="Heart Disease or Heart Attack"
            )

    with gr.Row():

        with gr.Column():

            gr.Markdown("## 🏃 Lifestyle")

            smoker = gr.Radio(
                ["No", "Yes"],
                value="No",
                label="Smoked at least 100 cigarettes"
            )

            physical_activity = gr.Radio(
                ["No", "Yes"],
                value="Yes",
                label="Physical Activity"
            )

            fruits = gr.Radio(
                ["No", "Yes"],
                value="Yes",
                label="Consumes Fruit Daily"
            )

            veggies = gr.Radio(
                ["No", "Yes"],
                value="Yes",
                label="Consumes Vegetables Daily"
            )

            heavy_alcohol = gr.Radio(
                ["No", "Yes"],
                value="No",
                label="Heavy Alcohol Consumption"
            )

        with gr.Column():

            gr.Markdown("## 🧠 General Health")

            general_health = gr.Slider(
                1,
                5,
                value=3,
                step=1,
                label="General Health (1 = Excellent, 5 = Poor)"
            )

            mental_health = gr.Slider(
                0,
                30,
                value=0,
                step=1,
                label="Poor Mental Health Days"
            )

            physical_health = gr.Slider(
                0,
                30,
                value=0,
                step=1,
                label="Poor Physical Health Days"
            )

            difficulty_walking = gr.Radio(
                ["No", "Yes"],
                value="No",
                label="Difficulty Walking"
            )

    with gr.Row():

        healthcare = gr.Radio(
            ["No", "Yes"],
            value="Yes",
            label="Healthcare Coverage"
        )

        no_doc_cost = gr.Radio(
            ["No", "Yes"],
            value="No",
            label="Unable to See Doctor Due to Cost"
        )

    predict_button = gr.Button(
        "🔍 Analyze Diabetes Risk",
        variant="primary"
    )

    gr.Markdown("## 📊 Screening Result")

    result = gr.Textbox(
        label="Risk Classification",
        interactive=False
    )

    risk_score = gr.Textbox(
        label="Model Risk Score",
        interactive=False
    )

    gr.Markdown(
        """
        ---
        ### About the Model

        **Algorithm:** XGBoost Classifier  
        **Dataset:** BRFSS 2015  
        **Records:** 70,692  
        **Features:** 21  
        **Test Accuracy:** 75.47%  
        **ROC-AUC:** 0.8304  
        **Diabetes Recall at 0.35 threshold:** 90%

        The model risk score should not be interpreted as the real-world
        probability that an individual has diabetes.
        """
    )

    predict_button.click(
        fn=predict_diabetes,
        inputs=[
            high_bp,
            high_chol,
            chol_check,
            bmi,
            smoker,
            stroke,
            heart_disease,
            physical_activity,
            fruits,
            veggies,
            heavy_alcohol,
            healthcare,
            no_doc_cost,
            general_health,
            mental_health,
            physical_health,
            difficulty_walking,
            sex,
            age,
            education,
            income
        ],
        outputs=[
            result,
            risk_score
        ]
    )

app.launch()