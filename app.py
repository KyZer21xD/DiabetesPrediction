import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import joblib

st.set_page_config(
    page_title="DiaPredict",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)


@st.cache_resource
def load_model():
    return joblib.load("diabetes_model.pkl")


model = load_model()


st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(37,99,235,0.08), transparent 30%),
        radial-gradient(circle at 90% 20%, rgba(16,185,129,0.08), transparent 30%),
        #F7FAFC;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

.stApp,
.stApp p,
.stApp label {
    color: #172033;
}

.hero {
    background: linear-gradient(135deg, #172554, #2563EB);
    border-radius: 24px;
    padding: 45px 30px;
    margin-bottom: 25px;
    text-align: center;
    box-shadow: 0 15px 45px rgba(37,99,235,0.18);
}

.hero h1 {
    color: white !important;
    font-size: 52px;
    font-weight: 800;
    margin: 0;
}

.hero p {
    color: #DBEAFE !important;
    font-size: 18px;
    margin-top: 12px;
}

.section-title {
    color: #172033 !important;
    font-size: 23px;
    font-weight: 750;
    margin-top: 32px;
    margin-bottom: 15px;
}

[data-testid="stWidgetLabel"] p {
    color: #475569 !important;
    font-weight: 600;
}

[data-baseweb="select"] > div {
    border-radius: 10px !important;
}

[data-testid="stNumberInput"] input {
    border-radius: 10px !important;
}

div.stButton > button {
    width: 100%;
    height: 58px;
    border: none;
    border-radius: 14px;
    font-size: 18px;
    font-weight: 700;
    background: linear-gradient(90deg, #2563EB, #4F46E5);
    color: white;
    box-shadow: 0 8px 20px rgba(37,99,235,0.25);
    transition: all 0.2s ease;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 25px rgba(37,99,235,0.32);
    color: white;
}

[data-testid="stMetric"] {
    background: white;
    border: 1px solid #E2E8F0;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0 5px 20px rgba(15,23,42,0.05);
}

[data-testid="stMetricLabel"] {
    color: #64748B;
}

[data-testid="stMetricValue"] {
    color: #172033;
}

[data-testid="stAlert"] {
    border-radius: 14px;
}

footer {
    visibility: hidden;
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


health_map = {
    "Excellent": 1,
    "Very Good": 2,
    "Good": 3,
    "Fair": 4,
    "Poor": 5
}


education_map = {
    "Never attended school": 1,
    "Primary school": 2,
    "Secondary school": 3,
    "Higher secondary / Class 12": 4,
    "Diploma / Some college": 5,
    "Graduate or above": 6
}


income_map = {
    "Below ₹2,00,000 per year": 1,
    "₹2,00,000 – ₹3,00,000 per year": 2,
    "₹3,00,000 – ₹4,00,000 per year": 3,
    "₹4,00,000 – ₹5,00,000 per year": 4,
    "₹5,00,000 – ₹7,00,000 per year": 5,
    "₹7,00,000 – ₹10,00,000 per year": 6,
    "₹10,00,000 – ₹15,00,000 per year": 7,
    "Above ₹15,00,000 per year": 8
}


yn = {
    "No": 0,
    "Yes": 1
}


st.markdown("""
<div class="hero">
    <h1>🩺 DiaPredict</h1>
    <p>AI-Powered Early Diabetes Risk Screening</p>
    <p>Machine learning analysis using public health indicators</p>
</div>
""", unsafe_allow_html=True)


st.warning(
    "⚠️ This application is an educational screening tool and "
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
        list(age_map.keys()),
        index=4
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
        value=25.0,
        step=0.1
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
        "Smoked at Least 100 Cigarettes in Lifetime",
        ["No", "Yes"]
    )

    physical_activity = st.selectbox(
        "Physical Activity in Last 30 Days",
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
    '<div class="section-title">🧠 General Health & Background</div>',
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
        ],
        index=2
    )

    mental_health = st.slider(
        "Poor Mental Health Days (Last 30 Days)",
        min_value=0,
        max_value=30,
        value=0
    )

    no_doc_cost = st.selectbox(
        "Unable to See Doctor Due to Cost",
        ["No", "Yes"]
    )


with c2:
    physical_health = st.slider(
        "Poor Physical Health Days (Last 30 Days)",
        min_value=0,
        max_value=30,
        value=0
    )

    education_text = st.selectbox(
        "Education Level",
        list(education_map.keys()),
        index=4
    )

    income_text = st.selectbox(
        "Annual Household Income (₹)",
        list(income_map.keys()),
        index=4,
        help="Income categories have been adapted for the Indian-facing interface."
    )


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
        "Education": education_map[education_text],
        "Income": income_map[income_text]
    }])


    probability = model.predict_proba(input_data)[0][1]

    score = probability * 100


    if probability >= 0.35:

        result_html = f"""
<!DOCTYPE html>
<html>
<head>

<style>

body {{
    margin: 0;
    padding: 10px;
    background: transparent;
    font-family: Arial, Helvetica, sans-serif;
}}

.card {{
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 22px;
    padding: 35px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(15,23,42,0.08);
}}

.label {{
    color: #64748B;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 1.5px;
}}

.score {{
    color: #172033;
    font-size: 64px;
    font-weight: 800;
    margin-top: 10px;
    margin-bottom: 15px;
}}

.risk {{
    color: #DC2626;
    font-size: 25px;
    font-weight: 700;
    margin-bottom: 18px;
}}

.description {{
    color: #64748B;
    font-size: 16px;
    line-height: 1.6;
}}

.threshold {{
    display: inline-block;
    margin-top: 15px;
    padding: 8px 16px;
    border-radius: 20px;
    background: #FEE2E2;
    color: #B91C1C;
    font-size: 13px;
    font-weight: 600;
}}

</style>

</head>

<body>

<div class="card">

    <div class="label">
        MODEL RISK SCORE
    </div>

    <div class="score">
        {score:.1f}%
    </div>

    <div class="risk">
        ⚠️ Higher Screening Risk
    </div>

    <div class="description">
        Your model score is above the screening threshold.
        <br>
        Consider discussing diabetes screening with a
        qualified healthcare professional.
    </div>

    <div class="threshold">
        Screening Threshold: 35%
    </div>

</div>

</body>
</html>
"""


    else:

        result_html = f"""
<!DOCTYPE html>
<html>
<head>

<style>

body {{
    margin: 0;
    padding: 10px;
    background: transparent;
    font-family: Arial, Helvetica, sans-serif;
}}

.card {{
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 22px;
    padding: 35px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(15,23,42,0.08);
}}

.label {{
    color: #64748B;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 1.5px;
}}

.score {{
    color: #172033;
    font-size: 64px;
    font-weight: 800;
    margin-top: 10px;
    margin-bottom: 15px;
}}

.risk {{
    color: #16A34A;
    font-size: 25px;
    font-weight: 700;
    margin-bottom: 18px;
}}

.description {{
    color: #64748B;
    font-size: 16px;
    line-height: 1.6;
}}

.threshold {{
    display: inline-block;
    margin-top: 15px;
    padding: 8px 16px;
    border-radius: 20px;
    background: #DCFCE7;
    color: #15803D;
    font-size: 13px;
    font-weight: 600;
}}

</style>

</head>

<body>

<div class="card">

    <div class="label">
        MODEL RISK SCORE
    </div>

    <div class="score">
        {score:.1f}%
    </div>

    <div class="risk">
        ✅ Lower Screening Risk
    </div>

    <div class="description">
        Your model score is below the screening threshold.
        <br>
        This result does not rule out diabetes or replace
        professional screening.
    </div>

    <div class="threshold">
        Screening Threshold: 35%
    </div>

</div>

</body>
</html>
"""


    components.html(
        result_html,
        height=330,
        scrolling=False
    )


