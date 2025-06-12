import streamlit as st
import base64
import os

def main():
    # Set page config for a wider layout and custom title
    st.set_page_config(layout="wide", page_title="Nizaal Khot - AI/ML Engineer Profile")

    # --- Creative and Interactive Header Section ---
    # Load Inter font and apply custom CSS for the header
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap" rel="stylesheet">
        <style>
            .header-container {
                font-family: 'Inter', sans-serif;
                background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%); /* Blue-purple gradient */
                padding: 30px;
                border-radius: 15px;
                color: white;
                text-align: center;
                box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
                margin-bottom: 30px;
                position: relative;
                overflow: hidden;
            }
            .header-container h1 {
                font-size: 3.5em; /* Larger font for the name */
                margin-bottom: 5px;
                font-weight: 800; /* Extra bold */
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            }
            .header-container h2 {
                font-size: 1.8em;
                margin-top: 0;
                font-weight: 400;
                opacity: 0.9;
            }
            .header-contact-info {
                display: flex;
                justify-content: center;
                gap: 25px; /* Space between contact items */
                margin-top: 20px;
                flex-wrap: wrap; /* Allow wrapping on smaller screens */
            }
            .header-contact-info a {
                color: white;
                text-decoration: none;
                font-size: 1.1em;
                display: flex;
                align-items: center;
                transition: transform 0.2s ease-in-out;
            }
            .header-contact-info a:hover {
                transform: translateY(-3px); /* Subtle hover effect */
                color: #e0f2f7; /* Lighter color on hover */
            }
            .header-contact-info svg {
                margin-right: 8px;
                width: 20px;
                height: 20px;
                fill: white; /* Ensures icons are white */
            }
            /* Waving hand animation */
            .waving-hand {
                display: inline-block;
                animation: wave-animation 2.5s infinite;
                transform-origin: 70% 70%;
                margin-left: 10px;
                font-size: 0.8em; /* Smaller relative to the name */
            }

            @keyframes wave-animation {
                0% { transform: rotate( 0.0deg) }
                10% { transform: rotate(14.0deg) }
                20% { transform: rotate(-8.0deg) }
                30% { transform: rotate(14.0deg) }
                40% { transform: rotate(-4.0deg) }
                50% { transform: rotate(10.0deg) }
                60% { transform: rotate( 0.0deg) }
                100% { transform: rotate( 0.0deg) }
            }
            /* Responsive adjustments */
            @media (max-width: 600px) {
                .header-container h1 {
                    font-size: 2.5em;
                }
                .header-container h2 {
                    font-size: 1.4em;
                }
                .header-contact-info {
                    flex-direction: column; /* Stack contact info vertically */
                    gap: 10px;
                }
            }
        </style>

        <div class="header-container">
            <h1>Nizaal Khot <span class="waving-hand">👋</span></h1>
            <h2>AI/ML Engineer | Data Scientist</h2>
            <div class="header-contact-info">
                <a href="https://linkedin.com/in/nizaalkhot" target="_blank">
                    <!-- LinkedIn Icon SVG (Font Awesome equivalent) -->
                    <svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                        <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/>
                        <path d="M2 9h4v12H2zM4 6a2 2 0 1 0 0-4 2 2 0 0 0 0 4z"/>
                    </svg>
                    LinkedIn
                </a>
                <a href="tel:+919594988780">
                    <!-- Phone Icon SVG (Font Awesome equivalent) -->
                    <svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                        <path d="M20 15.5c-1.25 0-2.45-.2-3.57-.57-.35-.11-.74-.03-1.01.24l-2.2 2.2c-2.83-1.44-5.15-3.75-6.59-6.59l2.2-2.2c.27-.27.35-.66.24-1.01-.37-1.12-.57-2.32-.57-3.57 0-.55-.45-1-1-1H3c-.55 0-1 .45-1 1 0 9.39 7.61 17 17 17 .55 0 1-.45 1-1v-3.5c0-.55-.45-1-1-1z"/>
                    </svg>
                    +91 9594988780
                </a>
                <a href="mailto:nijaal.khot.1@gmail.com">
                    <!-- Email Icon SVG (Font Awesome equivalent) -->
                    <svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                        <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
                    </svg>
                    nijaal.khot.1@gmail.com
                </a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # --- PROFESSIONAL SUMMARY ---
    st.subheader("PROFESSIONAL SUMMARY")
    st.write("""
    Results-oriented AI/ML Engineer with 3+ years of experience in developing and deploying scalable
    Machine Learning, Deep Learning, and NLP solutions. Proven track record in leading end-to-end AI
    project lifecycles, from data collection to model deployment and optimization. Expertise in leveraging
    generative AI, NLP, and LLMs for business intelligence, process automation, and predictive analytics.
    Adept at collaborating with cross-functional teams to integrate AI solutions and enhance operational
    efficiency. Passionate about driving innovation and delivering scalable, reliable solutions with a strong
    focus on quality and compliance.
    """)

    st.markdown("---")

    # --- TECHNICAL SKILLS ---
    st.subheader("TECHNICAL SKILLS")
    st.markdown("""
    * **Machine Learning & AI:** Model development (Regression, Classification, Clustering, CNNs,
        Object Detection), Generative AI, NLP (sentiment analysis, topic modeling, document
        summarization), LLM fine-tuning, GPT/Gemini models, AI-driven automation, model
        optimization, prompt engineering, agentic AI development, Statistical analysis, Feature
        Engineering.
    * **Deep Learning Frameworks:** TensorFlow, PyTorch, scikit-learn, LangChain, LangGraph,
        Pandas, NumPy, Keras, OpenCV.
    * **Generative AI Technologies:** OpenAI API, Google Gemini, LLMs (GPT/Gemini models),
        Retrieval-Augmented Generation (RAG) concepts applied in solutions.
    * **Data Engineering:** Data pipelines (ETL, web scraping, data preprocessing, large-scale dataset
        management, data warehousing), optimized data ingestion and processing.
    * **Programming Languages:** Python, SQL, JavaScript.
    * **Cloud Platforms & Deployment:** AWS (EC2, S3, SageMaker), Azure, GCP, CI/CD (Jenkins,
        GitLab CI), containerization (Docker, Kubernetes), On-premises deployment strategies.
    * **Automation & BI:** Power Automate, Power Apps, Power BI, workflow automation, Tableau,
        interactive dashboards.
    * **Agile & Version Control:** Git, GitHub, GitLab, Bitbucket, Agile methodologies.
    * **Communication & Leadership:** Stakeholder collaboration, mentoring, technical
        documentation.
    """)

    st.markdown("---")

    # --- CERTIFICATIONS ---
    st.subheader("CERTIFICATIONS")
    st.markdown("""
    * AWS Certified: Machine Learning Specialty - AWS
    * Microsoft Certified: AI Fundamentals - Microsoft
    * IBM Data Science Professional Certificate - IBM
    """)

    st.markdown("---")

    # --- EDUCATION ---
    st.subheader("EDUCATION")
    st.write("### Bachelor in Engineering in Information Technology (2022)")
    st.write("CGPA: 8.48/10.00")
    st.write("M.H. Saboo Siddik College of Engineering, Mumbai, India")

    st.markdown("---")

    # --- PROFESSIONAL EXPERIENCE ---
    st.subheader("PROFESSIONAL EXPERIENCE")
    st.write("### Data Engineer | AI/ML Specialist")
    st.write("Merkle CXM - Mumbai, India | May 2022 - present")
    st.markdown("""
    * Developed, trained, and deployed machine learning models using TensorFlow, PyTorch, and
        scikit-learn for various business applications.
    * Designed and implemented generative AI solutions using GPT/Gemini models to automate
        workflows, optimize processes, and drive business development.
    * Engineered robust data pipelines for large-scale data ingestion and processing, ensuring data
        quality and reliability.
    * Collaborated with cross-functional teams to identify and translate business requirements into
        effective AI/ML solutions.
    * Optimized model performance through hyperparameter tuning and feature engineering.
    * Deployed and monitored AI/ML models in production environments, ensuring scalability and
        reliability using cloud platforms like AWS.
    * Utilized CI/CD pipelines to streamline model deployment and updates.
    * Mentored junior engineers on prompt engineering, model optimization, and best practices.
    * Currently developing agentic AI systems utilizing frameworks like LangChain and LangGraph for
        effective and efficient work processes with reduced human interaction.
    """)

    st.markdown("---")

    # --- PROJECTS HANDLED ---
    st.subheader("PROJECTS HANDLED")
    st.markdown("""
    * **E-commerce Product Data Extraction:** Developed Python-based web scraping pipelines to
        extract product details, reviews, and recommendations from e-commerce platforms, enabling
        data-driven insights.
    * **AI-Powered Chatbots:** Built and deployed AI-powered chatbots using GPT/Gemini models to
        automate enhance user experience.
    * **Automated Workflow Implementation:** Created automation workflows using Power
        Automate to streamline business processes, improving efficiency and reducing manual effort.
    * **Large-Scale Data Pipeline Optimization:** Optimized data pipelines for efficient ingestion
        and processing of large datasets, ensuring data integrity and performance.
    * **Image Classification Model:** Developed and deployed an image classification model using
        convolutional neural networks (CNNs) in TensorFlow to classify product images.
    """)

    st.markdown("---")

    # --- SOFT SKILLS (From Professional Skills) ---
    st.subheader("SOFT SKILLS")
    st.markdown("""
    * Communication
    * Teamwork
    * Leadership
    * Problem-Solving
    """)

if __name__ == "__main__":
    main()
