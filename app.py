import streamlit as st
import pandas as pd
import joblib

model = joblib.load("diabetes_model.pkl")

st.set_page_config(
    page_title="DiaPredict",
    page_icon="🩺",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #f5fbff 0%, #eef8f4 100%);
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

.hero {
    text-align: center;
    padding: 45px 20px;
}

.hero h1 {
    font-size: 48px;
    font-weight: 800;
    margin-bottom: 10px;
}

.hero p {
    font-size: 19px;
    color: #64748b;
}

.section-title {
    font-size: 23px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 15px;
}

.result-card {
    padding: 30px;
    border-radius: 18px;
    background: white;
    box-shadow: 0 8px 30px rgba(0,0,0,0.08);
    text-align: center;
    margin-top: 25px;
}

.risk-score {
    font-size: 55px;
    font-weight: 800;
}

.high-risk {
    color: #dc2626;
    font-size: 24px;
    font-weight: 700;
}

.low-risk {
    color: #16a34a;
    font-size: 24px;
    font-weight: 700;
}

div.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)


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

yn = {
    "No": 0,
    "Yes": 1
}


st.markdown("""
<div class="hero">

<h1>🩺 DiaPredict</h1>

<p>
AI-Powered Early Diabetes Risk Screening
</p>

<p>
Machine learning analysis using public health indicators
</p>

</div>
""", unsafe_allow_html=True)


st.warning(
    "This application is an educational screening tool and "
    "does not provide a medical diagnosis."
)


st.markdown(
    '<div class="section-title">👤 Personal Information</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:
    age = st.selectbox(
        "Age",
        list(age_map.keys())
    )

with c2:
    sex = st.selectbox(
        "Sex",
        ["Female", "Male"]
    )

with c3:
    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=70.0,
        value=25.0
    )


st.markdown(
    '<div class="section-title">❤️ Medical Information</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:
    high_bp = st.selectbox(
        "High Blood Pressure",
        ["No", "Yes"]
    )

    stroke = st.selectbox(
        "History of Stroke",
        ["No", "Yes"]
    )

with c2:
    high_chol = st.selectbox(
        "High Cholesterol",
        ["No", "Yes"]
    )

    heart = st.selectbox(
        "Heart Disease / Heart Attack",
        ["No", "Yes"]
    )

with c3:
    chol_check = st.selectbox(
        "Cholesterol Check in Last 5 Years",
        ["Yes", "No"]
    )

    diff_walk = st.selectbox(
        "Difficulty Walking",
        ["No", "Yes"]
    )


st.markdown(
    '<div class="section-title">🏃 Lifestyle</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:

    smoker = st.selectbox(
        "Smoked 100+ Cigarettes",
        ["No", "Yes"]
    )

    physical_activity = st.selectbox(
        "Regular Physical Activity",
        ["Yes", "No"]
    )

with c2:

    fruits = st.selectbox(
        "Consumes Fruit Daily",
        ["Yes", "No"]
    )

    veggies = st.selectbox(
        "Consumes Vegetables Daily",
        ["Yes", "No"]
    )

with c3:

    alcohol = st.selectbox(
        "Heavy Alcohol Consumption",
        ["No", "Yes"]
    )

    healthcare = st.selectbox(
        "Has Healthcare Coverage",
        ["Yes", "No"]
    )


st.markdown(
    '<div class="section-title">🧠 General Health</div>',
    unsafe_allow_html=True
)

c1, c2 = st.columns(2)

with c1:

    general_health_text = st.selectbox(
        "General Health",
        [
            "Excellent",
            "Very Good",
            "Good",
            "Fair",
            "Poor"
        ]
    )

    mental_health = st.slider(
        "Poor Mental Health Days (Last 30 Days)",
        0,
        30,
        0
    )

    no_doc_cost = st.selectbox(
        "Unable to See Doctor Due to Cost",
        ["No", "Yes"]
    )

with c2:

    physical_health = st.slider(
        "Poor Physical Health Days (Last 30 Days)",
        0,
        30,
        0
    )

    education = st.slider(
        "Education Level",
        1,
        6,
        4
    )

    income = st.slider(
        "Income Level",
        1,
        8,
        5
    )


health_map = {
    "Excellent": 1,
    "Very Good": 2,
    "Good": 3,
    "Fair": 4,
    "Poor": 5
}


st.write("")

predict = st.button(
    "🔍 Analyze Diabetes Risk",
    type="primary"
)


if predict:

    input_data = pd.DataFrame([{

        "HighBP": yn[high_bp],
        "HighChol": yn[high_chol],
        "CholCheck": yn[chol_check],
        "BMI": bmi,
        "Smoker": yn[smoker],
        "Stroke": yn[stroke],
        "HeartDiseaseorAttack": yn[heart],
        "PhysActivity": yn[physical_activity],
        "Fruits": yn[fruits],
        "Veggies": yn[veggies],
        "HvyAlcoholConsump": yn[alcohol],
        "AnyHealthcare": yn[healthcare],
        "NoDocbcCost": yn[no_doc_cost],
        "GenHlth": health_map[general_health_text],
        "MentHlth": mental_health,
        "PhysHlth": physical_health,
        "DiffWalk": yn[diff_walk],
        "Sex": 1 if sex == "Male" else 0,
        "Age": age_map[age],
        "Education": education,
        "Income": income

    }])

    probability = model.predict_proba(input_data)[0][1]

    score = probability * 100


    if probability >= 0.35:

        st.markdown(
            f"""
            <div class="result-card">

                <p>MODEL RISK SCORE</p>

                <div class="risk-score">
                    {score:.1f}%
                </div>

                <div class="high-risk">
                    ⚠️ Higher Screening Risk
                </div>

                <br>

                <p>
                The model score exceeded the
                35% screening threshold.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="result-card">

                <p>MODEL RISK SCORE</p>

                <div class="risk-score">
                    {score:.1f}%
                </div>

                <div class="low-risk">
                    ✅ Lower Screening Risk
                </div>

                <br>

                <p>
                The model score was below the
                35% screening threshold.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


st.divider()

st.markdown("## 🤖 About the AI Model")

m1, m2, m3 = st.columns(3)

with m1:
    st.metric(
        "Test Accuracy",
        "75.47%"
    )

with m2:
    st.metric(
        "ROC-AUC",
        "0.8304"
    )

with m3:
    st.metric(
        "Diabetes Recall*",
        "90%"
    )

st.caption(
    "*Positive-class recall obtained using the 0.35 "
    "screening threshold on the held-out test set."
)

st.markdown("""
### Model Information

**Algorithm:** XGBoost Classifier

**Dataset:** BRFSS 2015 public health data

**Records:** 70,692

**Input Features:** 21

The displayed model risk score should not be interpreted as
the real-world probability that an individual has diabetes.
""")