st.divider()


st.markdown("## 🤖 About the AI Model")


st.write(
    "DiaPredict uses an XGBoost machine-learning classifier trained "
    "using public health indicators from the BRFSS 2015 dataset."
)


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
        "Diabetes Recall",
        "90%"
    )


st.caption(
    "90% positive-class recall was obtained using the 0.35 "
    "screening threshold on the held-out test set."
)


st.markdown("""
### 📊 Model Information

**Algorithm:** XGBoost Classifier

**Dataset:** BRFSS 2015 Public Health Dataset

**Dataset Records:** 70,692

**Input Features:** 21

**Training/Test Split:** 80% / 20%

**Screening Threshold:** 0.35
""")


st.info(
    "The displayed model risk score should not be interpreted as the "
    "real-world probability that an individual has diabetes. "
    "The model was trained using a balanced dataset."
)


st.warning(
    "The underlying machine-learning model was trained using the "
    "U.S. BRFSS 2015 dataset. Indian-style education and income labels "
    "in this interface are adaptations for usability and do not make "
    "the underlying model India-specific."
)


st.markdown("""
---

### ⚕️ Medical Disclaimer

DiaPredict is intended for **educational and research purposes only**.

The output of this application is generated by a machine-learning model
and **does not constitute medical advice, diagnosis, or treatment**.

If you are concerned about diabetes or your health, consult a qualified
healthcare professional and use appropriate clinical testing.
""")