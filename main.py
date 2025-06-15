import streamlit as st
import base64
import os

# --- PATHS AND CONFIGURATION ---
# IMPORTANT: Create a folder named 'media' in the same directory as this script.
# Inside 'media', create sub-folders 'certifications' and 'awards'.
# Place your images in the appropriate folders.
MEDIA_DIR = "media"
PROFILE_PHOTO_PATH = os.path.join(MEDIA_DIR, "profile-photo.jpg")
LINKEDIN_ICON_PATH = os.path.join(MEDIA_DIR, "linkedin.png")
GMAIL_ICON_PATH = os.path.join(MEDIA_DIR, "gmail.png")
GITHUB_ICON_PATH = os.path.join(MEDIA_DIR, "github.png")
CERTIFICATIONS_DIR = os.path.join(MEDIA_DIR, "certifications")
AWARDS_DIR = os.path.join(MEDIA_DIR, "awards")


# --- PAGE CONFIG ---
st.set_page_config(layout="wide", page_title="Nizaal Khot | AI/ML Engineer")


# --- HELPER FUNCTIONS ---

def get_image_as_base64(path):
    """Encodes an image file to a base64 string for embedding in HTML/CSS."""
    if not os.path.exists(path):
        st.error(f"File not found: {path}")
        return None
    try:
        with open(path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except Exception as e:
        st.error(f"Error reading {path}: {e}")
        return None

def get_images_from_dir(directory):
    """Gets a list of image paths from a directory, excluding hidden files."""
    if not os.path.isdir(directory):
        st.warning(f"Directory not found: {directory}. Please create it.")
        return []
    supported_formats = ['.png', '.jpg', '.jpeg', '.gif']
    # Filter out hidden files (e.g., .DS_Store on macOS)
    return sorted([os.path.join(directory, f) for f in os.listdir(directory) 
                   if any(f.lower().endswith(ext) for ext in supported_formats) and not f.startswith('.')])


# --- INJECT CUSTOM CSS FOR STYLING ---
def load_css():
    """Injects custom CSS into the Streamlit app."""
    st.markdown(f"""
    <style>
        /* --- General & Layout --- */
        .stApp {{
            background-color: #f0f2f6; /* Light gray background */
            color: #333333;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #262730; /* Darker text for headers */
        }}
        .stTabs [data-baseweb="tab-list"] {{
            gap: 24px;
        }}
        .stTabs [data-baseweb="tab"] {{
            height: 50px;
            white-space: pre-wrap;
            background-color: transparent;
            border-radius: 8px;
            padding: 10px 15px;
            transition: background-color 0.2s, color 0.2s;
        }}
        .stTabs [aria-selected="true"] {{
            background-color: #FF4B4B; /* Streamlit red for selected tab */
            color: white;
            font-weight: bold;
        }}

        /* --- Header & Profile --- */
        .profile-img img {{
            width: 200px;
            height: 200px;
            border-radius: 50%;
            object-fit: cover;
            border: 5px solid #FF4B4B;
            box-shadow: 0 0 30px rgba(255, 75, 75, 0.6);
        }}
        .social-icons a {{
            margin: 0 12px;
            transition: transform 0.3s ease;
            display: inline-block;
        }}
        .social-icons a:hover {{
            transform: scale(1.25);
        }}

        /* --- Metrics & Tags --- */
        .metric-success {{
            color: #28a745;
            font-weight: bold;
        }}
        .metric-icon {{
            font-size: 1.2em;
            vertical-align: middle;
        }}
        .skill-tag {{
            display: inline-block;
            padding: 0.5em 1em;
            margin: 0.3em;
            background-color: #FF4B4B;
            color: white;
            border-radius: 16px;
            font-size: 0.9em;
            font-weight: 500;
            transition: transform 0.2s;
        }}
        .skill-tag:hover {{
            transform: scale(1.05);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}

        /* --- Expander Design (used for Projects, Experience, Education, Soft Skills, Certs/Awards) --- */
        div[data-testid="stExpander"] > div:first-child {{
            padding: 1rem;
            border-radius: 0.5rem;
            background-color: #ffffff;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.2s, box-shadow 0.2s;
            margin-bottom: 1rem;
        }}
        div[data-testid="stExpander"] > div:first-child:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 12px rgba(0,0,0,0.15);
        }}
        div[data-testid="stExpander"] .streamlit-expanderContent {{
             background-color: #ffffff;
             border-radius: 0.5rem;
             margin-top: -0.5rem; /* Adjust to bring content closer to header */
             padding: 1.5rem;
             box-shadow: 0 6px 10px rgba(0,0,0,0.1);
        }}
        div[data-testid="stExpander"] .streamlit-expanderContent > div > p {{
            margin-bottom: 0.5rem; /* Spacing for text inside expanders */
        }}

        /* --- Certifications & Awards Grid --- */
        .cert-award-item {{
            text-align: center;
            padding: 15px;
            border-radius: 10px;
            background-color: #ffffff;
            box-shadow: 0 4px 8px rgba(0,0,0,0.08);
            transition: transform 0.2s, box-shadow 0.2s;
            height: 100%; /* Ensure uniform height for expander click area */
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}
        .cert-award-item:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0,0,0,0.15);
        }}
        .cert-award-item img {{
            max-width: 100%;
            height: 150px; /* Fixed height for image previews */
            object-fit: contain; /* Ensure entire image is visible */
            border-radius: 8px;
            margin-bottom: 10px;
        }}
        .cert-award-item .stExpander {{
            border: none !important; /* Remove expander border inside item */
            box-shadow: none !important;
            margin-bottom: 0 !important;
        }}
        .cert-award-item div[data-testid="stExpander"] > div:first-child {{
            background-color: transparent;
            box-shadow: none;
            padding: 0;
            margin-bottom: 0;
        }}
        .cert-award-item div[data-testid="stExpander"] .streamlit-expanderContent {{
            background-color: #f9f9f9; /* Lighter background for content */
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.05);
            padding: 1rem;
            margin-top: 0.5rem;
            border-radius: 8px;
            text-align: left;
        }}
    </style>
    """, unsafe_allow_html=True)


# --- DATA ---
TECHNICAL_SKILLS = {
    "🤖 ML & AI": [
        "Agentic AI Development", "Generative AI & Prompt Engineering", "LLM Fine-tuning (GPT, Gemini)",
        "Model Development (Regression, Classification, Clustering)", "NLP (Sentiment Analysis, Topic Modeling)", "Statistical Analysis & Feature Engineering",
    ],
    "🧠 Frameworks": [
         "LangChain", "LangGraph", "TensorFlow", "Scikit-learn", "PyTorch", "Pandas", "NumPy", "Beautifulsoup", "Playwright", "Selenium", "Keras", "OpenCV",
    ],
    "☁️ Cloud & DevOps": [
        "AWS (EC2, S3, SageMaker)", "Microsoft Azure", "GCP", "CI/CD (Jenkins, GitLab CI)", "Docker & Kubernetes",
    ],
    "📊 Data & BI": [
        "ETL & Data Warehousing", "Web Scraping", "Power Automate & Power Apps", "Power BI & Tableau",
    ],
    "💻 Programming": ["Python", "SQL", "JavaScript"],
}

PROJECTS = {
    "E-commerce Product Data Extraction": {
        "description": "Developed Python-based web scraping pipelines to extract product details, reviews, and recommendations from e-commerce platforms, enabling data-driven insights for competitive analysis.",
        "tech": ["Python", "Beautifulsoup", "Playwright and Selenium", "Scrapy", "Pandas", "SQL"]
    },
    "AI-Powered Customer Service Chatbot": {
        "description": "Built and deployed an AI-powered chatbot using GPT models and RAG to automate customer support, resolving over <span class='metric-success'>60% <span class='metric-icon'>⬆️</span></span> of common inquiries and reducing response times by <span class='metric-success'>75% <span class='metric-icon'>⬆️</span></span>.",
        "tech": ["Python", "LangChain", "OpenAI API", "Streamlit", "Docker"]
    },
    "Automated Financial Reporting Workflow": {
        "description": "Created an automation workflow using Power Automate to streamline the generation of weekly financial reports, improving efficiency and reducing manual effort by <span class='metric-success'>90% <span class='metric-icon'>⬆️</span></span>.",
        "tech": ["Power Automate", "SharePoint"]
    },
    "Real-time Image Classification Model": {
        "description": "Developed and deployed an image classification model using CNNs in TensorFlow to classify product images from a live camera feed with an accuracy of <span class='metric-success'>94% <span class='metric-icon'>⬆️</span></span>.",
        "tech": ["TensorFlow", "Keras", "OpenCV", "AWS SageMaker"]
    }
}

# Dummy data for Certifications and Awards (replace with your actual data)
# Each item should have 'title' and 'description' keys. Image path is mandatory.
CERTIFICATIONS_DATA = [
    # {"image_path": os.path.join(CERTIFICATIONS_DIR, "cert1.png"), "title": "Generative AI Fundamentals", "description": "Completed a comprehensive course on the fundamentals of Generative AI, covering GANs, VAEs, and diffusion models."},
    {"image_path": os.path.join(CERTIFICATIONS_DIR, "aws_certified_machine_learning_specialty.png"), "title": "AWS Certified Machine Learning – Specialty", "description": "Validated expertise in building, training, tuning, and deploying machine learning models using AWS services."},
    {"image_path": os.path.join(CERTIFICATIONS_DIR, "IBM Data Science.png"), "title": "IBM Data Science Professional Certificate", "description": "Acquired proficiency in Python programming, SQL, data analysis, visualization, machine learning, and deep learning through a series of courses."},
]

AWARDS_DATA = [
    {"image_path": os.path.join(AWARDS_DIR, "RnR_Individual_Brilliance.jpg"), "title": "Individual Brilliance", "description": "Awarded for significant contributions in internal initiatives and client delivery."},
    {"image_path": os.path.join(AWARDS_DIR, "Infinity_Award_Crawl_Build_AI_Re-engineering.jpg"), "title": "Crawl Build AI Re-engineering", "description": "Awarded for significant contributions to innovative AI solution development in 2023-24."},
    {"image_path": os.path.join(AWARDS_DIR, "RnR_Meta_build_delivery_and_onboarding_team_Certificate.jpg"), "title": "Client Delivery and Onboarding", "description": "Awarded for significant contributions in team onboarding and client delivery in 2024"},
]


# --- MAIN APP ---

# 1. Load CSS
load_css()

# 2. Sidebar Navigation
st.sidebar.title("Quick Navigation")
st.sidebar.markdown("[Summary](#professional-summary)")
st.sidebar.markdown("[Skills](#technical-skills)")
st.sidebar.markdown("[Experience](#professional-experience)")
st.sidebar.markdown("[Projects](#projects-handled)")
st.sidebar.markdown("[Certifications](#certifications)")
st.sidebar.markdown("[Awards](#awards)")
st.sidebar.markdown("[Education](#education)")
st.sidebar.markdown("[Soft Skills](#soft-skills)")


# 3. Header Section
profile_pic_b64 = get_image_as_base64(PROFILE_PHOTO_PATH)
linkedin_icon_b64 = get_image_as_base64(LINKEDIN_ICON_PATH)
gmail_icon_b64 = get_image_as_base64(GMAIL_ICON_PATH)
github_icon_b64 = get_image_as_base64(GITHUB_ICON_PATH)

with st.container():
    col1, col2 = st.columns([0.3, 0.7], gap="large")
    with col1:
        if profile_pic_b64:
            st.markdown(f'<div style="text-align: center;"><div class="profile-img"><img src="data:image/png;base64,{profile_pic_b64}"></div></div>', unsafe_allow_html=True)
        else:
            st.warning("Profile photo not found. Add 'profile-photo.jpg' to the 'media' folder.")

    with col2:
        st.title("Nizaal Khot")
        st.subheader("AI/ML Engineer | Data Scientist")
        st.write("Passionate about building intelligent systems that solve real-world problems.")
        
        # Social Icons with checks
        social_icons_html = "<div class='social-icons'>"
        if linkedin_icon_b64:
            social_icons_html += f'<a href="https://linkedin.com/in/nizaalkhot" target="_blank"><img src="data:image/png;base64,{linkedin_icon_b64}" width="32"></a>'
        if github_icon_b64:
            social_icons_html += f'<a href="https://github.com/nizaalkhot" target="_blank"><img src="data:image/png;base64,{github_icon_b64}" width="32"></a>'
        if gmail_icon_b64:
            social_icons_html += f'<a href="mailto:nijaal.khot.1@gmail.com"><img src="data:image/png;base64,{gmail_icon_b64}" width="32"></a>'
        social_icons_html += "</div>"
        st.markdown(social_icons_html, unsafe_allow_html=True)

st.divider()

# 4. Professional Summary
with st.container():
    st.markdown("<h2 id='professional-summary'>👨‍💻 Professional Summary</h2>", unsafe_allow_html=True)
    st.write("""
    Results-oriented AI/ML Engineer with 3+ years of experience in developing and deploying scalable
    Machine Learning, Deep Learning, and NLP solutions. Proven track record in leading end-to-end AI
    project lifecycles, from data collection to model deployment and optimization. Expertise in leveraging
    generative AI, NLP, and LLMs for business intelligence, process automation, and predictive analytics.
    Adept at collaborating with cross-functional teams to integrate AI solutions and enhance operational
    efficiency. Passionate about driving innovation and delivering scalable, reliable solutions with a strong
    focus on quality and compliance.
    """)

st.divider()

# 5. Technical Skills
with st.container():
    st.markdown("<h2 id='technical-skills'>🛠️ Technical Skills</h2>", unsafe_allow_html=True)
    skill_tabs = st.tabs(list(TECHNICAL_SKILLS.keys()))
    
    for tab, (category, skills) in zip(skill_tabs, TECHNICAL_SKILLS.items()):
        with tab:
            skills_html = ''.join([f'<span class="skill-tag">{skill}</span>' for skill in skills])
            st.markdown(f'<div style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center;">{skills_html}</div>', unsafe_allow_html=True)

st.divider()

# 6. Professional Experience
with st.container():
    st.markdown("<h2 id='professional-experience'>💼 Professional Experience</h2>", unsafe_allow_html=True)
    with st.expander("**Data Engineer | AI/ML Specialist** - Merkle CXM, Mumbai, India | May 2022 - present"):
        st.markdown("""
        - Developed, trained, and deployed machine learning models using TensorFlow, PyTorch, and scikit-learn, improving prediction accuracy by <span class='metric-success'>15% <span class='metric-icon'>⬆️</span></span>.
        - Engineered robust data pipelines for large-scale data ingestion, reducing processing time by <span class='metric-success'>40% <span class='metric-icon'>⬆️</span></span>.
        - Designed generative AI solutions using GPT/Gemini models to automate workflows, boosting team productivity by <span class='metric-success'>40% <span class='metric-icon'>⬆️</span></span>.
        - Deployed and monitored AI/ML models on AWS, ensuring 99.9% uptime and scalability.
        - Mentored junior engineers, improving team-wide adoption of best practices in prompt engineering and model optimization.
        - Currently developing agentic AI systems using LangChain and LangGraph to reduce human interaction in complex workflows.
        """, unsafe_allow_html=True)
    # Add more experience sections using st.expander as needed

st.divider()

# 7. Projects Handled
with st.container():
    st.markdown("<h2 id='projects-handled'>🚀 Projects Handled</h2>", unsafe_allow_html=True)
    st.write("Click on any project title to see the details.")
    
    for title, details in PROJECTS.items():
        with st.expander(f"**{title}**"):
            st.markdown(details['description'], unsafe_allow_html=True)
            tech_html = "".join([f'<span class="skill-tag">{tech}</span>' for tech in details["tech"]])
            st.markdown(f"**Technologies Used:**<br>{tech_html}", unsafe_allow_html=True)

st.divider()

# 8. Certifications
with st.container():
    st.markdown("<h2 id='certifications'>📜 Certifications</h2>", unsafe_allow_html=True)
    if CERTIFICATIONS_DATA:
        # Create columns for the grid layout
        cols = st.columns(3) # Adjust number of columns as desired
        for i, cert in enumerate(CERTIFICATIONS_DATA):
            with cols[i % 3]: # Cycle through columns
                cert_img_b64 = get_image_as_base64(cert["image_path"])
                if cert_img_b64:
                    st.markdown(f"""
                    <div class="cert-award-item">
                        <img src="data:image/png;base64,{cert_img_b64}" alt="{cert['title']}">
                        <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: flex-end;">
                            <details>
                                <summary style="font-weight: bold; cursor: pointer;">{cert['title']}</summary>
                                <p>{cert['description']}</p>
                            </details>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.warning(f"Image not found for certification: {cert['title']}")
    else:
        st.info("No certifications to display. Add data to CERTIFICATIONS_DATA.")

st.divider()

# 9. Awards
with st.container():
    st.markdown("<h2 id='awards'>🏆 Awards</h2>", unsafe_allow_html=True)
    if AWARDS_DATA:
        # Create columns for the grid layout
        cols = st.columns(3) # Adjust number of columns as desired
        for i, award in enumerate(AWARDS_DATA):
            with cols[i % 3]: # Cycle through columns
                award_img_b64 = get_image_as_base64(award["image_path"])
                if award_img_b64:
                    st.markdown(f"""
                    <div class="cert-award-item">
                        <img src="data:image/png;base64,{award_img_b64}" alt="{award['title']}">
                        <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: flex-end;">
                            <details>
                                <summary style="font-weight: bold; cursor: pointer;">{award['title']}</summary>
                                <p>{award['description']}</p>
                            </details>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.warning(f"Image not found for award: {award['title']}")
    else:
        st.info("No awards to display. Add data to AWARDS_DATA.")

st.divider()

# 10. Education & Soft Skills
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h2 id='education'>🎓 Education</h2>", unsafe_allow_html=True)
        with st.expander("**Bachelor of Engineering in Information Technology**"):
            st.write("**Institution:** M.H. Saboo Siddik College of Engineering, Mumbai")
            st.write("**Graduation Year:** 2022")
            st.write("**CGPA:** 8.48 / 10.00")

    with col2:
        st.markdown("<h2 id='soft-skills'>🤝 Soft Skills</h2>", unsafe_allow_html=True)
        with st.expander("Click to see my soft skills"):
            st.markdown("""
            - **Leadership & Mentoring**
            - **Effective Communication**
            - **Agile & Scrum Methodologies**
            - **Creative Problem-Solving**
            - **Stakeholder Collaboration**
            """)