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
    """Gets a list of image paths from a directory."""
    if not os.path.isdir(directory):
        st.warning(f"Directory not found: {directory}. Please create it.")
        return []
    supported_formats = ['.png', '.jpg', '.jpeg', '.gif']
    return [os.path.join(directory, f) for f in os.listdir(directory) if any(f.lower().endswith(ext) for ext in supported_formats)]


# --- INJECT CUSTOM CSS FOR STYLING ---
def load_css():
    """Injects custom CSS into the Streamlit app."""
    st.markdown(f"""
    <style>
        /* --- General & Layout --- */
        .stApp {{
            background-color: #f0f2f6; /* Light gray background */
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

        /* --- Projects Section (NEW Expander Design) --- */
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
             margin-top: -0.5rem;
             padding: 1.5rem;
             box-shadow: 0 6px 10px rgba(0,0,0,0.1);
        }}

        /* --- Image Carousel --- */
        .carousel-container {{
            width: 100%;
            overflow: hidden;
            position: relative;
            border-radius: 15px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            background: #ffffff;
            padding: 20px 0;
        }}
        .carousel-container:hover .carousel-track {{
            animation-play-state: paused;
        }}
        .carousel-track {{
            display: flex;
            align-items: center; /* Vertically center images */
            animation: scroll 30s linear infinite;
        }}
        .carousel-slide {{
            flex-shrink: 0;
            height: 400px;
            padding: 0 25px;
            box-sizing: border-box;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .carousel-slide img {{
            max-height: 100%;
            max-width: none; /* Allow image to be its natural width */
            height: auto;
            width: auto;
            object-fit: contain;
            border-radius: 10px;
            transition: transform 0.3s ease;
        }}
        .carousel-slide img:hover {{
            transform: scale(1.03);
        }}
        @keyframes scroll {{
            0% {{ transform: translateX(0); }}
            100% {{ transform: translateX(-50%); }}
        }}
    </style>
    """, unsafe_allow_html=True)

# --- UI HELPER: IMAGE CAROUSEL ---
def create_image_carousel(image_dir, title):
    """Creates a scrolling image carousel from a directory of images."""
    st.header(title)
    image_paths = get_images_from_dir(image_dir)

    if not image_paths:
        st.warning(f"No images found in '{image_dir}'. Add images to display the carousel.")
        return

    b64_images = [get_image_as_base64(img) for img in image_paths if get_image_as_base64(img)]
    if not b64_images:
        return

    # Duplicate images for a seamless loop
    b64_images.extend(b64_images)
    
    # Dynamically adjust animation duration based on the number of images
    # Slower scroll for more images
    num_images = len(image_paths)
    animation_duration = num_images * 8 # 8 seconds per image
    
    slides_html = "".join([
        f'<div class="carousel-slide"><img src="data:image/png;base64,{b64_img}" alt="Carousel Image"></div>'
        for b64_img in b64_images
    ])
    
    # Unique ID to target specific carousel track with CSS
    carousel_id = f"carousel-track-{title.lower().replace(' ', '-')}"
    
    st.markdown(f"""
    <style>
        /* Set animation duration and track width specifically for this carousel */
        #{carousel_id} {{
            width: calc({len(b64_images)} * 500px); /* Estimate slide width */
            animation-duration: {animation_duration}s;
        }}
    </style>
    <div class="carousel-container">
        <div class="carousel-track" id="{carousel_id}">
            {slides_html}
        </div>
    </div>
    """, unsafe_allow_html=True)


# --- DATA ---
TECHNICAL_SKILLS = {
    "🤖 ML & AI": [
        "Model Development (Regression, Classification, Clustering)", "Generative AI & Prompt Engineering",
        "NLP (Sentiment Analysis, Topic Modeling)", "LLM Fine-tuning (GPT, Gemini)", "Agentic AI Development",
        "Statistical Analysis & Feature Engineering",
    ],
    "🧠 Frameworks": [
        "TensorFlow", "PyTorch", "Scikit-learn", "LangChain & LangGraph", "Pandas & NumPy", "Keras & OpenCV",
    ],
    "☁️ Cloud & DevOps": [
        "AWS (EC2, S3, SageMaker)", "Azure & GCP", "CI/CD (Jenkins, GitLab CI)", "Docker & Kubernetes",
    ],
    "📊 Data & BI": [
        "ETL & Data Warehousing", "Web Scraping", "Power Automate & Power Apps", "Power BI & Tableau",
    ],
    "💻 Programming": ["Python", "SQL", "JavaScript"],
}

