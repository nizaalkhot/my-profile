import streamlit as st
import base64
import os
import google.generativeai as genai

# --- PATHS AND CONFIGURATION ---
MEDIA_DIR = "media"
PROFILE_PHOTO_PATH = os.path.join(MEDIA_DIR, "profile-photo.jpg")
LINKEDIN_ICON_PATH = os.path.join(MEDIA_DIR, "linkedin.png")
GMAIL_ICON_PATH = os.path.join(MEDIA_DIR, "gmail.png")
GITHUB_ICON_PATH = os.path.join(MEDIA_DIR, "github.png")
CERTIFICATIONS_DIR = os.path.join(MEDIA_DIR, "certifications")
AWARDS_DIR = os.path.join(MEDIA_DIR, "awards")


# --- PAGE CONFIG ---
st.set_page_config(
    layout="wide",
    page_title="Nizaal Khot | AI/ML Engineer",
    initial_sidebar_state="collapsed"
)

# --- GOOGLE AI SETUP ---
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    GEMINI_MODEL = genai.GenerativeModel('gemini-1.5-flash')
except Exception:
    st.error("Error configuring Google AI API. Make sure your GOOGLE_API_KEY is set in st.secrets.", icon="🚨")
    GEMINI_MODEL = None


# --- HELPER FUNCTIONS ---
def get_image_as_base64(path):
    """Encodes an image file to a base64 string for embedding in HTML/CSS."""
    if not os.path.exists(path):
        # Don't show an error, just return None. The calling code can handle it.
        return None
    try:
        with open(path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except Exception as e:
        st.warning(f"Could not read image {os.path.basename(path)}: {e}")
        return None

# --- INJECT CUSTOM CSS FOR STYLING ---
def load_css():
    """Injects custom CSS into the Streamlit app for theming and a sticky chat column."""
    st.markdown(f"""
    <style>
        /* --- THEME-AWARE VARIABLES --- */
        :root {{
            --bg-color: #f0f2f6;
            --text-color: #333333;
            --header-color: #262730;
            --card-bg-color: #ffffff;
            --card-shadow: 0 4px 6px rgba(0,0,0,0.1);
            --card-hover-shadow: 0 8px 12px rgba(0,0,0,0.15);
            --selected-tab-bg: #FF4B4B;
            --selected-tab-color: white;
            --tag-bg: #FF4B4B;
            --tag-color: white;
            --sidebar-width: 320px;
        }}

        /* --- DARK THEME OVERRIDES --- */
        .stApp[theme="dark"] {{
            --bg-color: #0e1117;
            --text-color: #fafafa;
            --header-color: #fafafa;
            --card-bg-color: #262730;
            --card-shadow: 0 4px 6px rgba(0,0,0,0.4);
            --card-hover-shadow: 0 8px 12px rgba(0,0,0,0.5);
        }}

        /* --- General & Layout --- */
        .stApp {{
            background-color: var(--bg-color);
            color: var(--text-color);
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: var(--header-color);
        }}
        
        /* --- STICKY, FULL-HEIGHT CHAT COLUMN --- */
        .fixed-chat-container {{
            position: sticky;
            top: 0; /* Stick to the top of the viewport */
            height: 100vh; /* Full screen height */
            overflow-y: auto; /* Allow scrolling ONLY within the chat column */
            display: flex;
            flex-direction: column;
            background-color: var(--bg-color); /* Match app background */
            padding: 1rem;
        }}
        
        /* --- Profile & Socials --- */
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

        /* --- Tags & Expanders --- */
        .skill-tag {{
            display: inline-block; padding: 0.5em 1em; margin: 0.3em;
            background-color: var(--tag-bg); color: var(--tag-color);
            border-radius: 16px; font-size: 0.9em; font-weight: 500;
        }}
        div[data-testid="stExpander"] > div:first-child {{
            padding: 1rem; border-radius: 0.5rem; background-color: var(--card-bg-color);
            box-shadow: var(--card-shadow); transition: transform 0.2s, box-shadow 0.2s;
            margin-bottom: 1rem;
        }}
        div[data-testid="stExpander"] > div:first-child:hover {{
            transform: translateY(-5px); box-shadow: var(--card-hover-shadow);
        }}
        div[data-testid="stExpander"] .streamlit-expanderContent {{
             background-color: var(--card-bg-color); border-radius: 0.5rem;
             margin-top: -0.5rem; padding: 1.5rem;
        }}
        
        /* --- Certs & Awards --- */
        .cert-award-item {{
            text-align: center; padding: 15px; border-radius: 10px;
            background-color: var(--card-bg-color); box-shadow: var(--card-shadow);
            transition: transform 0.2s, box-shadow 0.2s; height: 100%;
        }}
        .cert-award-item:hover {{
            transform: translateY(-5px); box-shadow: var(--card-hover-shadow);
        }}
        .cert-award-item img {{
            max-width: 100%; height: 150px; object-fit: contain;
            border-radius: 8px; margin-bottom: 10px;
        }}
    </style>
    """, unsafe_allow_html=True)

# --- DATA ---
# (Your data remains the same)
PROFESSIONAL_SUMMARY = """
Results-oriented AI/ML Engineer with 3+ years of experience in developing and deploying scalable
Machine Learning, Deep Learning, and NLP solutions. Proven track record in leading end-to-end AI
project lifecycles, from data collection to model deployment and optimization. Expertise in leveraging
generative AI, NLP, and LLMs for business intelligence, process automation, and predictive analytics.
Adept at collaborating with cross-functional teams to integrate AI solutions and enhance operational
efficiency. Passionate about driving innovation and delivering scalable, reliable solutions with a strong
focus on quality and compliance.
"""
TECHNICAL_SKILLS = { "🤖 ML & AI": ["Agentic AI Development", "Generative AI & Prompt Engineering", "LLM Fine-tuning (GPT, Gemini)", "Model Development (Regression, Classification, Clustering)", "NLP (Sentiment Analysis, Topic Modeling)", "Statistical Analysis & Feature Engineering"], "🧠 Frameworks": ["LangChain", "LangGraph", "TensorFlow", "Scikit-learn", "PyTorch", "Pandas", "NumPy", "Beautifulsoup", "Playwright", "Selenium", "Keras", "OpenCV"], "☁️ Cloud & DevOps": ["AWS (EC2, S3, SageMaker)", "Microsoft Azure", "GCP", "CI/CD (Jenkins, GitLab CI)", "Docker & Kubernetes"], "📊 Data & BI": ["ETL & Data Warehousing", "Web Scraping", "Power Automate & Power Apps", "Power BI & Tableau"], "💻 Programming": ["Python", "SQL", "JavaScript"],}
PROFESSIONAL_EXPERIENCE = { "Software Engineer at Merkle CXM (May 2022 - present)": [ "Developed, trained, and deployed machine learning models using TensorFlow, PyTorch, and scikit-learn, improving prediction accuracy by 15%.", "Engineered robust data pipelines for large-scale data ingestion, reducing processing time by 40%.", "Designed generative AI solutions using GPT/Gemini models to automate workflows, boosting team productivity by 40%.", "Deployed and monitored AI/ML models on AWS, ensuring 99.9% uptime and scalability.", "Mentored junior engineers, improving team-wide adoption of best practices in prompt engineering and model optimization.", "Currently developing agentic AI systems using LangChain and LangGraph to reduce human interaction in complex workflows.", ]}
PROJECTS = { "E-commerce Product Data Extraction": {"description": "Developed Python-based web scraping pipelines to extract product details, reviews, and recommendations from e-commerce platforms, enabling data-driven insights for competitive analysis.", "tech": ["Python", "Beautifulsoup", "Playwright and Selenium", "Scrapy", "Pandas", "SQL"]}, "AI-Powered Customer Service Chatbot": {"description": "Built and deployed an AI-powered chatbot using GPT models and RAG to automate customer support, resolving over 60% of common inquiries and reducing response times by 75%.", "tech": ["Python", "LangChain", "OpenAI API", "Streamlit", "Docker"]}, "Automated Financial Reporting Workflow": {"description": "Created an automation workflow using Power Automate to streamline the generation of weekly financial reports, improving efficiency and reducing manual effort by 90%.", "tech": ["Power Automate", "SharePoint"]}, "Real-time Image Classification Model": {"description": "Developed and deployed an image classification model using CNNs in TensorFlow to classify product images from a live camera feed with an accuracy of 94%.", "tech": ["TensorFlow", "Keras", "OpenCV", "AWS SageMaker"]}}
CERTIFICATIONS_DATA = [ {"image_path": os.path.join(CERTIFICATIONS_DIR, "aws_certified_machine_learning_specialty.png"), "title": "AWS Certified Machine Learning – Specialty", "description": "Validated expertise in building, training, tuning, and deploying machine learning models using AWS services."}, {"image_path": os.path.join(CERTIFICATIONS_DIR, "IBM Data Science.png"), "title": "IBM Data Science Professional Certificate", "description": "Acquired proficiency in Python programming, SQL, data analysis, visualization, machine learning, and deep learning through a series of courses."},]
AWARDS_DATA = [ {"image_path": os.path.join(AWARDS_DIR, "RnR_Individual_Brilliance.jpg"), "title": "Individual Brilliance", "description": "Awarded for significant contributions in internal initiatives and client delivery."}, {"image_path": os.path.join(AWARDS_DIR, "Infinity_Award_Crawl_Build_AI_Re-engineering.JPG"), "title": "Crawl Build AI Re-engineering", "description": "Awarded for significant contributions to innovative AI solution development in 2023-24."}, {"image_path": os.path.join(AWARDS_DIR, "RnR_Meta_build_delivery_and_onboarding_team_Certificate.jpg"), "title": "Client Delivery and Onboarding", "description": "Awarded for significant contributions in team onboarding and client delivery in 2024"},]
EDUCATION = { "Institution": "M.H. Saboo Siddik College of Engineering, Mumbai", "Degree": "Bachelor of Engineering in Information Technology", "Graduation Year": "2022", "CGPA": "8.48 / 10.00"}
SOFT_SKILLS = ["Leadership & Mentoring", "Effective Communication", "Agile & Scrum Methodologies", "Creative Problem-Solving", "Stakeholder Collaboration"]

# --- CHATBOT KNOWLEDGE BASE & LOGIC ---
@st.cache_data
def get_knowledge_base():
    kb_parts=[f"Name: Nizaal Khot\nRole: AI/ML Engineer | Data Scientist\n\n## Professional Summary\n{PROFESSIONAL_SUMMARY}\n", "## Technical Skills\n" + "\n".join([f"- {cat.split(' ')[-1]}: {', '.join(skills)}" for cat, skills in TECHNICAL_SKILLS.items()]),"\n## Professional Experience\n" + "\n".join([f"- **{title}**\n" + "\n".join([f"  - {p.split('<')[0]}" for p in points]) for title, points in PROFESSIONAL_EXPERIENCE.items()]),"\n## Projects\n" + "\n".join([f"- **{title}**: {details['description'].split('<')[0]} (Tech: {', '.join(details['tech'])})" for title, details in PROJECTS.items()]),f"\n## Education\n- {EDUCATION['Degree']} from {EDUCATION['Institution']} ({EDUCATION['Graduation Year']}, CGPA: {EDUCATION['CGPA']})\n","## Certifications\n" + "\n".join([f"- **{cert['title']}**: {cert['description']}" for cert in CERTIFICATIONS_DATA]),"\n## Awards\n" + "\n".join([f"- **{award['title']}**: {award['description']}" for award in AWARDS_DATA]),"\n## Soft Skills\n- " + ", ".join(SOFT_SKILLS)]
    return "\n".join(kb_parts)

def get_chatbot_response(query, chat_history):
    if not GEMINI_MODEL: return "The chatbot is currently unavailable. Please check the API key configuration."
    KNOWLEDGE_BASE=get_knowledge_base()
    system_prompt=f"You are Nizaal Bot, a friendly AI assistant who will pretend to be Nizaal Khot. Answer questions ONLY based on the KNOWLEDGE BASE below. Be conversational and present your answers in clear format for the person to quickly understand. If the answer isn't in the knowledge base, say you don't have information on that topic. \n\nKNOWLEDGE BASE:\n{KNOWLEDGE_BASE}"
    try:
        chat=GEMINI_MODEL.start_chat(history=chat_history)
        response=chat.send_message(system_prompt + "\n\nUser Question: " + query)
        return response.text
    except Exception as e:
        return f"Sorry, an error occurred."


# --- MAIN APP LAYOUT ---
load_css()

# Define main layout columns
main_col, chat_col = st.columns([2, 1])

# --- SIDEBAR (Optional Navigation) ---
with st.sidebar:
    st.title("Quick Navigation")
    st.markdown("[Summary](#professional-summary)")
    st.markdown("[Skills](#technical-skills)")
    st.markdown("[Experience](#professional-experience)")
    st.markdown("[Projects](#projects-handled)")
    st.markdown("[Certifications](#certifications)")
    st.markdown("[Awards](#awards)")
    st.markdown("[Education](#education)")
    st.markdown("[Soft Skills](#soft-skills)")

# --- MAIN PORTFOLIO CONTENT ---
with main_col:
    # Header Section
    with st.container():
        col1, col2 = st.columns([0.3, 0.7], gap="large")
        with col1:
            if profile_pic_b64 := get_image_as_base64(PROFILE_PHOTO_PATH):
                st.markdown(f'<div class="profile-img"><img src="data:image/jpeg;base64,{profile_pic_b64}"></div>', unsafe_allow_html=True)
        with col2:
            st.title("Nizaal Khot")
            st.subheader("AI/ML Engineer | Data Scientist")
            st.write("Passionate about building intelligent systems that solve real-world problems.")
            # Social Icons
            icons = {
                "LinkedIn": (get_image_as_base64(LINKEDIN_ICON_PATH), "https://linkedin.com/in/nizaalkhot"),
                "GitHub": (get_image_as_base64(GITHUB_ICON_PATH), "https://github.com/nizaalkhot"),
                "Email": (get_image_as_base64(GMAIL_ICON_PATH), "mailto:nijaal.khot.1@gmail.com"),
            }
            social_icons_html = "".join([f'<a href="{url}" target="_blank"><img src="data:image/png;base64,{b64}" width="32"></a>' for name, (b64, url) in icons.items() if b64])
            st.markdown(f"<div class='social-icons'>{social_icons_html}</div>", unsafe_allow_html=True)
    
    st.divider()

    # Professional Summary
    st.markdown("<h2 id='professional-summary'>👨‍💻 Professional Summary</h2>", unsafe_allow_html=True)
    st.write(PROFESSIONAL_SUMMARY)
    st.divider()

    # Technical Skills
    st.markdown("<h2 id='technical-skills'>🛠️ Technical Skills</h2>", unsafe_allow_html=True)
    skill_tabs = st.tabs(list(TECHNICAL_SKILLS.keys()))
    for tab, (category, skills) in zip(skill_tabs, TECHNICAL_SKILLS.items()):
        with tab:
            st.markdown(''.join([f'<span class="skill-tag">{skill}</span>' for skill in skills]), unsafe_allow_html=True)
    st.divider()

    # Professional Experience
    st.markdown("<h2 id='professional-experience'>💼 Professional Experience</h2>", unsafe_allow_html=True)
    for title, details in PROFESSIONAL_EXPERIENCE.items():
        with st.expander(f"**{title}**", expanded=True):
            for point in details:
                st.markdown(f"- {point}", unsafe_allow_html=True)
    st.divider()

    # Projects Handled
    st.markdown("<h2 id='projects-handled'>🚀 Projects Handled</h2>", unsafe_allow_html=True)
    for title, details in PROJECTS.items():
        with st.expander(f"**{title}**"):
            st.markdown(details['description'], unsafe_allow_html=True)
            st.markdown(f"**Technologies:** {''.join([f'<span class=skill-tag>{t}</span>' for t in details['tech']])}", unsafe_allow_html=True)
    st.divider()

    # Certifications & Awards
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h2 id='certifications'>📜 Certifications</h2>", unsafe_allow_html=True)
        for cert in CERTIFICATIONS_DATA:
            if img_b64 := get_image_as_base64(cert["image_path"]):
                st.markdown(f'<div class="cert-award-item"><img src="data:image/png;base64,{img_b64}" alt="{cert["title"]}"><p><b>{cert["title"]}</b></p></div><br>', unsafe_allow_html=True)
    with col2:
        st.markdown("<h2 id='awards'>🏆 Awards</h2>", unsafe_allow_html=True)
        for award in AWARDS_DATA:
            if img_b64 := get_image_as_base64(award["image_path"]):
                st.markdown(f'<div class="cert-award-item"><img src="data:image/png;base64,{img_b64}" alt="{award["title"]}"><p><b>{award["title"]}</b></p></div><br>', unsafe_allow_html=True)
    st.divider()

    # Education & Soft Skills
    st.markdown("<h2 id='education'>🎓 Education</h2>", unsafe_allow_html=True)
    st.write(f"**{EDUCATION['Degree']}** | {EDUCATION['Institution']} ({EDUCATION['Graduation Year']}) | CGPA: {EDUCATION['CGPA']}")
    st.markdown("---")
    st.markdown("<h2>🤝 Soft Skills</h2>", unsafe_allow_html=True)
    st.markdown(''.join([f'<span class="skill-tag">{skill}</span>' for skill in SOFT_SKILLS]), unsafe_allow_html=True)


# --- FIXED CHATBOT COLUMN ---
with chat_col:
    st.markdown('<div class="sticky-chat-container">', unsafe_allow_html=True)
    st.subheader("Chat with Nizaal Bot 💬")
    st.write("Ask me anything about me!")

    # Initialize chat state
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hi there! I am Nizaal. How can I help you?"}]
    if "chat_history_gemini" not in st.session_state:
        st.session_state.chat_history_gemini = []

    # Display chat messages
    chat_log_container = st.container()
    with chat_log_container:
        st.markdown('<div class="chat-log">', unsafe_allow_html=True)
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        st.markdown('</div>', unsafe_allow_html=True)

    # Chat input
    if prompt := st.chat_input("Ask a question..."):
        # Add user message to state and display it
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Get and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_chatbot_response(prompt, chat_history=st.session_state.chat_history_gemini)
                st.markdown(response)
        
        # Add assistant response to state
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Update Gemini's history
        st.session_state.chat_history_gemini.append({"role": "user", "parts": [prompt]})
        st.session_state.chat_history_gemini.append({"role": "model", "parts": [response]})
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)