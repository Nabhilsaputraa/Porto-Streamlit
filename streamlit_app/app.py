import streamlit as st
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import seaborn as sns
from dotenv import load_dotenv
import os

#! config 
st.set_page_config(
    layout="wide",
    page_title="Gilang Nabhil - Portfolio & House Price Prediction",
    initial_sidebar_state="collapsed",
    page_icon="🏊"
)

#! Api
load_dotenv()
API_KEY = os.getenv("API_KEY")
PREDICT_URL = "https://python-powered-mlops-from-frameworks-to-model-mo-production.up.railway.app/predict"

import streamlit as st

#! CSS
st.set_page_config(page_title="Gilang Nabhil - Portfolio", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
<style>
    /* Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* NAV */
    * {font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;}
    .stApp {background-color: #ffffff;}
    .nav-container {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        padding: 2rem 4rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 1000;
        border-bottom: 1px solid rgba(0, 0, 0, 0.05);
    }
    
    .logo {
        font-size: 1rem;
        font-weight: 600;
        color: #000000;
        letter-spacing: -0.02em;
    }
    
    .nav-links {
        display: flex;
        gap: 3rem;
    }
    
    .nav-link {
        color: #000000;
        text-decoration: none;
        font-size: 0.875rem;
        font-weight: 400;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        transition: opacity 0.3s ease;
    }
    
    .nav-link:hover {
        opacity: 0.6;
    }
    
    /* Hero */
    .hero-container {
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;
        padding: 0 4rem;
        margin-top: -80px;
    }
    
    .hero-title {
        font-size: clamp(3rem, 8vw, 6.5rem);
        font-weight: 800;
        line-height: 1.1;
        color: #000000;
        margin: 0;
        letter-spacing: -0.03em;
        max-width: 1200px;
    }
    
    .case-studies {
        padding: 4rem;
        margin-top: 6rem;
    }
    
    .section-label {
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        color: #000000;
        margin-bottom: 1rem;
    }
    
    .projects-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin-top: 3rem;
    }
    
    .project-card {
        background: #f8f8f8;
        padding: 2.5rem;
        border-radius: 0px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        display: flex;
        flex-direction: column;
        height: 100%;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
    }
    
    .project-title {
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: #000000;
    }
    
    .project-desc {
        font-size: 1rem;
        color: #666666;
        line-height: 1.6;
        flex-grow: 1;
        margin-bottom: 1.5rem;
    }
    
    .project-btn {
        display: inline-block;
        padding: 0.75rem 1.5rem;
        background: #000000;
        color: #ffffff;
        text-decoration: none;
        font-size: 0.875rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        transition: background 0.3s ease;
        text-align: center;
        border: none;
        cursor: pointer;
    }
    
    .project-btn:hover {
        background: #333333;
        color: #ffffff;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .nav-container {
            padding: 1.5rem 2rem;
        }
        
        .hero-container {
            padding: 0 2rem;
        }
        
        .case-studies {
            padding: 2rem;
        }
        
        .nav-links {
            gap: 1.5rem;
        }
        
        .projects-grid {
            grid-template-columns: 1fr;
        }
    }
</style>
""", unsafe_allow_html=True)

# Nav
st.markdown("""
<div class="nav-container">
    <div class="logo">GilangNabhil</div>
    <div class="nav-links">
        <a href="#about" class="nav-link" style="color:#000000;">About</a>
        <a href="#resume" class="nav-link" style="color:#000000;">Resume</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Hero 
st.markdown("""
<div class="hero-container">
    <h1 class="hero-title">Hi, I'm Gilang Nabhil. I'm an athlete and IT student.</h1>
</div>
""", unsafe_allow_html=True)