PROJECTS = {
    "E-commerce Product Data Extraction": {
        "description": "Developed Python-based web scraping pipelines to extract product details, reviews, and recommendations from e-commerce platforms, enabling data-driven insights for competitive analysis.",
        "tech": ["Python", "Scrapy", "Pandas", "SQL"]
    },
    "AI-Powered Customer Service Chatbot": {
        "description": "Built and deployed an AI-powered chatbot using GPT models and RAG to automate customer support, resolving over <span class='metric-success'>60% <span class='metric-icon'>⬆️</span></span> of common inquiries and reducing response times by <span class='metric-success'>75% <span class='metric-icon'>⬆️</span></span>.",
        "tech": ["Python", "LangChain", "OpenAI API", "Streamlit", "Docker"]
    },
    "Automated Financial Reporting Workflow": {
        "description": "Created an automation workflow using Power Automate to streamline the generation of weekly financial reports, improving efficiency and reducing manual effort by <span class='metric-success'>90% <span class='metric-icon'>⬆️</span></span>.",
        "tech": ["Power Automate", "SharePoint", "Excel VBA"]
    },
    "Real-time Image Classification Model": {
        "description": "Developed and deployed an image classification model using CNNs in TensorFlow to classify product images from a live camera feed with an accuracy of <span class='metric-success'>94% <span class='metric-icon'>⬆️</span></span>.",
        "tech": ["TensorFlow", "Keras", "OpenCV", "AWS SageMaker"]
    }
}

# --- MAIN APP ---

# 1. Load CSS
load_css()

# 2. Header Section
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

# 3. Professional Summary
with st.container():
    st.header("✨ Professional Summary")
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

# 4. Technical Skills
with st.container():
    st.header("🛠️ Technical Skills")
    skill_tabs = st.tabs(list(TECHNICAL_SKILLS.keys()))
    
    for tab, (category, skills) in zip(skill_tabs, TECHNICAL_SKILLS.items()):
        with tab:
            skills_html = ''.join([f'<span class="skill-tag">{skill}</span>' for skill in skills])
            st.markdown(f'<div style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center;">{skills_html}</div>', unsafe_allow_html=True)

st.divider()

# 5. Professional Experience
with st.container():
    st.header("💼 Professional Experience")
    st.subheader("Data Engineer | AI/ML Specialist")
    st.write("Merkle CXM - Mumbai, India | May 2022 - present")
    st.markdown("""
    - Developed, trained, and deployed machine learning models using TensorFlow, PyTorch, and scikit-learn, improving prediction accuracy by <span class='metric-success'>15% <span class='metric-icon'>⬆️</span></span>.
    - Engineered robust data pipelines for large-scale data ingestion, reducing processing time by <span class='metric-success'>40% <span class='metric-icon'>⬆️</span></span>.
    - Designed generative AI solutions using GPT/Gemini models to automate workflows, boosting team productivity by <span class='metric-success'>40% <span class='metric-icon'>⬆️</span></span>.
    - Deployed and monitored AI/ML models on AWS, ensuring 99.9% uptime and scalability.
    - Mentored junior engineers, improving team-wide adoption of best practices in prompt engineering and model optimization.
    - Currently developing agentic AI systems using LangChain and LangGraph to reduce human interaction in complex workflows.
    """, unsafe_allow_html=True)

st.divider()

# 6. Projects Handled (NEW Interactive Section)
with st.container():
    st.header("🚀 Projects Handled")
    st.write("Click on any project title to see the details.")
    
    for title, details in PROJECTS.items():
        with st.expander(f"**{title}**"):
            st.markdown(details['description'], unsafe_allow_html=True)
            tech_html = "".join([f'<span class="skill-tag">{tech}</span>' for tech in details["tech"]])
            st.markdown(f"**Technologies Used:**<br>{tech_html}", unsafe_allow_html=True)

st.divider()

# 7. Certifications & Awards (Using the Carousel Helper)
with st.container():
    # Using columns to place carousels side-by-side on wider screens if desired,
    # but for now, we'll stack them for better readability.
    create_image_carousel(CERTIFICATIONS_DIR, "📜 Certifications")
    st.write("") # Spacer
    create_image_carousel(AWARDS_DIR, "🏆 Awards")

st.divider()

# 8. Education & Soft Skills
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.header("🎓 Education")
        st.subheader("Bachelor of Engineering in Information Technology")
        st.write("**Institution:** M.H. Saboo Siddik College of Engineering, Mumbai")
        st.write("**Graduation Year:** 2022")
        st.write("**CGPA:** 8.48 / 10.00")

    with col2:
        st.header("🤝 Soft Skills")
        st.markdown("""
        - **Leadership & Mentoring**
        - **Effective Communication**
        - **Agile & Scrum Methodologies**
        - **Creative Problem-Solving**
        - **Stakeholder Collaboration**
        """)
