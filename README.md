# Nizaal Khot | AI/ML Engineer Portfolio

This repository hosts a dynamic and interactive personal portfolio, built using Streamlit, designed to showcase the skills, projects, and professional experience of me (Nizaal Khot), an AI/ML Engineer. This application serves as a comprehensive online resume, highlighting technical expertise, professional achievements, and educational background in an engaging format.

## Table of Contents

- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Directory Structure](#directory-structure)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Customization](#customization)
## Features

The portfolio application includes the following sections and interactive elements:

* **Dynamic Header:** Displays a profile photo, name, title, and social media links (LinkedIn, GitHub, Gmail).
* **Professional Summary:** A concise overview of the engineer's experience and expertise.
* **Technical Skills:** An interactive tabbed interface categorizing skills in ML & AI, Frameworks, Cloud & DevOps, Data & BI, and Programming.
* **Professional Experience:** Detailed description of roles and responsibilities with quantifiable achievements.
* **Projects Handled:** An interactive expander section for each project, revealing its description and technologies used upon click.
* **Certifications & Awards:** Auto-scrolling image carousels displaying certifications and awards.
* **Education & Soft Skills:** Dedicated sections for academic background and key soft skills.
* **Responsive Design:** Custom CSS ensures a visually appealing and responsive layout across various devices.

## Setup and Installation

To run this portfolio locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/nizaalkhot/my-profile.git
    cd my-profile
    ```

2.  **Create a Python virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required libraries:**
    ```bash
    pip install streamlit
    ```

4.  **Create the `media` directory:**

    In the same directory as `main.py`, create a folder named `media`.

5.  **Create sub-folders for images:**

    Inside the `media` directory, create two sub-folders: `certifications` and `awards`.

6.  **Place your media files:**
    * Place your profile photo (e.g., `profile-photo.jpg`) directly inside the `media` folder.
    * Place your social media icons (e.g., `linkedin.png`, `gmail.png`, `github.png`) directly inside the `media` folder.
    * Place your certification images inside the `media/certifications` folder.
    * Place your award images inside the `media/awards` folder.

    **Example `media` directory structure:**

    ```
    .
    ├── main.py
    └── media/
        ├── profile-photo.jpg
        ├── linkedin.png
        ├── gmail.png
        ├── github.png
        ├── certifications/
        │   ├── cert1.png
        │   └── cert2.jpg
        └── awards/
            ├── award1.png
            └── award2.jpeg
    ```

## Directory Structure

    ```
    .
    ├── main.py                     # The main Streamlit application script
    └── media/                      # Directory for all images
        ├── profile-photo.jpg       # Your profile picture
        ├── linkedin.png            # LinkedIn icon
        ├── gmail.png               # Gmail icon
        ├── github.png              # GitHub icon
        ├── certifications/         # Folder for certification images
        │   └── <your_cert_image>.png/jpg
        └── awards/                 # Folder for award images
            └── <your_award_image>.png/jpg
    ```

## Usage

To run the Streamlit application, open your terminal or command prompt, navigate to the project directory, and execute:

```bash
streamlit run main.py
```
This will open the portfolio in your default web browser.


## Technologies Used
* **Streamlit**: For building the interactive web application.
* **Python**: The core programming language.
* **Base64**: Used for embedding images directly into HTML/CSS.
* **Custom CSS**: For styling and ensuring a responsive, modern design.

## Customization
You can easily customize the content of this portfolio:

1. **Media Files**: Update the images in the media and its subdirectories as described in Setup and Installation.
2. **Personal Information**:
    * Modify st.title("Nizaal Khot") and st.subheader("AI/ML Engineer | Data Scientist") in the  Header Section.
    * Update the st.write description below the subheader.
    * Change the social media links in social_icons_html.
3. **Professional Summary**: Edit the text within the Professional Summary container.
4. **Technical Skills**: Modify the TECHNICAL_SKILLS dictionary to add, remove, or change skill categories and individual skills.
5. **Professional Experience**: Update the Professional Experience section with your roles, companies, dates, and bullet points. Remember to use unsafe_allow_html=True if you're embedding custom HTML for metrics.
6. **Projects Handled**: Modify the PROJECTS dictionary to add, remove, or update your projects, their descriptions, and the technologies used.
7. **Education**: Update the Education section with your institution, degree, graduation year, and CGPA.
8. **Soft Skills**: Edit the markdown list under Soft Skills.