# Projects 
st.markdown("""
<div class="case-studies">
    <div class="section-label">Projects</div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="project-card">
        <div class="project-title">Inspant.</div>
        <div class="project-desc">Unlock championship-level insights with our cutting-edge sports analytics platform. Track, analyze, and optimize athletic performance with real-time data visualization and AI-powered insights.</div>
        <a href="https://inspant.com/" target="_blank" class="project-btn">View Project</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="project-card">
        <div class="project-title">Inspant Store</div>
        <div class="project-desc">A simple e-commerce platform for Inspant, allowing users to browse and purchase analytics tools and training resources.</div>
        <a href="https://github.com/Nabhilsaputraa/Inspant---Shop" target="_blank" class="project-btn">View Project</a>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="project-card">
        <div class="project-title">House Price Prediction</div>
        <div class="project-desc">Machine learning model to predict house prices using Python and scikit-learn, providing quick insights for property evaluation.</div>
        <a href="https://github.com/Nabhilsaputraa/Python-Powered-MLOps-From-Frameworks-to-Model-Monitoring" target="_blank" class="project-btn">View Project</a>
    </div>
    """, unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

#! ML Model
st.markdown("""
<div class="case-studies">
    <div class="section-label">House Price Prediction</div>
    <h2 style="font-size: 2rem; font-weight: 700; margin: 0.5rem 0; color: #000000;">ML Model Deployment</h2>
    <p style="font-size: 0.95rem; color: #666666; margin-bottom: 1.5rem;">Upload CSV → visualize → predict using deployed ML model</p>
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload CSV file for prediction", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.markdown("""
    <div style="padding: 2rem 4rem 0 4rem;">
        <div class="section-label">Dataset Overview</div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Rows", f"{len(df):,}")
    with col2:
        st.metric("Columns", len(df.columns))
    with col3:
        st.metric("Numeric", len(df.select_dtypes(include="number").columns))
    
    with st.expander("Preview Data", expanded=False):
        st.dataframe(df.head(8), use_container_width=True, height=300)
    df = df.replace([np.inf, -np.inf], np.nan).fillna(0)
    
    # !EDA
    st.markdown("""
    <div style="padding: 1.5rem 4rem 0 4rem;">
        <div class="section-label">Exploratory Analysis</div>
    </div>
    """, unsafe_allow_html=True)
    
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    
    if numeric_cols:
        selected_feature = st.selectbox("Select feature", numeric_cols, key="dist_select")
        
        col_viz1, col_viz2, col_viz3 = st.columns(3)
        
        with col_viz1:
            fig, ax = plt.subplots(figsize=(4, 3))
            sns.histplot(df[selected_feature], kde=True, ax=ax, color="#000000", linewidth=1.5)
            ax.set_title("Distribution", fontsize=10, fontweight='600', pad=8)
            ax.set_xlabel(selected_feature, fontsize=8)
            ax.set_ylabel("Count", fontsize=8)
            ax.tick_params(labelsize=7)
            plt.tight_layout()
            st.pyplot(fig)
        
        with col_viz2:
            fig, ax = plt.subplots(figsize=(4, 3))
            sns.boxplot(y=df[selected_feature], ax=ax, color="#f8f8f8", linewidth=1.5)
            ax.set_title("Outliers", fontsize=10, fontweight='600', pad=8)
            ax.set_ylabel(selected_feature, fontsize=8)
            ax.tick_params(labelsize=7)
            plt.tight_layout()
            st.pyplot(fig)
        
        with col_viz3:
            fig, ax = plt.subplots(figsize=(4, 3))
            stats = df[selected_feature].describe()
            ax.axis('off')
            stats_text = f"""Mean: {stats['mean']:.2f}
            Median: {stats['50%']:.2f}
            Std: {stats['std']:.2f}
            Min: {stats['min']:.2f}
            Max: {stats['max']:.2f}"""
            ax.text(0.1, 0.5, stats_text, fontsize=9, verticalalignment='center', 
                   family='monospace', bbox=dict(boxstyle='round', facecolor='#f8f8f8', alpha=0.8))
            ax.set_title("Statistics", fontsize=10, fontweight='600', pad=8)
            plt.tight_layout()
            st.pyplot(fig)

        st.markdown("<br>", unsafe_allow_html=True)
        col_corr1, col_corr2 = st.columns([3, 2])
        
        with col_corr1:
            top_features = min(12, len(numeric_cols))
            selected_cols = numeric_cols[:top_features]
            
            fig, ax = plt.subplots(figsize=(7, 5))
            correlation_matrix = df[selected_cols].corr()
            sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap="RdBu_r", 
                       center=0, ax=ax, cbar_kws={'shrink': 0.7}, 
                       annot_kws={'size': 7}, linewidths=0.5)
            ax.set_title("Correlation Matrix", fontsize=11, fontweight='600', pad=10)
            ax.tick_params(labelsize=7)
            plt.tight_layout()
            st.pyplot(fig)
        
        with col_corr2:
            corr_pairs = []
            full_corr = df[numeric_cols].corr()
            for i in range(len(full_corr.columns)):
                for j in range(i+1, len(full_corr.columns)):
                    corr_pairs.append({
                        'Pair': f"{full_corr.columns[i][:8]}—{full_corr.columns[j][:8]}",
                        'Corr': full_corr.iloc[i, j]
                    })
            
            corr_df = pd.DataFrame(corr_pairs).sort_values('Corr', ascending=False, key=abs).head(8)
            
            st.markdown("<p style='font-size: 0.75rem; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.5rem;'>TOP CORRELATIONS</p>", unsafe_allow_html=True)
            st.dataframe(corr_df, hide_index=True, use_container_width=True, height=280)
    
    #! ML Prediction
    st.markdown("""
    <div style="padding: 2rem 4rem 0 4rem;">
        <div class="section-label">ML Prediction</div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Run Prediction"):
        required_columns = [
            "OverallQual","GrLivArea","GarageCars","GarageArea",
            "TotalBsmtSF","FirstFlrSF","FullBath","TotRmsAbvGrd","YearBuilt"
        ]
        missing_cols = [c for c in required_columns if c not in df.columns]
        
        if missing_cols:
            st.error(f"Missing columns: {', '.join(missing_cols)}")
            st.stop()
        
        payload = [row for row in df[required_columns].to_dict(orient="records")]
        headers = {"x-api-key": API_KEY}
        
        with st.spinner("Calling ML API..."):
            try:
                response = requests.post(PREDICT_URL, json=payload, headers=headers, timeout=60)
            except requests.exceptions.RequestException as e:
                st.error(f"Connection error: {e}")
                st.stop()
        
        if response.status_code != 200:
            st.error(f"API Error ({response.status_code})")
            st.code(response.text)
            st.stop()
        
        result = response.json()
        
        if "predicted_prices" not in result:
            st.error("Invalid API response")
            st.json(result)
            st.stop()
        
        df["prediction"] = result["predicted_prices"]
        st.success("Prediction completed")
        
        col_m1, col_m2, col_m3, col_m4 = st.columns(4)
        with col_m1:
            st.metric("Mean", f"${df['prediction'].mean():,.0f}")
        with col_m2:
            st.metric("Median", f"${df['prediction'].median():,.0f}")
        with col_m3:
            st.metric("Min", f"${df['prediction'].min():,.0f}")
        with col_m4:
            st.metric("Max", f"${df['prediction'].max():,.0f}")
        

        col_p1, col_p2 = st.columns(2)        
        with col_p1:
            fig, ax = plt.subplots(figsize=(5.5, 3.5))
            ax.plot(df.index, df["prediction"], marker="o", linewidth=1.5, markersize=3, color="#000000")
            ax.set_title("Price Predictions", fontsize=10, fontweight='600', pad=8)
            ax.set_xlabel("Index", fontsize=8)
            ax.set_ylabel("Price ($)", fontsize=8)
            ax.tick_params(labelsize=7)
            ax.grid(True, alpha=0.2, linewidth=0.5)
            plt.tight_layout()
            st.pyplot(fig)
        
        with col_p2:
            fig, ax = plt.subplots(figsize=(5.5, 3.5))
            sns.histplot(df["prediction"], kde=True, ax=ax, color="#000000", linewidth=1.5)
            ax.set_title("Distribution", fontsize=10, fontweight='600', pad=8)
            ax.set_xlabel("Price ($)", fontsize=8)
            ax.set_ylabel("Count", fontsize=8)
            ax.tick_params(labelsize=7)
            plt.tight_layout()
            st.pyplot(fig)
        
        with st.expander("View Full Results"):
            st.dataframe(df, use_container_width=True, height=400)
        
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇Download Results", csv, "predictions.csv", "text/csv")
