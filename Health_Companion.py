from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Configure Gemini
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

st.set_page_config(
    page_title="AI Health Companion",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=DM+Serif+Display&display=swap');

:root {
    --green-primary: #2E7D5A;
    --radius:        12px;
    --radius-sm:     8px;
}

/* ── Base typography ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    font-size: 16px;
}
h2, h3 {
    font-family: 'DM Serif Display', serif;
}
.stMarkdown p, .stMarkdown li, .stMarkdown span,
div[data-testid="stText"], label, .stCaption {
    font-size: 1rem !important;
}
.stTextArea label, .stTextInput label, .stFileUploader label {
    font-size: 1rem !important;
    font-weight: 500 !important;
}

/* ── Hero ── */
.hero-header {
    background: linear-gradient(135deg, #2E7D5A 0%, #1B4D38 60%, #0D2E20 100%);
    border-radius: var(--radius);
    padding: 2.5rem 2rem 2rem;
    margin-bottom: 1.75rem;
    position: relative;
    overflow: hidden;
}
.hero-header::after {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 220px; height: 220px;
    border-radius: 50%;
    background: rgba(168,213,181,0.12);
    pointer-events: none;
}
.hero-title {
    font-family: 'DM Serif Display', serif;
    font-size: 2.8rem;
    color: #FFFFFF;
    margin: 0 0 0.35rem;
    line-height: 1.15;
}
.hero-subtitle {
    font-size: 1.15rem;
    color: #A8D5B5;
    margin: 0;
    font-weight: 300;
    letter-spacing: 0.02em;
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    border-right: 1px solid rgba(46,125,90,0.18);
}
.sidebar-title {
    font-family: 'DM Serif Display', serif;
    font-size: 1.4rem;
    color: var(--green-primary);
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid var(--green-primary);
    display: block;
}

/* ── Profile chips ── */
.profile-chip {
    display: inline-flex;
    align-items: center;
    background: rgba(46,125,90,0.15);
    border: 1px solid rgba(46,125,90,0.35);
    color: var(--green-primary);
    border-radius: 20px;
    padding: 4px 12px;
    font-size: 0.85rem;
    font-weight: 500;
    margin: 3px 2px;
}

/* ── Stat card ──
   Uses Streamlit's own CSS variables so it automatically
   adapts to light AND dark mode with zero media queries.     ── */
.stat-card {
    border: 1px solid rgba(46,125,90,0.22);
    border-radius: var(--radius);
    padding: 1.1rem 1.2rem;
    margin-bottom: 0.75rem;
    background-color: var(--secondary-background-color);
}
.stat-card .stat-label {
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 0.09em;
    text-transform: uppercase;
    color: var(--green-primary);
    margin-bottom: 0.3rem;
}
.stat-card .stat-value {
    font-size: 1rem;
    line-height: 1.6;
    white-space: pre-line;
    color: var(--text-color);
}

/* ── Response card — same approach ── */
.response-card {
    border-left: 4px solid var(--green-primary);
    border-radius: 0 var(--radius) var(--radius) 0;
    background-color: var(--secondary-background-color);
    padding: 1.4rem 1.6rem;
    margin-top: 1rem;
    color: var(--text-color);
    line-height: 1.7;
}
.response-card p,
.response-card li,
.response-card h1,
.response-card h2,
.response-card h3,
.response-card strong,
.response-card span,
.response-card code {
    color: var(--text-color) !important;
}

/* ── Section divider ── */
.section-divider {
    height: 2px;
    background: linear-gradient(90deg, var(--green-primary) 0%, transparent 100%);
    border: none;
    margin: 1.5rem 0;
    border-radius: 2px;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    border-bottom: 2px solid rgba(46,125,90,0.2);
}
.stTabs [data-baseweb="tab"] {
    border-radius: var(--radius-sm) var(--radius-sm) 0 0;
    padding: 0.6rem 1.4rem;
    font-weight: 500;
    font-size: 1rem;
    border: 1px solid transparent;
    border-bottom: none;
    transition: all 0.2s ease;
}
.stTabs [aria-selected="true"] {
    background: rgba(46,125,90,0.12) !important;
    border-color: rgba(46,125,90,0.3) !important;
    color: var(--green-primary) !important;
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, #2E7D5A, #1B4D38);
    color: #fff !important;
    border: none;
    border-radius: var(--radius-sm);
    padding: 0.6rem 1.8rem;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    font-size: 1rem;
    letter-spacing: 0.02em;
    transition: opacity 0.2s ease, transform 0.15s ease;
}
.stButton > button:hover {
    opacity: 0.88;
    transform: translateY(-1px);
}
.stButton > button:active {
    transform: translateY(0);
}
.stDownloadButton > button {
    background: transparent !important;
    border: 1.5px solid var(--green-primary) !important;
    color: var(--green-primary) !important;
    border-radius: var(--radius-sm) !important;
    font-weight: 500 !important;
    transition: background 0.2s;
}
.stDownloadButton > button:hover {
    background: rgba(46,125,90,0.10) !important;
}

/* ── Inputs ── */
.stTextArea textarea, .stTextInput input {
    border-radius: var(--radius-sm) !important;
    border: 1.5px solid rgba(46,125,90,0.25) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 1rem !important;
    transition: border-color 0.2s;
}
.stTextArea textarea:focus, .stTextInput input:focus {
    border-color: var(--green-primary) !important;
    box-shadow: 0 0 0 2px rgba(46,125,90,0.12) !important;
}

/* ── File uploader ── */
.stFileUploader {
    border: 2px dashed rgba(46,125,90,0.3) !important;
    border-radius: var(--radius) !important;
    padding: 1rem !important;
    background: rgba(46,125,90,0.04) !important;
    transition: border-color 0.2s;
}
.stFileUploader:hover {
    border-color: var(--green-primary) !important;
}

/* ── Footer ── */
.app-footer {
    margin-top: 3rem;
    padding-top: 1rem;
    border-top: 1px solid rgba(46,125,90,0.15);
    text-align: center;
    font-size: 0.82rem;
    letter-spacing: 0.03em;
    color: var(--text-color);
    opacity: 0.6;
}

/* ── Misc ── */
.stSpinner > div { border-top-color: var(--green-primary) !important; }
.stSuccess, .stWarning, .stError { border-radius: var(--radius-sm) !important; }
.stImage { border-radius: var(--radius); overflow: hidden; }
</style>
""", unsafe_allow_html=True)

# ─── Session State ───────────────────────────────────────────────────────────────
if 'health_profile' not in st.session_state:
    st.session_state.health_profile = {
        'goals':        'Lose 10 pounds in 3 months\nImprove cardiovascular health',
        'conditions':   'None',
        'routines':     '30-minute walk 3x/week',
        'preferences':  'Vegetarian\nLow carb',
        'restrictions': 'No dairy\nNo nuts'
    }

# ─── Gemini helpers ──────────────────────────────────────────────────────────────
def get_gemini_response(input_prompt, image_data=None):
    model = genai.GenerativeModel('gemini-2.5-flash')
    content = [input_prompt]
    if image_data:
        content.extend(image_data)
    try:
        response = model.generate_content(content)
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        return [{"mime_type": uploaded_file.type, "data": bytes_data}]
    return None

# ─── Hero Header ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-header">
    <p class="hero-title">🌿 AI Health Companion</p>
    <p class="hero-subtitle">Personalised nutrition, meal planning & health insights — powered by AI</p>
</div>
""", unsafe_allow_html=True)

# ─── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<span class="sidebar-title">Your Health Profile</span>', unsafe_allow_html=True)

    health_goals       = st.text_area("Health Goals",         value=st.session_state.health_profile['goals'])
    medical_conditions = st.text_area("Medical Conditions",   value=st.session_state.health_profile['conditions'])
    fitness_routines   = st.text_area("Fitness Routines",     value=st.session_state.health_profile['routines'])
    food_preferences   = st.text_area("Food Preferences",     value=st.session_state.health_profile['preferences'])
    restrictions       = st.text_area("Dietary Restrictions", value=st.session_state.health_profile['restrictions'])

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    if st.button("Save Profile"):
        st.session_state.health_profile = {
            'goals':        health_goals,
            'conditions':   medical_conditions,
            'routines':     fitness_routines,
            'preferences':  food_preferences,
            'restrictions': restrictions
        }
        st.success("Profile saved!")

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.caption("PROFILE SNAPSHOT")
    chips = []
    if health_goals:                                              chips.append("Goals set")
    if medical_conditions and medical_conditions.lower()!='none': chips.append("Conditions noted")
    if fitness_routines:                                          chips.append("Active routine")
    if food_preferences:                                          chips.append("Preferences set")
    if restrictions:                                              chips.append("Restrictions set")
    st.markdown("".join(f'<span class="profile-chip">{c}</span>' for c in chips), unsafe_allow_html=True)

# ─── Tabs ───────────────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["Meal Planning", "Food Analysis", "Health Insights"])

# ── Tab 1 ── Meal Planning ───────────────────────────────────────────────────────
with tab1:
    st.subheader("Personalised Meal Planning")
    st.caption("A 7-day meal plan tailored to your goals, preferences, and restrictions.")

    col1, col2 = st.columns([3, 2], gap="large")

    with col1:
        st.markdown("**Specific requirements**")
        user_input = st.text_area(
            "extra",
            placeholder="e.g., I need quick meals for busy workdays",
            label_visibility="collapsed"
        )
        generate_clicked = st.button("Generate Meal Plan")

    with col2:
        st.markdown("**Current profile**")
        profile = st.session_state.health_profile
        for label, key in [
            ("Goals",        "goals"),
            ("Conditions",   "conditions"),
            ("Routine",      "routines"),
            ("Preferences",  "preferences"),
            ("Restrictions", "restrictions"),
        ]:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-label">{label}</div>
                <div class="stat-value">{profile[key] or '—'}</div>
            </div>""", unsafe_allow_html=True)

    if generate_clicked:
        if not any(st.session_state.health_profile.values()):
            st.warning("Complete your health profile in the sidebar first.")
        else:
            with st.spinner("Crafting your personalised meal plan…"):
                prompt = f"""
                Create a personalized meal plan based on the following health profile:
                Health Goals: {st.session_state.health_profile['goals']}
                Medical Conditions: {st.session_state.health_profile['conditions']}
                Fitness Routines: {st.session_state.health_profile['routines']}
                Food Preferences: {st.session_state.health_profile['preferences']}
                Dietary Restrictions: {st.session_state.health_profile['restrictions']}
                Additional Requirements: {user_input if user_input else 'None provided'}

                Provide:
                1. A 7-day meal plan with breakfast, lunch, dinner, and snacks
                2. Nutritional breakdown for each day (calories, macros)
                3. Contextual explanations for why each meal was chosen
                4. Shopping list organised by category
                5. Preparation tips and time-saving suggestions

                Format the output clearly with headings and bullet points.
                """
                response = get_gemini_response(prompt)

            st.subheader("Your Meal Plan")
            st.markdown(f'<div class="response-card">{response}</div>', unsafe_allow_html=True)
            st.markdown("")
            st.download_button(
                label="Download Meal Plan",
                data=response,
                file_name="personalised_meal_plan.txt",
                mime="text/plain"
            )

# ── Tab 2 ── Food Analysis ───────────────────────────────────────────────────────
with tab2:
    st.subheader("Food Image Analysis")
    st.caption("Upload a photo of your meal to get instant nutritional insights.")

    uploaded_file = st.file_uploader("Drop your food photo here", type=["jpg","jpeg","png"])

    if uploaded_file is not None:
        col_img, col_btn = st.columns([2, 1], gap="large")

        with col_img:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded food image", use_column_width=True)

        with col_btn:
            st.markdown("")
            st.markdown("**Ready to analyse?**")
            st.caption("AI will estimate calories, macros, portion sizes, and flag dietary concerns.")
            analyse = st.button("Analyse Food")

        if analyse:
            with st.spinner("Analysing nutritional content…"):
                image_data = input_image_setup(uploaded_file)
                prompt = """
                You are an expert nutritionist. Analyse this food image carefully.
                Provide:
                - Estimated calories
                - Macronutrient breakdown (protein, carbs, fat, fibre)
                - Key micronutrients present
                - Potential health benefits
                - Any concerns based on common dietary restrictions
                - Suggested portion sizes
                If the image contains multiple items, analyse each separately then summarise.
                """
                response = get_gemini_response(prompt, image_data)

            st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
            st.subheader("Analysis Results")
            st.markdown(f'<div class="response-card">{response}</div>', unsafe_allow_html=True)

# ── Tab 3 ── Health Insights ─────────────────────────────────────────────────────
with tab3:
    st.subheader("Health & Nutrition Insights")
    st.caption("Ask any health or nutrition question and get science-backed, personalised guidance.")

    health_query = st.text_input(
        "Your question",
        placeholder="e.g., How can I improve my gut health?"
    )

    if st.button("Get Insights"):
        if not health_query:
            st.warning("Please enter a health question first.")
        else:
            with st.spinner("Researching your question…"):
                prompt = f"""
                You are a certified nutritionist and health expert.
                Provide detailed, science-backed insights about: {health_query}
                Consider the user's health profile: {st.session_state.health_profile}
                Include:
                1. Clear explanation of the science
                2. Practical, actionable recommendations
                3. Relevant precautions or contraindications
                4. References to studies where applicable
                5. Suggested foods or supplements if appropriate
                Use plain language while maintaining accuracy.
                """
                response = get_gemini_response(prompt)

            st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
            st.subheader("Expert Insights")
            st.markdown(f'<div class="response-card">{response}</div>', unsafe_allow_html=True)

# ─── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="app-footer">
    AI Health Companion · For informational purposes only · Always consult a qualified healthcare professional
</div>
""", unsafe_allow_html=True)